from typing import Any, Dict
from boto3.dynamodb.conditions import Key

from dynamodb import dynamo_db_client

def compute(event: Dict[str, Any], _: Any) -> None:
    """
    """
    _query('GasolinePrices')


def _query(table_name: str) -> None:
    table = dynamo_db_client.Table(table_name)

    response = table.scan()
    print('response', response)