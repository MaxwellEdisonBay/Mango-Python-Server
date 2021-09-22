import flask
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/")
def main():
    return flask.render_template("index.html")


class TestAPI(Resource):
    def get(self, name, age):
        return {"data": f"Hi, your name is {name} and age is {age}"}

    def post(self):
        return {"data": "Posted"}


api.add_resource(TestAPI, "/testapi/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run(debug=False)
