import face_recognition
import requests
from io import BytesIO
from api import Api
from PIL import Image
import numpy as np

class Faces:

    def __init__(self):
        self.load()


    def load(self):

        print('LOADING FACES')
        api = Api()

        known_face_encodings = []
        known_face_names = []


        for face in api.data['faces']:

            print('face:')
            print(face)

            response = requests.get(face['image'])

            img = Image.open(BytesIO(response.content))

            face_image = np.array(img)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            known_face_encodings.append(face_encoding)
            known_face_names.append(face)

            img.close()



        # Create arrays of known face encodings and their names
        self.known_face_encodings = known_face_encodings
        self.known_face_names = known_face_names



    def getKnownFaceEncodings(self):
        return self.known_face_encodings

    def getKnownFaceNames(self):
        return self.known_face_names


#x = Faces()