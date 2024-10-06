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
        max_tokens=55,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return Question.choices[0].message

role = "Your role is to create one meaningful question based on the topics that a user would choose. you will create one question that has 4 possible answers with only one of them being the correct one. An example of how you will respond is the following: Question: What is the time complexity of searching for an element in a binary search tree (BST)?\nA) O(1)\nB) O(log n)\nC) O(n)\nD) O(n^2)\nCorrect Answer: O(log n)"
message = "C++ data structures and algorithms?"

example_question = "Question: What is the time complexity of searching for an element in a binary search tree (BST)?\nA) O(1)\nB) O(log n)\nC) O(n)\nD) O(n^2) \nCorrect Answer: O(log n)"

def parse():
    # question = getQuestion(role,message)
    question = example_question
    content = question.split("\n")
    question = content[0][10:]
    answer1 = content[1][3:]
    answer2 = content[2][3:]
    answer3 = content[3][3:]
    answer4 = content[4][3:]
    correct = content[5][16:]
    # db.add_question(questions=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correct=correct)


