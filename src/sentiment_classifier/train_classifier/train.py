import argparse
from os import path

import pandas as pd
import joblib as jb

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

g_random_state = 1234

arg_parser = argparse.ArgumentParser(description='Train sentiment classifier')

arg_parser.add_argument('--data_folder', dest='data', default='data', 
help='Path to train folder')

arg_parser.add_argument('--reviews_fname', dest='reviews', default='reviews.json', 
help='File with train data. Must be json format')

arg_parser.parse_args()

# tf-idf transform
transformer = TfidfVectorizer(max_df=0.85, min_df=0.003, ngram_range=(1, 2))

# Logistic regression with elasticnet regularization
# and SGD optimizer
sgdc = SGDClassifier(random_state=g_random_state, 
max_iter=10000, tol=0.0001, class_weight='balanced', penalty='elasticnet',
alpha=0.0001, l1_ratio=0.15, loss='log')

classifier = Pipeline([
    ('tf_idf_vectorizer', transformer),
    ('SGDC', sgdc)
    ])

train_data = pd.read_json(path.join(arg_parser.data, arg_parser.reviews))
classifier.fit(train_data['review'], train_data['target'])

jb.dump(classifier, path.join(arg_parser.data, 'mobile_review_clf.dat'))