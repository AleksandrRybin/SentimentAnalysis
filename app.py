from sentiment_classifier import SentimentClassifier
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
classifier = SentimentClassifier('mobile_review_clf.dat')

@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['text']
    result, prediction = classifier.get_prediction_message(text)

    return jsonify({
        'status' : result,
        'message' : prediction
    })

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
