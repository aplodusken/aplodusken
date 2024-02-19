# Sell movie ticket free up till 3 between 3-12 $10 over 13 and up $15
active = True
while active:
    msg = input("What is your age? ")

    if msg.isdigit():
        msg = int(msg)
        if msg < 3:
           print("Your ticket i s free.")
        elif msg > 12:
            print("Your ticket cost $15")
        else:
            print("Your ticket cost $10")
    else:
        if msg == "quit":
            print("Ending program, bye!")
            break
        else:
            print("Didn't get that, try again.")