from .sentiment_classifier.classifier_wrapper import SentimentClassifier
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
classifier = SentimentClassifier() # классификатор

@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['text']
    result, prediction = classifier.get_prediction_message(text)

    return jsonify({
        'status' : result,   # результат 'failed' или степень уверенности классификатора
        'class' : prediction # предсказанный класс  или None в случае ошибки
    })

@app.route('/')
def index_page():
    return render_template('index.html')
