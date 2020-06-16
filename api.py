from flask import Flask, render_template, redirect, url_for, request, jsonify, Response
from werkzeug.utils import secure_filename
from pathlib import Path
import json
import os
import requests
import time
app = Flask(__name__)


@app.route('/')
def indexPage():
    return render_template('index.html')


@app.route('/upload')
def uploadPage():
    return render_template('upload.html')


@app.route('/data',  methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        fname = str(time.time()) + f.filename
        f.save(secure_filename(fname))
        size = Path(fname).stat().st_size
        if size < 1000000:
            status = sendTOAWS(fname)
            os.remove(fname)
            return render_template('submitted.html', msg="File verified by backend and successfully submitted with status code " + str(status))
        else:
            os.remove(fname)
            return render_template('submitted.html', msg="File size too big to handle")


def sendTOAWS(file):
    url = "https://patw1h5276.execute-api.eu-west-1.amazonaws.com/beta/upload"
    files = {'upload_file': open(file, 'rb')}
    headers = {
        'content-type': "application/json"
    }
    response = requests.request("POST", url, files=files, headers=headers)
    return(response.status_code)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
