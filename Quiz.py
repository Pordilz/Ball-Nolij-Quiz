from art import *
import random

tprint("BOL NOLIJ QUIZ")
print(text2art("W e l c o m e  T o  B O L  N O L I J  Q U I Z ","white_bubble")) 
print("This is the Ultimate test of Football Knowledge...")
name = input("What is your name? ")
difficulty = input("What difficulty do you want to play? [ Farmers | FT | Elite ]")

class Player:
    def __init__(self,name = name,score = 0,Difficulty = difficulty):
        self.name = name
        self.score = score
        self.Difficulty = Difficulty
        
def get_random_question(start_num):
# Set the range of numbers
    end_num = 80  # set the end number to 1 more than the max you want to allow (e.g. 101 instead of 100)

# Generate a random number from the set
    random_num = random.randint(start_num, end_num)

# Convert the random number to a number in the set (incremented by 4)
    random_num = ((random_num - 1) // 4) * 4 + 1

    return(random_num)


def get_question():
    # Open the file in read mode and read all lines into a list
    with open('Difficult Questions.txt', 'r') as f:
        lines = f.readlines()

# Define the line number you want to retrieve
    line_number = get_random_question(1)

# Get the desired line from the list of lines
    question = lines[line_number-1]
    answers = lines[line_number].strip().split(',')
    print(question)
    print(answers)
# Do something with the line, for example print it
get_question()


