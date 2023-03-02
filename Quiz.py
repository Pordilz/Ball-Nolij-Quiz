from art import *
import random

tprint("BOL NOLIJ QUIZ")
print(text2art("W e l c o m e  T o  B O L  N O L I J  Q U I Z ","white_bubble")) 
print("This is the Ultimate test of Football Knowledge...")
name = input("What is your name? ")
difficulty = input("What difficulty do you want to play? [ Farmers | FT | Elite ]")

def get_random_question(start_num):
# Set the range of numbers
    end_num = 80  # set the end number to 1 more than the max you want to allow (e.g. 101 instead of 100)

# Generate a random number from the set
    random_num = random.randint(start_num, end_num)

# Convert the random number to a number in the set (incremented by 4)
    random_num = ((random_num - 1) // 4) * 4 + 1

    return(random_num)

class Player:
    used_questions = []
    def __init__(self,name = name,score = 0,Difficulty = difficulty):
        self.name = name
        self.score = score
        if difficulty == "Farmers":
            self.Difficulty = "EZ questions.txt"
        elif difficulty == "FT":
            self.Difficulty = "Mid questions.txt"
        elif difficulty == "Elite":
            self.Difficulty = "Elite questions.txt"
        else:
            print("Invalid difficulty")
            
    def get_question(self,difficulty,used_questions = used_questions):
    # Open the file in read mode and read all lines into a list
        with open(difficulty, 'r') as f:
            lines = f.readlines()

# Define the line number you want to retrieve
        while True:
            line_number = get_random_question(1)

    # Get the desired line from the list of lines
            question = lines[line_number-1]
    
    # Check if the question has already been used
            if question in used_questions:
                continue
    
            used_questions.append(question)
            options = lines[line_number].strip().split(',')
            answer = lines[line_number+1].strip()
            print(question)
            print(options)
            return answer

                
    
    def answer(self):
        player_answer = input("Please Chose your answer:")
        answer = Player.get_question(self.Difficulty)
        if player_answer == answer:
            print("Correct!")
            self.score += 100
        else:
            print("Wrong!")
            self.score -= 100
          







