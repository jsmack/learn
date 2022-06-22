import json

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from datetime import datetime
from zoneinfo import ZoneInfo

import boto3

translate = boto3.client('translate')


dynamodb_translate_tbl = boto3.resource('dynamodb').Table('k-test-translate')


def lambda_handler(event, context):
    logger.debug(event)
    # TODO implement
    
    #input_text = 'さようなら'
    input_text = event['queryStringParameters']['input_text']
    
    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )
    
    output_text = response.get('TranslatedText')
    dynamodb_translate_tbl.put_item(
        Item = {
            'timestamp': datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%d%H%M%S"),
            'input_text': input_text,
            'output_text': output_text
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        }),
        'isBase64Encoded': False,
        'headers': {}
    }
