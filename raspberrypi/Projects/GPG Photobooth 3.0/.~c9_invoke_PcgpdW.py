import os
import boto3
import s3
from flask import Flask, request, redirect, url_for
from forms import RegistrationForm, LoginForm
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dynamodb = boto3.client('dynamodb', "us-east-1")
s3 = boto3.client('s3', 'us-east-1')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_image(filename, fullname):
	file = open(filename,'rb')
	object = s3.Object('gpgphotobooth3',filename)
	ret = object.put(Body=file,
			Metadata={'FullName':fullname}
			)
	print(ret)
	return
	
def update_index(tableName,ReferenceImageID, faceId, fullName, Confidence, NumberOfFaces):
	response = dynamodb.put_item(
	TableName=tableName,
	Item={
		'ReferenceImageID': {'S': ReferenceImageID},
		'FullName': {'S': fullName},
		'Confidence': {'S': Confidence},
		'NumberOfFaces' : {'S': NumberOfFaces},
		'FaceID' : {'S':faceId}
		}
	)

def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.index_faces(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		CollectionId=collection_id,
		ExternalImageId="taifur",
	    DetectionAttributes=attributes,
	)
	if response['`																																																ResponseMetadata']['HTTPStatusCode'] == 200:
		faceId = response['FaceRecords'][0]['Face']['FaceId']
		print(faceId)
		ret = s3.head_object(Bucket=bucket,Key=key)
		personFullName = ret['Metadata']['fullname']
		#print(ret)
		print(personFullName)
		update_index('gpgphotobooth3',faceId,personFullName)
		
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
