from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": f"Hello World You name is {name} and age is {test}"}

    def post(self):
        return {"data": "Posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)
