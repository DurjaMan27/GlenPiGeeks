import os
from uuid import uuid4 
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import decimal
from flask import Flask, request, render_template, send_from_directory
import ntpath
from random import random
import os, shutil
from random import seed
from datetime import date, datetime, time, timedelta
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
s3Resource = boto3.resource('s3', 'us-east-1')
s3 = boto3.client('s3')
client=boto3.client('rekognition', 'us-east-1')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
bucket='gpgphotoboothliveimages'
referencebucket='gpgphotobooth30'
collectionId='GlenPiGeeks'
table = dynamodb.Table('gpgphotobooth3')

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def upload_image(filename, firstname, lastname):
	file = open(filename,'rb')
	referencefilepath = filename
	referencefilename = path_leaf(referencefilepath)
	print(referencefilename)
	ret = s3.put_object(Body=file, Bucket=referencebucket, Key=referencefilename, Metadata={'FirstName':firstname, 'LastName':lastname})
	print(ret)
	return
	
#For reference image
def update_index(tableName,ReferenceImageID, faceId, firstName, lastName):
	response = dynamodb.put_item(
	TableName=tableName,
	Item={
		'FaceID' : {'S':faceId},
		'ReferenceImageID': {'S': ReferenceImageID},
		'FirstName': {'S': firstName},
		'LastName': {'S': lastName}
		}
	)
	
@app.route("/")
def index():
    return render_template("uploadreferenceimage.html")

@app.route("/upload", methods=["POST"])
def upload():
    firstname = request.form['firstname']
    print(firstname)
    lastname = request.form['lastname']
    print(lastname)
    target = os.path.join(APP_ROOT, 'referenceimages/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        upload_image(destination, firstname, lastname)
        
        #For live faces
        response=client.index_faces(CollectionId=collectionId,
                                    Image={'S3Object':{'Bucket':referencebucket,'Name':filename}},
                                    #ExternalImageId=filename,
                                    MaxFaces=1,
                                    QualityFilter="AUTO",
                                    DetectionAttributes=['ALL'])
    
        print ('Results for ' + filename) 	
        print('Faces indexed:')						
        for faceRecord in response['FaceRecords']:
             print('  Face ID: ' + faceRecord['Face']['FaceId'])
             print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
             #update_index('gpgphotobooth3',filename, faceRecord['Face']['FaceId'], firstname, lastname)
    
    
        print('Faces not indexed:')
        for unindexedFace in response['UnindexedFaces']:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("displayreferenceimage.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("referenceimages", filename)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
