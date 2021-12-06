import boto3
import base64

s3 = boto3.client('s3')

def handler(event, context):
    bucket = event['pathParameters']['bucket']
    file = event['queryStringParameters']['file']

    fileObj = s3.get_object(Bucket=bucket, Key=file)
    file_content = fileObj['Body'].read()

    print(bucket, file)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/pdf',
            'Content-Disposition': 'attachment; filename={}'.format(file_content)
        },
        'body': base64.b64encode(file_content),
        'isBase64Encoded': True
    }
