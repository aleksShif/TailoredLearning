import os
import openai
from passwords import api_key

openai.api_key = api_key

def getQuestion(role,prompt):
    Question = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""{role}"""
            },
            {
                "role": "user",
                "content": f"""{prompt}"""
            }
        ],
        temperature=.5, #the randomness/ unpredictablitiy of the question
        max_tokens=40,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return Question.choices[0].message

role = "You are a quiz question generator. You create a question with four possible answers."
message = "Can I have a question about C++ data structures and algorithms?"

print(getQuestion(role,message))

    