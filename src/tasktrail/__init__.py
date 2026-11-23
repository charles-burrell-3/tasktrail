from flask import Flask, redirect, url_for, jsonify, request, abort

app = Flask(__name__)
app.config["APP_NAME"] = "TaskTrail"


def main() -> None:
    print("Hello from tasktrail!")


@app.route("/")
def home():
    return f"Hello from {app.config['APP_NAME']}!"


@app.route("/projects")
def project_list():
    return "All projects will go here."


@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    return f"Details for project number {project_id}."


@app.route("/projects/new", methods=["GET", "POST"])
def project_new():
    return 'A form to create a project will go here.'


@app.route("/go-to-projects")
def go_to_projects():
    return redirect(url_for("project_list"))


@app.route("/go-to-first-project")
def go_to_first_project():
    return redirect(url_for("project_detail", project_id=1))

@app.route("/echo")
def echo():
    return jsonify(request.args.to_dict())

@app.route("/teapot")
def teapot():
    return "I'm a teapot", 418

@app.route("/forbidden-fruit")
def forbidden_fruit():
    abort(404)