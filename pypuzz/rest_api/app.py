import json
from flask import Flask, request, render_template, Response
from flask_restful import Api, Resource, reqparse
from pypuzz.anagrams import Anagrams
from pypuzz.resources import WordList
from pypuzz.resources import MODERATE_VOCAB_1500

app = Flask(__name__)
api = Api(app)

class Anagrams_Api(Resource):

    def get(self):
        length = int(request.args.get("length"))
        if not length:
            length = 7
        word_list = WordList(MODERATE_VOCAB_1500)
        word = word_list.get_random_word(length)
        anagrams = Anagrams()
        scrambled = anagrams.scramble(word)
        result = {"word": word, "scrambled": scrambled}
        r = Response(response=render_template('anagram.html',word=word,scrambled=scrambled), status=200, mimetype="application/html")
        r.headers["Content-Type"] = "text/html; charset=utf-8"
        return r

api.add_resource(Anagrams_Api,"/anagrams")

app.run(debug=True)