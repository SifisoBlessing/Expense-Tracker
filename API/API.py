from flask import Flask, render_template, request, redirect
from API.Domain import ClientController
import json
import os

app = Flask(__name__)
controller = ClientController.Controller()


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


@app.route('/postData', methods=["POST"])
def postData():
    """
        Captures the data from the form and deserializes it.
    """
    data = request.get_data()
    data = f"{data}".strip('b\'][')
    data = data.split("&")
    controller.setData(data)

    #loads the user data from the dataBase if the user already exists
    #redirects to the expenseFile view to prompt the user to insert new data

    if controller.validateData():
        data = controller.getFileData()
        return render_template("graph.html",
            income_vs_expenses = json.dumps([data[0],data[1]]),
            dates_label = json.dumps(data[2]),
            income = json.dumps(data[3]),
            expense = json.dumps(data[4])
        )
    else:
        return redirect("/expenseFile")


@app.route('/saveFile', methods=["POST"])
def saveFile():
    """
        gets the file from user and saves it
    """
    render_template("expenseFile.html")
    try:
        uploaded_file = request.files['Efile']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            file_path = f"{file_path}".replace('\\','/')
            uploaded_file.save(file_path)
            data = controller.handleFile(file_path)
            return render_template("graph.html",
                income_vs_expenses = json.dumps([data[0],data[1]]),
                dates_label = json.dumps(data[2]),
                income = json.dumps(data[3]),
                expense = json.dumps(data[4])
                )   
    except:
        return redirect("/error")

@app.route('/error')
def errorPage():
    return render_template("error.html")
