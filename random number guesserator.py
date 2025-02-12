# Write your code here :-)
import random

correctNum = random.randint(0,100) # creates a random number between 0 and 100 to guess
print(correctNum) # CHEAT CODE
chances = 5
def askUser():
    userAnswer = int(input('What number am I thinking of between 0 and 100? ')) # asks user for their guess
    if userAnswer > 100 or userAnswer < 0:
        print('Did you even read the directions?')
        askUser() # reruns the function again
    return userAnswer # returns the value of user's answer
def compare(userAnswer, chances):
    if userAnswer != correctNum: # compares if user's guess is accurate to random number
        print('Wrong!')
        if chances == 1:
            print('You lose!')
            exit(2) # ran out of chances
        return False
    else:
        print('Congratulations! You won!')
        if chances == 2:
            print('CLUTCH!')
        return True
while True:
    if compare(askUser(), chances) == True:
        break
    else:
        chances -= 1 # deincrements chances if the compare function returns false
        print('You have ' + str(chances) + ' more chances.')
exit(1) # if the program gets out of the while True loop then that means the user got the right number

