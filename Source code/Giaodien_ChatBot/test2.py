import requests
import json

API_URL = "https://eflowai-api-stg.epacific.net/api/v1/prediction/91108a28-3b8b-4268-b1d6-3e3a9bbe56d3"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "béo phì là gì",
})



text_value = output['text']


print(text_value)