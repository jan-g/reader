import os
from flask import Flask, render_template, request,jsonify, request, url_for, redirect, session
import docx2txt

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():

    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
    
    if request.method == 'POST':
        text = docx2txt.process(file)
        word1 = 'relevant'
        word2 = 'matthew'
    return render_template('home.html',text=text, display=False, word1 = word1, word2=word2)

if __name__ == '__main__':
    app.run(port=5000, debug=True)