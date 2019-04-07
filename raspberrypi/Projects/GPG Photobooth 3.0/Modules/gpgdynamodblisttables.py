import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

for table in dynamodb.tables.all():
    print(table);