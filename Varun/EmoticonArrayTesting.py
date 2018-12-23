likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    detection = "faces:"
    for face in faces:
        detection = detection + '\n anger: {}'.format(likelihood_name[face.anger_likelihood])
        detection = detection + '\n joy: {}'.format(likelihood_name[face.joy_likelihood])
        detection = detection + '\n surprise: {}'.format(likelihood_name[face.surprise_likelihood])
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
