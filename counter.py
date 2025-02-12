# Write your code here :-)
import time

def countdown(number):
    count = number
    limit = 0
    while True:
        print(f"We got {count}")
        # if count is above 0, decrement count by 1 and add a pause by 0.1 seconds
        if count > 0:
            count -= 1
            time.sleep(0.1)
        # checks if the process has been repeated more than three times
        elif limit < 3:
            count = number
            print("wanna see me do that again?")
            limit += 1
            time.sleep(2)
        # stops the program after the limit goes over 3
        else:
            print("ok man, that's it, i'm tired.")
            break

initialNum = int(input("so what's your number? "))
countdown(initialNum)
