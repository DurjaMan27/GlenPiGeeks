import boto3

# Create an S3 client
s3 = boto3.client('s3', 'us-east-1')
bucket_name = 'gpgphotobooth30'
table_name = 'gpgphotobooth3'

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Movies')

def upload_image(filename, firstname, lastname):
	file = open(filename,'rb')
	ret = s3.put_object(Body=file, Bucket=bucket_name, Key=filename, Metadata={'FirstName':firstname, 'LastName':lastname})
	print(ret)
	return
	

	
#filename = '/home/ec2-user/environment/Images/guru.jpg'
filename=input("Enter File location: ")

firstname=input('Enter First Name')
lastname=input('Enter Last Name')
# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
upload_image(filename, firstname, lastname)
