import pickle
import uuid

import Algorithmia

client = Algorithmia.client()
base_path = 'data://pocketpatch'
pipelines_path = base_path + "/pipelines"
datasets_path = base_path + "/datasets"

def save_pipeline(pipeline_steps):
    pipeline_id = uuid.uuid4().hex
    pipeline_path = pipelines_path + "/" + pipeline_id

    for model_name, model in pipeline_steps.items():
        tmp_path = model_name + ".pkl"

        pickle.dump(model, open(tmp_path, "wb"))
        client.file(pipeline_path + "-" + model_name + ".pkl").putFile(tmp_path)

    return pipeline_id

def load_csv_file(file_path):
    source_path = client.file(datasets_path + "/" + file_path).getFile().name

    return open(source_path, "rb")
