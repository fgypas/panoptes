from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><h1>Welcome to the development server of vzflow</h1></html>'
