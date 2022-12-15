
import os
import openai
from transformers import BertForSequenceClassification
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")

BASE = "OPEN_AI"

prompts = "Classify the sentiment in this tweet"


def sentiment(input_list):
    filter_list = []
    for input in input_list:
        if BASE == "OPEN_AI":
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt= "Classify the sentiment in this tweet as positive, negative or neutral" + input[0],
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            if response == "positive" or response =="neutral":
                filter_list.append(input)
        elif BASE == "BERT":
            API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
            headers = {"Authorization": f"Bearer {API_TOKEN}"}
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            output = query({
                "inputs": input[0],
            })
            if output > 3:
                filter_list.append(input)
            
        else: 
            raise Exception("not support")

    return filter_list
