# server.py

from flask import Flask, jsonify, request, json

app = Flask(__name__)

IVs = [
    {
        'url': 'www.google.de',
        'topics': ['suche', 'suchmaschine', 'google'],
        'preview': 'image_url',
        'description': 'Google is a search engine',
        'type':'none'
    },
    {
        'url': 'www.test.de',
        'topics': ['test', 'website'],
        'preview': 'image_url',
        'description': 'This is a website for test purposes',
        'type':'IV'
    }
]
def get_data():
    f = open('data\\json\\ToAnalyze2.json', 'r')
    data = json.load(f)
    return data

@app.route('/search', methods=['GET'])
def get_tasks():
    if request.method == 'GET':
        args = request.args
        search_query=args.get("search_query") # =abc, wenn /search?search_query=abc 
        #return search_query
        return jsonify(get_data())

if __name__ == '__main__':
    app.run(debug=True)