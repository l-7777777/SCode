import os
from flask import Flask, jsonify, request, render_template
nameVar = ""
orgnameVar = ""
orgidVar = ""
bundleidVar = ""
app = Flask(__name__)


@app.route('/launch', methods=['POST'])
def post():
    if request.method == 'POST':
        os.system("python3 " + request.get_data(as_text=True))
        return 'OK', 200


@app.route('/kill', methods=['POST'])
def kill():
    if request.method == 'POST':
        os.system("pkill -f " + request.get_data(as_text=True))
        return 'OK', 200


@app.route('/quit', methods=['POST'])
def quit():
    if request.method == 'POST':
        os.system("killall python3 && killall flask")
        return 'OK', 200


@app.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        global nameVar
        global orgnameVar
        global orgidVar
        global bundleidVar
        nameVar = request.get_data(as_text=True).split(",")[0]
        orgnameVar = request.get_data(as_text=True).split(",")[1]
        orgidVar = request.get_data(as_text=True).split(",")[2]
        bundleidVar = request.get_data(as_text=True).split(",")[3]
        return 'OK', 200