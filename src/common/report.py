import os
import time
import boto3
from boto3.dynamodb.conditions import Attr


class Report():

    payload = None

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(os.environ['ddb'])
        self.s3 = boto3.client('s3')
        self.size = 0

    def execute(self):
        data = self.fetchData()
        self.s3.put_object(
                ACL = 'private',
                Body = data,
                Bucket = os.environ['report_bucket'],
                Key = time.strftime("%Y%m%d%H")
            )
        self.size = len(data)
        return True

    def fetchData(self):
        text = ""

        updates = self.table.query(KeyConditionExpression=Attr('update').exists())
        for i in updates['Items']:
            text += i['update']
            text += "\n"

        return text


