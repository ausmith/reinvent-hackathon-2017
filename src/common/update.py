import os
import boto3
from urllib.parse import parse_qs


class Update():

    payload = None

    def __init__(self, event):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(os.environ['ddb'])
        self.event = event

    def execute(self):
        self.buildDataStruct()
        self.table.put_item(Item=self.payload)
        return True

    def buildDataStruct(self):
        sms_data = parse_qs(self.event['body'])
        self.payload = {
            'smssid': sms_data['SmsSid'][0],
            'update': sms_data['Body'][0],
            'from_number': sms_data['From'][0]
        }
