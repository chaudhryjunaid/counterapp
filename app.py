from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


counter = 0

@app.route("/")
def index():
    return f'{counter}'

@app.route("/inc")
def inc():
    global counter
    counter += 1
    return f'{counter}'

@app.route("/dec")
def dec():
    global counter
    counter -= 1
    return f'{counter}'


app.run(debug=True)

