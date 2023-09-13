from flask import Flask
from flask import request
from .getFaces import getFaces

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/api', methods=['POST'])
def upload_file():
    f = request.files['image']
    f.save("/tmp/"+f.filename)
    faces = getFaces(f.filename)
    return faces
