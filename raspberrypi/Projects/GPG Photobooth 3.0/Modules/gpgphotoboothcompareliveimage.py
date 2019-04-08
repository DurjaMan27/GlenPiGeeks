#gpgphotoboothcompareliveimage.py
#Program is for security person to take a live image and compare it to reference images
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import decimal
import ntpath

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
s3 = boto3.client('s3')
client=boto3.client('rekognition', 'us-east-1')
referenceLookupImage = '/home/ec2-user/environment/GlenPiGeeks/raspberrypi/Projects/upload_file_python/src/referenceimages/referenceimage.jpg'

#Person takes live picture
#Guard uploads picture to AWS
filepath=input('Enter File Name')

print(filepath)    
# replace bucket, collectionId, and photo with your values.
bucket='gpgphotoboothliveimages'
collectionId='GlenPiGeeks'
    
table = dynamodb.Table('gpgphotobooth3')

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
    
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


#I want to take the Face ID that is being printed and pass it into gpgphotoboothsearchfacesincollection.py
#This way, you won't have to manually enter a new Face ID everytime you take a live picture

#Computer creates random Face ID from gpgphotoboothaddfaces.py
#Takes Face ID and underlying image and compares IDs with students through gpgphotoboothsearchfacesinimage.py
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
                str(item['ReferenceImageID'])
                s3.Bucket(bucket).download_file(item['ReferenceImageID'], referenceLookupImage)
                

    











