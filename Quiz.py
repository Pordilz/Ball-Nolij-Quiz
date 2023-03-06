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
        if Difficulty == "Farmers":
            self.Difficulty = "EZ questions.txt"
        elif Difficulty == "FT":
            self.Difficulty = "Mid questions.txt"
        elif Difficulty == "Elite":
            self.Difficulty = "Difficult questions.txt"
        else:
            print("Invalid difficulty")
            
    def get_question(self):
    
    # Open the file in read mode and read all lines into a list
        difficulty = self.Difficulty
        with open(difficulty, 'r') as f:
            lines = f.readlines()

# Define the line number you want to retrieve
        while True:
            line_number = get_random_question(1)

    # Get the desired line from the list of lines
            question = lines[line_number-1]
    
    # Check if the question has already been used
            if question in Player.used_questions:
                continue
    
            Player.used_questions.append(question)
            options = lines[line_number].strip().split(',')
            answer = lines[line_number+1].strip()
            answer_letter = answer[1]
            return question,options,answer_letter

                
    
    def answer(self,answer):
        player_answer = input("Please Chose your answer: (letter only)").upper()
        if player_answer == answer.upper():
            print("\nWe cannoh replace him, More Than You can belive\n")
            self.score += 100
        else:
            print("\nThis Guyyy, On My Life He's playing Against Us\n")
            self.score -= 100
     
    def generate_result(self): 
        print("Your score is: " + str(self.score))
        if self.score >= 2000:
            print(text2art("I  T h i n k  I  w i l l  L o v e  I t ,  A n d  I  D e s e r v e  I T . . . .  S u i i i i i","white_bubble")+"\n")
            print("{name} is JOSE MOURINHO!".format(name = self.name))
        elif self.score < 2000 and self.score >= 1500:
            print(text2art("I Used to pray for times like this!!!","white_bubble")+"\n")
            print("{name} has Elite Bol Nolij!".format(name = self.name))
        elif self.score < 1500 and self.score >= 1000:
            print(text2art("Absoloute Scenes Get In Lads!!!","white_bubble")+"\n")
            print("{name} has DEEEECENT Bol Nolij!".format(name = self.name))
        elif self.score < 1000 and self.score >= 500:
            print(text2art("Job's Not Finished!!!","white_bubble")+"\n")
            print("{name} is the ball nolij equivalent of LAKAKA".format(name = self.name))
        else:
            print(text2art("Pretty One Come My Way...","white_bubble")+"\n")
            print("{name} should start watching Tom Brady and dem Man".format(name = self.name))

player1 = Player()
for i in range(20):
    q,o,a = player1.get_question()
    print("\n"+q)
    print(o)
    player1.answer(a)

player1.generate_result()



