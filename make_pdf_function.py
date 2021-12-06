import boto3
import json
import datetime

s3 = boto3.client('s3')

def handler(event, context):
    print(event)
    bucket_name = event['pathParameters']['bucket']
    file_name = event['queryStringParameters']['file']

    data = {
        'bucket': bucket_name,
        'file': file_name,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }


    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {'Content-Type': 'application/json'}
    }
