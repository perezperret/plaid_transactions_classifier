import pandas as pd

from .lib import store

def apply(input):
    dataset = input['dataset']
    X = pd.Series(map(lambda x : x["description"], dataset), name="description")

    pipeline = store.load_pipeline(input["pipeline_id"])
    y_proba = pipeline.predict_proba(X)

    ids = list(map(lambda x : x['id'], dataset))
    classes = list(pipeline.classes_)
    probas = list(map(lambda x : list(x), y_proba))

    return { "ids": ids, "classes": classes, "probas": probas }
