import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

# from previous steps 
input_list = []


MODEL = "text-davinci-003"
prompts_list = ["TL;DR","In conclusion", "Summarize"]
models_output = {}

#TODO: add curl url 
def summarize(input_list,fix_prompt=None):
    for prompt in prompts_list: 
        all_summary = []
        for query in input_list:
            response = openai.Completion.create(
                    model=MODEL,
                    prompt= prompt+query,
                    temperature=0.7,
                    max_tokens=60,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=1
                    )
            all_summary.append(response)
        models_output[prompt] = all_summary
    if fix_prompt:
        return  models_output[fix_prompt]

