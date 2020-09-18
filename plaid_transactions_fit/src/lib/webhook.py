import requests

def notify(webhook_url, user_id, pipeline_id):
    data = { 'user_id': user_id, 'pipeline_id': pipeline_id }
    requests.post(webhook_url, data = data)
