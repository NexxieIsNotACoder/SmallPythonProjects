# Write your code here :-)
import time

def getHour():
    #fetch the time from the user
    clock = time.localtime(time.time())
    return clock[3]
def findIfSunStillUp(time):
    if time > 19: #i should not hard code this, but this is around the time where the sun would already be set.
        return False
    else:
        return True

#if the function calculates that the sun has been set
if findIfSunStillUp(getHour()) == False:
    print("sun has been set, amigo")
    print("it's been " + str(getHour()) + " hours since the day started.")
else:
    print("you still got time brodie")
    print("it's been " + str(getHour()) + " hours since the day started.")
