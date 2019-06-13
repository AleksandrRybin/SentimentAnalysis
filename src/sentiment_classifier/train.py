from os import path

import pandas as pd
import joblib as jb

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

transformer = TfidfVectorizer(max_df=0.85, min_df=0.003, ngram_range=(1, 2))

sgdc = SGDClassifier(random_state=1234, 
max_iter=10000, tol=0.0001, class_weight='balanced', penalty='elasticnet',
alpha=0.0001, l1_ratio=0.15, loss='log')

classifier = Pipeline([
    ('tf_idf_vectorizer', transformer),
    ('SGDC', sgdc)
    ])

train_data = pd.read_json(path.join('data', 'reviews.json'))
classifier.fit(train_data['review'], train_data['target'])

jb.dump(classifier, path.join('data', 'mobile_review_clf.dat'))