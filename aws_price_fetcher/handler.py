from typing import Any, Dict, List

from requests import Response

import requests
import logging

import boto3

from dynamodb import dynamo_db_client


GASOLINE_PRICE_TABLE_NAME = "GasolinePrices"

GASOLINE_API_URL = "https://data.ny.gov/resource/wuxr-ni2i.json"

SNS_ARN = "arn:aws:sns:us-east-1:008735640664:price-updates-topic"

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

def price_fetcher(event: Dict[str, Any], _: Any) -> None:
    """
    Fetches gasoline price from public API
    Calculate the most recent gasoline price with the last record saved in the dynamoDB table
    if the price has dropped, it inserts that record into the table otherwise, it skips it.
    """
    items = query(GASOLINE_PRICE_TABLE_NAME)
    LOG.info(f"Got items: {items}")

    gasoline_api_response = request()
        
    gasoline_api_json = gasoline_api_response.json()

    most_recent_gasoline_price: Dict = gasoline_api_json[0]
    LOG.info(f"Got most recent gasoline price: {most_recent_gasoline_price}")

    published_at = most_recent_gasoline_price['date']
    gasoline_price = most_recent_gasoline_price['new_york_state_average_gal']

    if items:
        previous_gasoline_price = float(items[0]['newYorkStateAverageGal'])
        LOG.info(f'Got previous previous_gasoline_price {previous_gasoline_price}')

        recent_gasoline_price = float(gasoline_price) 

        price_has_dropped = recent_gasoline_price < previous_gasoline_price

        if not price_has_dropped:
            LOG.info("Skipping insertion because price hasn't dropped")
            return

    response = insert(GASOLINE_PRICE_TABLE_NAME, published_at=published_at, gasoline_price=gasoline_price)
    LOG.info(f"Got response: {response}")
      
    return None

def price_publisher(event: Dict[str, Any], _: Any) -> None:
    """
    Get dynamo DB events and send information to the user.
    """
    LOG.info(f'Got event {event}')
    record = event['Records'][0]
    most_recent_gasoline_price = record['dynamodb']['NewImage']['newYorkStateAverageGal']['S']
    message = f'🛡🛡🛡 Gasoline price {most_recent_gasoline_price} have fell 🛡🛡🛡'
    subject = 'A gasoline price dropped has been detected'
    send_sns(message, subject)


def send_sns(message, subject):
    client = boto3.client("sns")
    response = client.publish(
        TopicArn=SNS_ARN, Message=message, Subject=subject)
    return response

def query(table_name: str) -> List:
    """
    Makes a query to dynamo_db
    """
    table = dynamo_db_client.Table(table_name)

    response = table.scan()
    return response['Items']

def insert(table_name: str, *, published_at: str, gasoline_price: str) -> Dict:
    """
    Insert an item to dynamo_db
    """
    table = dynamo_db_client.Table(table_name)
    response = table.put_item(
       Item={
           'publishedAt': published_at,
           'newYorkStateAverageGal': gasoline_price
       }
    )
    return response

def request() -> Response:
    response: Response = requests.get(GASOLINE_API_URL)
    LOG.info(f"Got status_code: {response.status_code}")
        
    if response.status_code != 200:
        raise SystemError()

    return response