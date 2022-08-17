# server.py

from flask import Flask, jsonify, request, json
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
#import logging
#logging.basicConfig(filename='error.log',level=logging.DEBUG)

# returns the filtered json data
def get_data(string):
    f = open('data\\json\\ToEvaluate.json', 'r')
    data = json.load(f)
    if string:
        help=[]
        for i in data:
            if string in i["topics"] or re.search(rf"{string}", i["url"]):#or re.search(rf"{string}", i["microlink"]["data"]["description"])
                help.append(i)
        return help
    return data

@app.route('/search', methods=['GET'])
def get_tasks():
    if request.method == 'GET':
        args = request.args
        search_query=args.get("search_query") # =birds, wenn /search?search_query=birds 
        return jsonify(get_data(search_query))

if __name__ == '__main__':
    app.run(debug=True)