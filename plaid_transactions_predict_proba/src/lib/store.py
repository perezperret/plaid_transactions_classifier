import pickle

from sklearn.pipeline import Pipeline

import Algorithmia

client = Algorithmia.client()
base_path = "data://pocketpatch/pipelines"
steps = ["count_vect", "tfidf_transformer", "clf"]

def load_pipeline(pipeline_id):
    pipeline_path = base_path + "/" + pipeline_id
    named_steps = []

    for model_name in steps:
        model_path = client.file(pipeline_path + "-" + model_name + ".pkl").getFile().name

        with open(model_path, "rb") as f:
            named_steps.append((model_name, pickle.load(f)))

    return Pipeline(named_steps)
