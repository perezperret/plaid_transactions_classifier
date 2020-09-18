from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

steps = ["count_vect", "tfidf_transformer", "clf"]

def fit(X, y):
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    clf = SGDClassifier(loss='log')

    named_steps = list(zip(
        steps, [count_vect, tfidf_transformer, clf]
    ))

    pipeline = Pipeline(named_steps)

    pipeline.fit(X, y)

    return pipeline
