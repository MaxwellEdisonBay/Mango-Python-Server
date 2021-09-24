import flask
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/")
def main():
    return flask.render_template("index.html")


@app.route("/feature")
def features():
    return flask.render_template("feature.html")


@app.route("/services")
def services():
    return flask.render_template("services.html")


@app.route("/pricing")
def pricing():
    return flask.render_template("pricing.html")


@app.route("/blog")
def blog():
    return flask.render_template("blog.html")


@app.route("/single-blog")
def single_blog():
    return flask.render_template("single-blog.html")


@app.route("/elements")
def elements():
    return flask.render_template("elements.html")


@app.route("/contact")
def contact():
    return flask.render_template("contact.html")


class TestAPI(Resource):
    def get(self, name, age):
        return {"data": f"Hi, your name is {name} and age is {age}"}

    def post(self):
        return {"data": "Posted"}


api.add_resource(TestAPI, "/testapi/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run(debug=False)
