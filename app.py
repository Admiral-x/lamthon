from flask import Flask, request, Response,jsonify,make_response
import nltk
from newspaper import Article
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<num>')
def num(num):
    return make_response(jsonify(int(num) ** 2),200)

@app.route('/article')
def article_parse():
    nltk.data.path.append("/tmp")
    nltk.download("punkt", download_dir="/tmp")
    url = request.args.get('url')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return make_response(jsonify(article.summary),200)

# app.run(debug=True)