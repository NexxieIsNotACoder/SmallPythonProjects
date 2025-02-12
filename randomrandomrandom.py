import random

def randomNumber():
    # generates a number between 0-100, and determines if it's above or under 50.
    return ('heads') if random.randrange(0,100) < 50 else ('tails')

print(randomNumber())
