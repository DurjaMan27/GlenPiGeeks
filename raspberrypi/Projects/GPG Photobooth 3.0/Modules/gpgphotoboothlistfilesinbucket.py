import boto3

# Create an S3 client
s3 = boto3.client('s3', 'us-east-1')

bucket = input('Enter Bucket Name: ')
for key in s3.list_objects(Bucket=bucket)['Contents']:
    print(key['Key'])