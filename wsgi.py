from flask import Flask, render_template, request, redirect, url_for
from Domain import ClientController
import json
from Domain import ClientController
import pandas as pd
import os


app = Flask(__name__)
app.config["DEBUG"] = True
controller = ClientController.Controller()
app.config['UPLOAD_FOLDER'] =  'static/files'


@app.route('/')
def index():
    """
        renders the home page
    """
    return render_template('index.html')


@app.route('/postData', methods=["POST"])
def postData():
    """
        Captures the data from the form and deserializes it.
    """
    data = request.get_data()
    data = f"{data}".strip('b\'][')
    data = data.split("&")
    controller = ClientController.Controller()
    controller.setData(data)
    controller.postData()
    # controller.handleFile(saveFile())
    
    
    return "redirect(url_for('graph.html'))"

def saveFile():
    app.config['UPLOAD_FOLDER'] =  'static/files'
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
        return file_path


if (__name__ == "__main__"):
     app.run(port = 8080)