import boto3
import json
bucket='gpgphotobooth3'
collectionId='GlenPiGeeks'
key ='Guru Rao'
photo = 'Guru'

s3 = boto3.resource('s3')
my_bucket = s3.Bucket(bucket)
    
client=boto3.client('rekognition', 'us-east-1')

for object in my_bucket.objects.all():
        print(object.key)
        image1={'S3Object':{'Bucket':bucket, 'Name':key}}
        print(image1)
        ifresponse=client.index_faces(CollectionId=collectionId,
                                Image=image1,
                                ExternalImageId='Guru',
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
        print ('Results for ' + photo) 	
        print('Faces indexed:')						
        for faceRecord in ifresponse['FaceRecords']:
             print('  Face ID: ' + faceRecord['Face']['FaceId'])
             print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
        print('Faces not indexed:')
        for unindexedFace in ifresponse['UnindexedFaces']:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)
        dfresponse = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':key}},Attributes=['ALL'])
        print('Detected faces for ' + photo)    
        for faceDetail in dfresponse['FaceDetails']:
            print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
                + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
            print('Here are the other attributes:')
            print(json.dumps(faceDetail, indent=4, sort_keys=True))