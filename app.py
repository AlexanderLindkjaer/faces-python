from flask import Flask
from webcam import Webcam
app = Flask(__name__)
webcam = Webcam()


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/status')
def status():
    if webcam.running:
        return 'Running'
    else:
        return 'Not Running'



@app.route('/start')
def start():

    return 'running'








if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    webcam.runDetection()