from flask import Flask, render_template, request, Response
from Domain import ClientController
import json
from Domain import ClientController


app = Flask(__name__)

controller = ClientController.Controller()

@app.route('/index')
def index():
    """
        renders the home page
    """
    print("does it print?")
    return render_template('index.html')


@app.route('/postData')
def postData():
    """
        Captures the data from the form and deserializes it. That data is then 
    """
    try:
        data = request.get_data()
        data = f"{data}".strip('b\'][')
        data = json.loads(data)
        controller = ClientController.Controller()
        controller.setData(data)
        controller.postData()

        return Response("success")
    except:
        return Response(status=400)



@app.route('/testing')
def saveData():
    data = [
        ("01-01-2022",1594),
        ("02-01-2022",1594),
        ("03-01-2022",1594),
        ("04-01-2022",1594),
        ("04-01-2022",1594),
        ("05-01-2022",1594),
        ("06-01-2022",1594),
        ("07-01-2022",1594),
        ("08-01-2022",1594),

    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("graph.html",labels=labels, values=values)