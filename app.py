from flask import send_file
from flask import render_template
from flask import Flask
from flask import request

from api_requests import respond
from blueprints.index_bp import index_bp
from firebaseConnector import Firebase

app = Flask(__name__)

# app.config["SERVER_NAME"] = "mango.test"
app.config['SERVER_NAME'] = 'mango-friends.com'
# fireBase = Firebase(user_create_mode='users-test')
fireBase = Firebase()


@app.route("/static/<path:path>", subdomain="www")
def static_dir(path):
    return send_file("static/"+path)


@app.route("/", methods=['POST', 'GET'], subdomain='www')
def main():
    return render_template("index.html")


@app.route("/feature", subdomain="www")
def features():
    return render_template("feature.html")


@app.route("/services", subdomain="www")
def services():
    return render_template("services.html")


@app.route("/pricing", subdomain="www")
def pricing():
    return render_template("pricing.html")


@app.route("/blog", subdomain="www")
def blog():
    return render_template("blog.html")


@app.route("/single-blog", subdomain="www")
def single_blog():
    return render_template("single-blog.html")


@app.route("/elements", subdomain="www")
def elements():
    return render_template("elements.html")


@app.route("/contact", subdomain="www")
def contact():
    return render_template("contact.html")


@app.route("/contact_process.php", methods=['POST'])
def contact_process():
    if request.method == 'POST':
        return


@app.route("/", subdomain="api", methods=['POST', 'GET'])
def api_process():
    if request.method == 'POST':
        return respond(request, fireBase)

    elif request.method == 'GET':
        print("SDSDSD")
        return render_template("api.html")


if __name__ == "__main__":
    app.run()
