from sklearn.externals import joblib

class SentimentClassifier():
    def __init__(self, path):
        self.model = joblib.load(path)
        self.classes_dict = {
            0 : 'neg', 
            1 : 'pos'
        }

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