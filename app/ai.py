import os
import openai
from passwords import api_key

import db

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
        temperature=.8, #the randomness/ unpredictablitiy of the question
        max_tokens=450,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return Question.choices[0].message.content

role = "Your role is to create five meaningful questions based on the topics that a user would choose. you will create five question that each have 4 possible answers with only one of them being the correct one. Separate each question with two newline characters, \n. Strictly follow this format, filling in the square brackets with your generated questions and answers: Question: [question]?\nA) [answer]\nB) [answer]\nC) [answer]\nD) [answer]\nCorrect Answer: Letter answer choice. Make sure the answer you give is only the letter choice, and nothing but the letter choice. So if the answer corresponds to choice A, then the answer is A."
current_message = "C++ data structures and algorithms?"
accepted = ["C++ data structures and algorithms?", "Environment?", "Linear Algebra?", "Psychology?"]
example_question = "Question: What is the time complexity of searching for an element in a binary search tree (BST)?\nA) O(1)\nB) O(log n)\nC) O(n)\nD) O(n^2) \nCorrect Answer: O(log n)"

def parse_question(question_content, message): 
        content = question_content.split("\n")
        question = content[0].lstrip('Question:').lstrip()
        answer1 = content[1].lstrip('A)').lstrip()
        answer2 = content[2].lstrip('B)').lstrip()
        answer3 = content[3].lstrip('C)').lstrip()
        answer4 = content[4].lstrip('D)').lstrip()
        correct = content[5].split(' ')[2]
        if (correct=='A'):
            correct = ''+answer1
        elif(correct=="B"):
            correct = ''+answer2
        elif(correct=="C"):
            correct = ''+answer3
        elif(correct=="D"):
            correct = ''+answer4

        if(message=="C++ data structures and algorithms?"):
            db.add_data_question(questions=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correct=correct)
        elif(message=="Environment?"):
            db.add_env_question(questions=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correct=correct)
        elif(message=="Linear Algebra?"):
            db.add_linearalg_question(questions=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correct=correct)
        elif(message=="Psychology?"):
            db.add_psych_question(questions=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correct=correct)

def parse(message):
    if message not in accepted:
        raise Exception("Currently not accepting this topic. Please try one of our four provided topics.")

    else:
        question_query = getQuestion(role,message)
        # question = example_question
        content = question_query.split("\n\n")
        for question in content:
            parse_question(question, message)

# parse("C++ data structures and algorithms?")