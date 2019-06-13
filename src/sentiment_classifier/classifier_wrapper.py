import sklearn
import joblib as jb
from os import path

class SentimentClassifier():
    def __init__(self):
        this_dir, *_ = path.split(__file__)
        self.model = jb.load(path.join(this_dir, 'data', 'mobile_review_clf.dat'))
        self.classes_dict = {
            0 : 'neg', 
            1 : 'pos'
        }

    # интерпритация предсказанной вероятности
    @staticmethod
    def get_probability_words(probability):
        if probability < 0.5:
            return 'neutral or not sure'
        if probability < 0.75:
            return 'possibly'
        else:
            return 'exactly'

    def predict_text(self, text):
        try:
            return self.model.predict([text])[0],\
                   self.model.predict_proba([text])[0].max()
        except:
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)

        if prediction != None:
            class_prediction, probability_prediction = prediction

            return self.get_probability_words(probability_prediction),\
                   self.classes_dict[class_prediction]
        else:
            return 'failed', None