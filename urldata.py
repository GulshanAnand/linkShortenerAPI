from flask import Flask, jsonify
import mysql.connector as sql

def getNextWord(s):
    chars = list(s)
    i = len(chars) - 1
    while i >= 0 and chars[i] == 'z':
        i -= 1
    if i < 0:
        a = "a"
        for i in range(0, len(s)):
            a += 'a'
        return a
    chars[i] = chr(ord(chars[i]) + 1)
    chars[i+1:] = ['a'] * (len(chars) - i - 1)
    return ''.join(chars)

class urldata:
    def __init__(self, url):
        self.url = url
        self.db = sql.connect(
            host = "localhost",
            user = "linkadmin",
            password = "cuttly",
            database = "link"
        )

    def shorten(self):
        cursor = self.db.cursor(dictionary = True)
        cursor.execute("SELECT MAX(shortURL) as shortURL FROM urls")
        row = cursor.fetchone()
        shortURL = row['shortURL']
        shortURL = getNextWord(shortURL)
        cursor.execute("INSERT INTO urls VALUES(%s, %s)", (self.url, shortURL,))
        self.db.commit()
        self.shortURL = shortURL