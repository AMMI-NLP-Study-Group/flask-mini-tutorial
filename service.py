from flask import Flask
from flask import jsonify
from flask import request,render_template
import json as json
from flask_cors import CORS, cross_origin
from predict import Predicter

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
pred = Predicter()

@app.route('/sentiment',methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def sentiment():
    if request.method =='POST':
        sentence = request.form['feedback']

        sentiment = pred.predict_sentiment(sentence)

        if sentiment > 0.5:
            feeling = 'positive '
        else:
            feeling = 'negative'

        return render_template('index.html',feedback=feeling,sentiment_value=round(sentiment,3))

    return render_template('index.html')




    