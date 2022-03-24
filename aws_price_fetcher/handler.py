from typing import Any, Dict, List

from dynamodb import dynamo_db_client

from settings import GASOLINE_API_URL

def compute(event: Dict[str, Any], _: Any) -> None:
    """
    """
    items = query('GasolinePrices')

    if not items:
        pass
        # Table is empty, we need to get the last result from API
        
    return None

def query(table_name: str) -> List:
    table = dynamo_db_client.Table(table_name)

    response = table.scan()
    return response['Items']
