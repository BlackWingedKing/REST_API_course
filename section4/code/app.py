from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

# no need to do jsonify in flask restful

class Item(Resource):
    """
    docstring
    """
    def get(self, name):
        for item in items:
            if(item['name'] == name):
                return item
        return {'item': None}, 404
            
    
    def post(self, name):
        data = request.get_json()
        # if request doesn't have a proper json or a type header the above
        # line gives an error. force=True will format it to json without checking the header.
        # silent=True returns None instead of giving the error
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 

class ItemList(Resource):
    """
    docstring
    """
    def get(self):
        return {'item': items}
    

api.add_resource(Item, '/item/<string:name>')

app.run(port=8000, debug=True)

