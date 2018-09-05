__author__ = 'Aleksandr Rybin'
from sklearn.externals import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./mobile_review_clf.dat")
        self.classes_dict = {0: "негативный", 1: "положительный"}

    @staticmethod
    def get_probability_words(probability):
        if probability < 0.5:
            return "отзыв нейтральный или классификатор не уверен в выборе"
        if probability < 0.75:
            return "возможно"
        else:
            return "определённо"

    def predict_text(self, text):
        try:
            return self.model.predict([text])[0],\
                   self.model.predict_proba([text])[0].max()
        except:
            print("ошибка классификации!")
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)

        if prediction != None:
            class_prediction = prediction[0]
            prediction_probability = prediction[1]
            return self.get_probability_words(prediction_probability) + " " + self.classes_dict[class_prediction]
        else:
            return "ошибка классификации!"