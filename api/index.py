from flask import Flask
from flask import request
# from getFaces import *
import face_recognition
import sys
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/api', methods=['POST'])
def upload_file():
    f = request.files['image']
    imgName = "/tmp/"+f.filename
    f.save(imgName)
    # faces = getFaces(f.filename)
    # detect the faces from the images
    image = face_recognition.load_image_file(imgName)

    face_locations = face_recognition.face_locations(image)
    # encode the 128-dimension face encoding for each face in the image

    counter = 1
    faceLocs = []

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        height = len(image)
        width = len(image[0])

        # print(int((right - left) / 5))
        div = 1.3
        newtop = top - int((bottom - top) / div)
        newleft = left - int((right - left) / div)
        newbottom = bottom + int((bottom - top) / div)
        newright = right + int((right - left) / div)
        if (newtop < 0):
            newtop = 0
        if (newleft < 0):
            newleft = 0
        if (newright > width):
            newright = width
        if (newbottom > height):
            newbottom = height

        faceLocs.append({"wide": [newtop, newright, newbottom, newleft, ], "org": [
                        top, right, bottom, left]})

    face_encodings = face_recognition.face_encodings(image, face_locations)

    # print(face_locations)
    response = {"status": True, "faces": [], "locations": faceLocs}

    for face_encoding in face_encodings:
        response["faces"].append(face_encoding.tolist())

    if (len(response["faces"]) > 0):
        # print(json.dumps(response))
        # print("My program took", time.time() - start_time, "to run")
        # sys.stdout.flush()
        # exit()
        return json.dumps(response)

    response = {"status": False}
    # print(json.dumps(response))
    # print("My program took", time.time() - start_time, "to run")
    # sys.stdout.flush()
    return json.dumps(response)
