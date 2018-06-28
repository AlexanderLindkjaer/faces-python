import requests


class Api():

    def __init__(self):
        self.loadFaces()

    def loadFaces(self):
        r = requests.get('http://127.0.0.1:8000//api/faces')
        self.data = r.json()

    def getData(self):
        return self.data


    def getRandomShout(self, face_id):
        r = requests.get('http://127.0.0.1:8000//api/face/'+face_id+'/shouts/random')
        return r.json()