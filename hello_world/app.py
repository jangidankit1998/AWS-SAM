from __future__ import print_function
import json
import boto3

# import requests

def scheduled_handler(event, context):
    
    #call Hello world api handler
    api_handler_response = lambda_handler({}, context)

    #produce message to SQS queue
    sqs = boto3.client('sqs') 
    queue_url = 'https://sqs.eu-north-1.amazonaws.com/300099455105/sam-app-MySqsQueue-BXyh2PNAD4Q1'

    message_body = {
        "message": "Hello Sending message",
        "api_response": api_handler_response
    }

    sqs.send_message(
        QueueUrl = queue_url,
        MessageBody = json.dumps(message_body)
    )


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello we are in api lambda handler!",
            # "location": ip.text.replace("\n", "")
        }),
    }

def sqs_handler(event, context):
    for record in event['Records']:
        #print("test")
        payload = record["body"]
        print("Message received by sqs : ",str(payload))
