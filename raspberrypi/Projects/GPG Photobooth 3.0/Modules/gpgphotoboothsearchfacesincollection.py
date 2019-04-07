import boto3

if __name__ == "__main__":

    # Replace collectionId and faceID with tthe values you want to use.
    collectionId='GlenPiGeeks'
    threshold = 50
    maxFaces=2
    faceId='2348700f-b301-4efe-b757-331aee8c612e'

    client=boto3.client('rekognition', 'us-east-1')

  
    response=client.search_faces(CollectionId=collectionId,
                                FaceId=faceId,
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                        
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print