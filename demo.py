__author__ = 'Aleksandr Rybin'

from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request

app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print(time.time() - start_time, " seconds")

@app.route("/sentiment-demo", methods=["POST"])
def prediction():
    text = request.form["text"]
    
    logfile = open("sentiment_demo_logs.txt", "a", "utf-8")
    print(text)
    print("<response>", file=logfile)
    print(text, file=logfile)
    prediction_message = classifier.get_prediction_message(text)
    print(prediction_message)
    print(prediction_message, file=logfile)
    print("</response>", file=logfile)
    logfile.close()

    return render_template('form.html', text=text, prediction_message=prediction_message)

@app.route("/")
def index_page():
    return render_template('form.html', text="Введите отзыв", prediction_message="")

if __name__ == "__main__":
    app.run()
