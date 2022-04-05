from django.shortcuts import render
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


@app.route('/expenseFile')
def expensefileView():
    """
        renders the expenseFile.html page
    """
    return render_template('expenseFile.html')

    
@app.route('/graphs')
def graphsView():
    """
        renders the graph.html page
    """
    return render_template('graph.html')


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
    return redirect("/expenseFile")


@app.route('/saveFile', methods=["POST"])
def saveFile():
    """
        gets the file from user and saves it
    """
    render_template("expenseFile.html")
    app.config['UPLOAD_FOLDER'] =  'static/files'
    uploaded_file = request.files['Efile']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        file_path = f"{file_path}".replace('\\','/')
        uploaded_file.save(file_path)
        controller = ClientController.Controller()
        x,y = controller.handleFile(file_path)
        return redirect("/graphs")


if (__name__ == "__main__"): 
     app.run(port = 8080)