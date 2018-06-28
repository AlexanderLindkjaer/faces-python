import requests


class Api():

    def __init__(self):
        self.loadFaces()

    def loadFaces(self):
        r = requests.get('http://facefunadmin.test/api/faces')
        self.data = r.json()

    def getData(self):
        return self.data


    def getRandomShout(self, face_id):
        r = requests.get('http://facefunadmin.test/api/face/'+face_id+'/shouts/random')
        return r.json()