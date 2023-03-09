from flask import Flask, jsonify
import mysql.connector as sql
import random, string


def generate():
    length = 6
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


class urldata:
    originalURL = None
    shortURL = None
    def __init__(self):
        self.db = sql.connect(
            host = "localhost",
            user = "linkadmin",
            password = "cuttly",
            database = "link"
        )


    def shorten(self, url):
        cursor = self.db.cursor(dictionary = True)
        shortURL = generate()

        while True:
            cursor.execute("SELECT shortURL FROM urls WHERE shortURL=%s", (shortURL,))
            row = cursor.fetchone()
            if not row:
                break
            else:
                shortURL = generate()

        cursor.execute("INSERT INTO urls VALUES(%s, %s)", (url, shortURL,))
        self.db.commit()
        self.shortURL = shortURL
        self.originalURL = url


    def getURL(self, alias):
        cursor = self.db.cursor(dictionary = True)
        cursor.execute("SELECT originalURL from urls WHERE shortURL=%s", (alias,))
        row = cursor.fetchone()
        if not row:
            self.originalURL = None
        else:
            originalURL = row['originalURL']
            self.originalURL = originalURL
            self.shortURL = alias