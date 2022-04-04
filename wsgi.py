from flask import Flask, render_template, request, redirect, url_for
from Domain import ClientController
import json
from Domain import ClientController
import pandas as pd
import os


app = Flask(__name__)
controller = ClientController.Controller()
app.config['UPLOAD_FOLDER'] =  'static/files'


@app.route('/index')
def index():
    """
        renders the home page
    """
    print("does it print?")
    return render_template('index.html')


@app.route('/index',methods=['POST'])
def postData():
    """
        Captures the data from the form and deserializes it. That data is then 
    """
    print('i am working')
    
    data = f"{request.get_data()}".strip('b\'][')
    data = json.loads(data)
    controller = ClientController.Controller()
    controller.handleFile(saveFile())
    controller.setData(data)
    controller.postData()
    
    
    return redirect(url_for('graph.html'))

def saveFile():
    app.config['UPLOAD_FOLDER'] =  'static/files'
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
        return file_path