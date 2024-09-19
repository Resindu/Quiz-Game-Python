from random import random

import requests

class Quiz:
    def __init__(self,amount=10, category=10, difficulty="easy", qtype="multiple"):
        self.API_URL = f"https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple"
        self.questions = []
        self.score = 0


    def get_questions(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            data = response.json()
            self.questions = data['results']
        else:
            print(f"Error: {response.status_code}")

    def load_quiz(self):
        if self.questions:
            for index,question in enumerate(self.questions):
                print(f"\nQuestion {index+1}: {question['question']}\n")
                options = question['incorrect_answers']+ [question['correct_answer']]
             #   random.shuffle(options)

                for i,option in enumerate(options):
                    print(f"Option {i+1}: {option}")

                #get user inputs
                user_choice = int(input("\nEnter the number of your choice: "))
                correct_answer = question['correct_answer']

                #check the user input matches with the correct answer
                if options[user_choice-1] == correct_answer:
                    print(f"Correct answer")
                    self.score+=1
                else:
                    print(f"Incorrect answer")
            self.display_score()

    def display_score(self):
        print(f"Your score is {self.score}")