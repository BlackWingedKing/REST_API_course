from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# api works with resouces and every resource must be a class

class Student(Resource):
    """
    docstring
    """
    def get(self, name):
        return {'student': name}
a
api.add_resource(Student, '/student/<string:name>')

app.run(port=8000)

