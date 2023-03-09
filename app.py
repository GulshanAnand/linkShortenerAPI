from flask import Flask, jsonify, request, redirect, render_template, make_response
from flask_restful import Resource, Api
from urldata import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class shorten(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)

    def post(self):
        link = request.form.get('url')
        alias = request.form.get('alias')
        ob = urldata()
        ob.shorten(link)
        return jsonify({'status' : ob.shortURL})

class home(Resource):
    def get(self, code):
        ob = urldata()
        ob.getURL(code)
        if not ob.originalURL:
            return jsonify({'link' : ob.originalURL})
        else:
            return redirect(ob.originalURL)
        

api.add_resource(HelloWorld, '/')
api.add_resource(shorten, '/shorten')
api.add_resource(home, '/<string:code>')

if __name__ == '__main__':
    app.run(debug=True)