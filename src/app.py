from .sentiment_classifier.classifier_wrapper import SentimentClassifier
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
classifier = SentimentClassifier()

@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['text']
    result, prediction = classifier.get_prediction_message(text)

    return jsonify({
        'status' : result,
        'class' : prediction
    })

@app.route('/')
def index_page():
    return render_template('index.html')
