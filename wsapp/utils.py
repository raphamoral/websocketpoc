import os
import boto3
from boto3.dynamodb.conditions import Key


def get_table():
    table_name = os.environ.get("DYNAMO_TABLE", "example_table")
    region = os.environ.get("AWS_REGION", "us-east-1")
    return boto3.resource("dynamodb", region_name=region).Table(table_name)


def fetch_items(api_type: int):
    table = get_table()
    response = table.query(KeyConditionExpression=Key("api_type").eq(api_type))
    return response.get("Items", [])
