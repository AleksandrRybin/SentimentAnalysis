from flask import Flask, render_template, request, jsonify

from .classifier_wrapper import SentimentClassifier

app = Flask(__name__)
classifier = SentimentClassifier()

@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['text']
    result, prediction = classifier.get_prediction_message(text)

    return jsonify({
        'status' : result,   # 'failed' or classifier's confidence
        'class' : prediction # predicted class or None if error
    })

@app.route('/')
def index_page():
    return render_template('index.html')
