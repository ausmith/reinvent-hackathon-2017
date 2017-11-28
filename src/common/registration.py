import os
import boto3
from urllib.parse import unquote


class Registration():

    payload = None

    def __init__(self, event):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(os.environ['ddb'])
        self.event = event

    def execute(self):
        self.buildDataStruct()
        return self.table.put_item(Item=self.payload)

    def buildDataStruct(self):
        sms_data = self.event['body'].split('&')
        sid = sms_data[2].split('=')
        email = sms_data[16].split('=')
        from_number = sms_data[6].split('=')
        self.payload = {
            'smssid': unquote(sid[1]),
            'email': unquote(email[1]),
            'from_number': unquote(from_number[1])
        }
