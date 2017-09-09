import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import *
from flask import render_template

app = Flask(__name__)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import time


###########################
#socket io:
###########################
'''
import socketio
import eventlet
import eventlet.wsgi
sio = socketio.Server()

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('chat message', namespace='/chat')
def message(sid, data):
    print("message ", data)
    sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)
'''
###########################


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        request_data = request.get_json()
        print('request_data',request_data)
        #return redirect(url_for('uploaded', filename=filename, import_option=import_option, model_name=model_name))
    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    # wrap Flask application with engineio's middleware
    #app = socketio.Middleware(sio, app)
    #app.run(port=5000, debug=True)
    # deploy as an eventlet WSGI server
    #eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
