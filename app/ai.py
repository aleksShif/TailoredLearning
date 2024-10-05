import os
from openai import OpenAI

def getQuestion(role,prompt):
    Question = client.chat.completions.create(
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
        max_tokes=40,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

    Role = "You are a quiz question generator. You create a question with four possible answers."
    Message = "Can I have a question about C++ data structures and algorithms?"

    print(getQuestion(Role,Message))

    