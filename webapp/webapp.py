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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        if 'import_options' not in request.form:
            print('No import option selected')
            return redirect(request.url)

        if 'ml_models' not in request.form:
            print('No model selected')
            return redirect(request.url)

        #Variables for request parameters:
        file = request.files['file']
        import_option = request.form['import_options']
        model_name = request.form['ml_models']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect('/uploaded')
            print('return successful')
            return redirect(url_for('uploaded', filename=filename, import_option=import_option, model_name=model_name))
    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)