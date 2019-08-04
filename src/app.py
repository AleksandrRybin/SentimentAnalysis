# std
import logging

# Flask
from flask import Flask, render_template, request, jsonify

# locals
from .classifier_wrapper import SentimentClassifier

logging.info('creating application')
app = Flask(__name__)

logging.info('loading classifier')
classifier = SentimentClassifier()

@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['text']
    logging.info('predicting for text: %s', text)

    result, prediction = classifier.get_prediction_message(text)

    if result != 'failed':
        logging.info('success %s %s', result, prediction)
    else:
        logging.warn('failed')

    return jsonify({
        'status' : result,   # 'failed' or classifier's confidence
        'class' : prediction # predicted class or None if error
    })

@app.route('/')
def index_page():
    return render_template('index.html')
