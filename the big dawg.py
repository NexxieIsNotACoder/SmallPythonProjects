# Write your code here :-)
x = int(input("Add a number here and I'll check if it's more than 21 "))
while True:
    if x < 10:
        if x < 5:
            print("so teeny!")
            break
        print("wow that's pretty small")
        break
    if x > 10:
            if x > 15:
                print("even more bigger...")
                break
        #print("that's a little bigger now")
        #break
    if x == int(21):
        print("you stoopid")
        break
    if x > 21:
        print("oh hey it is more than 21")
        break
    if x > 50:
        print("oh jeez you over did it")
        break
    if x > 100:
        print("oh my goodness.")
        break
