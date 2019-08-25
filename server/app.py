from flask import Flask, request, render_template, abort
from server.database import init_db, db_session
import traceback
from server.models import Workflows, WorkflowMessages
from server.schema_forms import SnakemakeUpdateForm

app = Flask(__name__, template_folder=".")
init_db()


@app.route('/')
def index():

    return f"<html> \
             <h1>Welcome to the development server of vzflow. </h1> <br> \
             If you can see this message then your DB is set properly <br> \
             DB info: {Workflows.query.all()}. <br> \
             To check the status of the workflow go to the following route: <a href=\"/workflow_status\">/workflow_status</a> <br> \
             </html>"


@app.route('/workflow_status/<id>', methods=['GET'])
def get_status(id):
    try:
        workflow = Workflows.query.filter(Workflows.id == id).first()
        if workflow:
            return str(workflow.name)
        else:
            return f"<html>No workflow currently running with id= {id}!!!</html>"

    except:
        traceback.print_exc()
        return f"<html>No workflow currently running with id= {id}!!!</html>"


@app.route('/update_workflow_status', methods=['POST', 'GET'])
def update_status():
    update_form = SnakemakeUpdateForm()
    errors = update_form.validate(request.form)
    if errors:
        abort(404, str(errors))
    # now all required fields exist and are the right type
    # business requirements aren't necessarily satisfied (length, time bounds, etc)

    w = WorkflowMessages(update_form)
    db_session.add(w)
    db_session.commit()

    print('New update from snakemake {}'.format(id))

    return "ok"


if __name__ == '__main__':
    app.run()
