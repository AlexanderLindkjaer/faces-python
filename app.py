from flask import  Flask, jsonify, request, redirect, send_file
from flask_cors import CORS, cross_origin
from webcam import Webcam
from io import BytesIO
from PIL import Image
import base64
import re




app = Flask(__name__)
webcam = Webcam()


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route("/")
@cross_origin()
def hello():
    return "Hello World!"


@app.route('/status')
@cross_origin()
def status():
    if webcam.running:
        return 'Running'
    else:
        return 'Not Running'



@app.route('/start')
@cross_origin()
def start():

    return 'running'

@app.route('/pic', methods=['GET', 'POST'])
@cross_origin()
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':

        if 'file' not in request.files:
            if request.form['file']:

                image_data = re.sub('^data:image/.+;base64,', '', request.form['file'])
                file = Image.open(BytesIO(base64.b64decode(image_data)))

            else:
                 return 'No file'

        else:

            file = request.files['file']
            file = Image.open(BytesIO(file.stream.read()))

        print(file)

        if file:
            # The image file seems valid! Detect faces and return the result.

            result = webcam.detect_faces_in_image(file)
            return serve_pil_image(result)

    # If no valid image file was uploaded, show the file upload form:
    return 'no valid image'



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def serve_pil_image(pil_img):
    #img_io = BytesIO()
    #pil_img.save(img_io, 'PNG', quality=70)
    #img_io.seek(0)
    #return send_file(img_io, mimetype='image/png')
    buffered = BytesIO()
    pil_img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

if __name__ == '__main__':
    app.run(debug=True)
