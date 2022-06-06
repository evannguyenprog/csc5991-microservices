#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
import random
app = Flask(__name__)


@app.route('/jokes/', methods=['GET', 'POST'])


def joker():
    
    num = request.args.get('num', type=int)

    jokes = [   'Which bear is the most condescending? A pan-duh!',
            'Whats brown and sticky? A stick.',
            'Two guys walked into a bar. The third guy ducked.',
            'How do you get a country girls attention? A tractor.',
            'Why are elevator jokes so classic and good? They work on many levels.'
            'What do you call a pudgy psychic? A four-chin teller.',
            'What did the police officer say to his belly-button? Youre under a vest.',
            'What do you call it when a group of apes starts a company? Monkey business.',
            'My wife asked me to stop singing "Wonderwall" to her. I said may...'
        ]


    return jsonify(jokes = random.sample(jokes, x=num))

app.run()
# def index():
#     
# app.run()
#return jsonify()