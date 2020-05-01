from flask import Flask
from predict import Predicter
from flask import request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sentiment')
def sentiment_analysis():
    sentence = request.args.get('sentence')
    pr = Predicter()
    return str(pr.predict_sentiment(sentence))

    