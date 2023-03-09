from flask import Flask, jsonify, request, redirect
from flask_restful import Resource, Api
import json
from urldata import *
from jsonUtils import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class shorten(Resource):
    def post(self):
        data = request.get_json()
        link = data.get('url')
        alias = data.get('alias')
        ob = urldata()
        ob.shorten(link)
        return responseOk(ob)

class home(Resource):
    def get(self, alias):
        ob = urldata()
        ob.getURL(alias)
        if not ob.originalURL:
            return jsonify({'link' : ob.originalURL})
        else:
            return redirect(ob.originalURL)
        

api.add_resource(HelloWorld, '/')
api.add_resource(shorten, '/shorten')
api.add_resource(home, '/<string:alias>')

if __name__ == '__main__':
    app.run(debug=True)