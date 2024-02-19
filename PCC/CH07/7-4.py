active = True
while active:
    msg = input("What topping would you like on your pizza ")
    if msg == "quit":
        active = False
    else:
        print("Adding " + msg + " to your pizza")