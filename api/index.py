from flask import Flask
from flask import request
# from getFaces import *
# import face_recognition
# import sys
# import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/api', methods=['POST'])
def upload_file():
    f = request.files['image']
    imgName = "/tmp/"+f.filename
    f.save(imgName)
    return "good"
