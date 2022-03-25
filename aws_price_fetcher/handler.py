from typing import Any, Dict, List

from requests import Response

import requests
import logging

from dynamodb import dynamo_db_client


GASOLINE_PRICE_TABLE_NAME = "GasolinePrices"

GASOLINE_API_URL = "https://data.ny.gov/resource/wuxr-ni2i.json"

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

def compute(event: Dict[str, Any], _: Any) -> None:
    """
    """
    items = query(GASOLINE_PRICE_TABLE_NAME)
    LOG.info(f"Got items:", extra={'items': items})

    if not items:
        # Table is empty, we need to get the last result from API
        gasoline_api_response = request()
        LOG.info(f"Got status_code: {gasoline_api_response.status_code}")
        
        if gasoline_api_response.status_code != 200:
            raise SystemError()

        gasoline_api_json = gasoline_api_response.json()

        most_recent_gasoline_price: Dict = gasoline_api_json[0]
        LOG.info(f"Got most recent gasoline price:", extra={'most_recent_gasoline_price': most_recent_gasoline_price})

        published_at = most_recent_gasoline_price['date']
        gasoline_price = most_recent_gasoline_price['new_york_state_average_gal']

        response = insert(GASOLINE_PRICE_TABLE_NAME, published_at=published_at, gasoline_price=gasoline_price)
        LOG.info(f"Got response:", extra={'response': response})
        
    return None

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
    return requests.get(GASOLINE_API_URL)