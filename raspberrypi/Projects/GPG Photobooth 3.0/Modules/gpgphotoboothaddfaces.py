#gpgphotoboothaddfaces.py
import boto3
dynamodb = boto3.client('dynamodb', "us-west-2")
s3 = boto3.client('s3', 'us-east-1')

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
	
if __name__ == "__main__":
    
    filename=input('Enter File Name')
    firstname=input('Enter First Name')
    lastname=input('Enter Last Name')
    
    # replace bucket, collectionId, and photo with your values.
    bucket='gpgphotobooth30'
    collectionId='GlenPiGeeks'
    
    client=boto3.client('rekognition', 'us-east-1')

    #For live faces
    response=client.index_faces(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':filename}},
                                #ExternalImageId=filename,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    print ('Results for ' + filename) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
         update_index('gpgphotobooth3',filename, faceRecord['Face']['FaceId'], firstname, lastname)


    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)

