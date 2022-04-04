from flask import Flask, render_template, request, Response
from Domain import ClientController
import json
import xlrd


app = Flask(__name__)

controller = ClientController.Controller()

@app.route('/index')
def index():
    print("does it print?")
    return render_template('index.html')


@app.route('/postData')
def postData():
    print("i am trying to test the code")
    try:
        data = request.get_data()
        data = f"{data}".strip('b\'][')
        data = json.loads(data)

        return Response("success")
    except:
        return Response(status=400)



@app.route('/testing')
def saveData():
    return ""