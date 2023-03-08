from flask import Flask, jsonify, request, redirect
from flask_restful import Resource, Api
from urldata import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class shorten(Resource):
    def get(self, link):
        ud = urldata(link)
        ud.shorten()
        return jsonify({'status' : ud.shortURL})

api.add_resource(HelloWorld, '/')
api.add_resource(shorten, '/shorten/<string:link>')

if __name__ == '__main__':
    app.run(debug=True)