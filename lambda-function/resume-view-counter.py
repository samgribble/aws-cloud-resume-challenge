import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Resume-Challenge')
    
    response = table.get_item(Key={'ID':'1'})
    
    if 'Item' in response:
        current_views = response['Item']['Views']
        print(f"Current Views: {current_views}")
        
        new_views = current_views + 1
        
        response = table.put_item(Item={
            'ID':'1',
            'Views': new_views
        })
        
        return new_views