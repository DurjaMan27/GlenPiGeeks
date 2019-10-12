import os
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

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
s3Resource = boto3.resource('s3', 'us-east-1')
s3 = boto3.client('s3')

client=boto3.client('rekognition', 'us-east-1')
referenceLookupPath = '/home/ec2-user/environment/GlenPiGeeks/raspberrypi/Projects/GPG Photobooth 3.0/GPG Uploader 1.0/liveimages/'

referenceLookupImage = referenceLookupPath + str(datetime.now()) + str(random()) + '.jpg'
print(referenceLookupImage)
# replace bucket, collectionId, and photo with your values.
bucket='gpgphotoboothliveimages'
referencebucket='gpgphotobooth30'
collectionId='GlenPiGeeks'
table = dynamodb.Table('gpgphotobooth3')

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
    
def compareliveimage(filepath):

    print(filepath)    
    filename=path_leaf(filepath)
    print(filename)
    
    s3.upload_file(filepath, bucket, filename)

    #For live faces
    indexfacesresponse=client.index_faces(CollectionId=collectionId,
                                    Image={'S3Object':{'Bucket':bucket,'Name':filename}},
                                    #ExternalImageId=filename,
                                    MaxFaces=1,
                                    QualityFilter="AUTO",
                                    DetectionAttributes=['ALL'])

    threshold = 50
    maxFaces=1
    print ('Results for ' + filename) 	
    print('Faces indexed:')						
    for faceRecord in indexfacesresponse['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            searchfacesresponse=client.search_faces(CollectionId=collectionId,
                                    FaceId=faceRecord['Face']['FaceId'],
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
            #Program finds match and prints a message; if it cannot find a match, it will print a message saying so
            faceMatches=searchfacesresponse['FaceMatches']
            print ('Matching faces')
            for match in faceMatches:
                    print ('FaceId:' + match['Face']['FaceId'])
                    print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                    itemresponse = table.get_item(
                        Key={
                            'FaceID': match['Face']['FaceId']
                        }) 
                    item = itemresponse['Item'] 
                    print(str(item['ReferenceImageID']))
                    #print(referenceLookupImage)
                    referenceLookupImage = referenceLookupPath + str(datetime.now())  + '.jpg'
                    s3Resource.Bucket(referencebucket).download_file(item['ReferenceImageID'], referenceLookupImage)
                    


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("uploadliveimage.html")

@app.route("/upload", methods=["POST"])
def upload():
    for the_file in os.listdir(referenceLookupPath):
        file_path = os.path.join(referenceLookupPath, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    target = os.path.join(APP_ROOT, 'liveimages')
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
        compareliveimage(destination)
    
    target = os.path.join(APP_ROOT, 'referenceimages/')
    reference_image_names = os.listdir(target)
    print(target)
    target = os.path.join(APP_ROOT, 'liveimages/')
    live_image_names = os.listdir(target)
    print(target)
    print(live_image_names)
    print(reference_image_names)
    return render_template("displayreferenceliveimage.html", live_image_names=live_image_names, ref_image_names=reference_image_names)
    
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("liveimages", filename)

@app.route('/uploadreference/<filename>')
def send_ref_image(filename):
    return send_from_directory("liveimages", filename)

@app.route('/gallery')
def get_gallery():
    target = os.path.join(APP_ROOT, 'referenceimages/')
    reference_image_names = os.listdir(target)
    target = os.path.join(APP_ROOT, 'liveimages/')
    live_image_names = os.listdir(target)
    print(live_image_names)
    print(reference_image_names)
    return render_template("gallery.html", live_image_names=live_image_names, ref_image_names=reference_image_names)
    
if __name__ == "__main__":
    app.run(port=8080, debug=True)