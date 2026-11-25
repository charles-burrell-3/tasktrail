from flask import Flask, redirect, url_for, jsonify, request, abort, render_template, flash

from tasktrail.sample_data import PROJECTS

app = Flask(__name__)
app.config["APP_NAME"] = "TaskTrail"
app.config["SECRET_KEY"] = "dev-only-not-a-real-secret"


def main() -> None:
    print("Hello from tasktrail!")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/flash-demo")
def flash_demo():
    flash("This is a success message!", "success")
    flash("And this one is a warning.", "warning")
    return redirect(url_for("project_list"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def project_list():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    for project in PROJECTS:
        if project["id"] == project_id:
            return render_template("project_detail.html", project=project)
    abort(404)


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


@app.route("/test_500")
def test_500():
    return 1/0


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500