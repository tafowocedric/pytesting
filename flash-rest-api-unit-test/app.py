from flask import Flask
from flask_restful import Resource, Api
import sys
import json

app = Flask(__name__)
api = Api(app)

PORT = 5000

if sys.argv.__len__() > 1:
    PORT = sys.argv[1]


class HelloWorld(Resource):
    def get(self):
        return json.dumps({"Message": "ok"})


api.add_resource(HelloWorld, "/fo")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
