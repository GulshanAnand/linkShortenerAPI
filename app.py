# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, redirect
import mysql.connector as sql

db = sql.connect(
  host = "localhost",
  user = "linkadmin",
  password = "cuttly",
  database = "link"
)

  
# creating a Flask app
app = Flask(__name__)

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

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
        
@app.route('/shorten/<string:link>')
def shorten(link):
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT MAX(shortURL) as shortURL FROM urls")
    row = cursor.fetchone()
    shortURL = row['shortURL']
    shortURL = nextWord(shortURL)
    cursor.execute("INSERT INTO urls VALUES(%s, %s)", (link, shortURL,))
    db.commit()
    return jsonify({'status':shortURL})

@app.route('/test')
def test():
    murl = request.args.get('link')
    code = request.args.get('code')
    return jsonify({'data': murl, 'code': code})

# driver function
if __name__ == '__main__':
    app.run(debug = True)
