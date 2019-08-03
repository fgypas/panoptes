from flask import Flask, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder=".")
app.config["MONGO_URI"] = "mongodb://localhost:27017/vzflow"
mongo = PyMongo(app, connect=True)

@app.route('/')
def index():
    db_info = mongo.db
    return f"<html> \
             <h1>Welcome to the development server of vzflow. </h1> <br> \
             If you can see this message then your DB is set properly <br> \
             DB info: {db_info}. <br> \
             To check the status of the workflow go to the following route: <a href=\"/workflow_status\">/workflow_status</a> <br> \
             </html>"

@app.route('/workflow_status', methods=['GET', 'POST'])
def get_status():
    try:
        doc = db.vzflow.status.getOne()
        return str(doc)
    except:
        return f"<html>No workflow currently running!!!</html>"

@app.route('/update_workflow_status', methods=['POST', 'GET'])
def update_status():
    status = request.form["status"]

    doc = mongo.db.vzflow.insert({"status": status})

    print(doc)

    return "asd"


