from __future__ import print_function # Python 2/3 compatibility

import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

for table in dynamodb.tables.all():
    print(table);
    
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

table = dynamodb.Table('gpgphotobooth3')

faceid = input('Please Enter FaceID')

print("Looking up Glen Pi Geeks Photobooth Items")

queryresponse = table.query(
    KeyConditionExpression=Key('FaceID').eq(faceid)
)

itemresponse = table.get_item(
    Key={
        'FaceID': faceid
    })

item = itemresponse['Item']
print(str(item['FaceID']))
#print(str(item['Confidence']))
print(str(item['FirstName']))
print(str(item['LastName']))
print(str(item['ReferenceImageID']))


for i in queryresponse[u'Items']:
    print(json.dumps(i, cls=DecimalEncoder))
    