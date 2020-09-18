import pandas as pd

from .lib import model, webhook, store

def apply(input):
    csv_file_path = input['csv_file_path']
    user_id = input['user_id']
    webhook_url = input['webhook_url']

    csv_data = store.load_csv_file(csv_file_path)
    dataset = pd.read_csv(csv_data).dropna()

    X = dataset['description']
    y = dataset['target_category']

    pipeline = model.fit(X, y)

    pipeline_id = store.save_pipeline(pipeline.named_steps)

    webhook.notify(webhook_url, user_id, pipeline_id)

import json

if __name__ == '__main__':
    input = '{"foo":"bar"}'
    print(apply(json.loads(input)))
