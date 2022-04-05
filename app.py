from API import API

if __name__ == "__main__":
    api = API
    api.app.config['UPLOAD_FOLDER'] =  'API/static/files'
    api.app.run(debug=True,port=8080)
