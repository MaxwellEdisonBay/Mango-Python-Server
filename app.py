from flask import send_file
from flask import render_template
from flask import Flask
from flask import request
from flask_restful import Api, Resource
from blueprints.index_bp import index_bp
from consts import ErrorCode

app = Flask(__name__)
api = Api(app)

app.config["SERVER_NAME"] = "mango.test:5000"
# app.config['SERVER_NAME'] = 'mango-friends.com'


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


class TestAPI(Resource):
    def get(self, name, age):
        return {"data": f"Hi, your name is {name} and age is {age}"}

    def post(self):
        return {"data": "Posted"}


@app.route("/contact_process.php", methods=['POST'])
def contact_process():
    if request.method == 'POST':
        return


@app.route("/", subdomain="api", methods=['POST', 'GET'])
def api_process():
    if request.method == 'POST':
        res = {'data':'test'}
        print(request.headers)
        headers = request.headers
        if headers['Request-Type']=="test":
            return res, ErrorCode.OK
        else:
            return res, ErrorCode.FORBIDDEN
    elif request.method == 'GET':
        print("SDSDSD")
        return render_template("api.html")


api.add_resource(TestAPI, "/testapi/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run()
