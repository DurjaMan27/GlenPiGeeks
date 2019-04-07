import boto3

# Create an S3 client
s3 = boto3.client('s3', 'us-east-1')
bucket_name = 'gpgphotobooth30'

def upload_image(filename, fullname):
	file = open(filename,'rb')
	ret = s3.put_object(Body=file, Bucket=bucket_name, Key=filename, Metadata={'FullName':fullname})
	print(ret)
	return
	

#filename = '/home/ec2-user/environment/Images/guru.jpg'
filename=input("Enter File location: ")

fullname=input('Enter Full Name')

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
upload_image(filename, fullname)
 
