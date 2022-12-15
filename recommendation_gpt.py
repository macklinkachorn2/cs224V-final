import os
import openai

prompt = "Is this article related to"
def recommmendation_gpt(filtered_list,interest):
    output= []
    for query in filtered_list:
        title = query[0]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=  prompt +interest + title ,  
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )

        if response == "yes":
            output.append(query)
    return output