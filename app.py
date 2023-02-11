from flask import Flask, jsonify, request, redirect
from flask_restful import Resource, Api
import mysql.connector as sql

db = sql.connect(
  host = "localhost",
  user = "linkadmin",
  password = "cuttly",
  database = "link"
)

def nextWord(s):
    if (s == " "):
        return "a"
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1
    if (i == -1):
        s = s + 'a'
    else:
        s = s.replace(s[i], chr(ord(s[i]) + 1), 1)
    return s

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class shorten(Resource):
    def get(self, link):
        cursor = db.cursor(dictionary = True)
        cursor.execute("SELECT MAX(shortURL) as shortURL FROM urls")
        row = cursor.fetchone()
        shortURL = row['shortURL']
        shortURL = nextWord(shortURL)
        cursor.execute("INSERT INTO urls VALUES(%s, %s)", (link, shortURL,))
        db.commit()
        return jsonify({'status':shortURL})

api.add_resource(HelloWorld, '/')
api.add_resource(shorten, '/shorten/<string:link>')

if __name__ == '__main__':
    app.run(debug=True)