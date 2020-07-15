import boto3
from boto3.dynamodb.conditions import Key
def lambda_handler(event, context):
    TABLE_NAME1 = "netflix"
    Movie_Title=event['title']
    # Creating the DynamoDB Client
    dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

    # Creating the DynamoDB Table Resource
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table(TABLE_NAME1)
    response = table.get_item(
        Key={
            'title': Movie_Title
        
        }
    )
    print(response['Item'])
    return response
