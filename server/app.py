from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/vzflow"
mongo = PyMongo(app)

@app.route('/')
def index():
    db_info = mongo.db
    return f"<html>\
             <h1>Welcome to the development server of vzflow. </h1> <br> \
             If you can see this message then your DB is set properly <br> \
             DB info: {db_info}. <br> \
             </html>"