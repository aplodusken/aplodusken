msg = input("How many people do you want to book a table for? ")
msg = int(msg)
if msg > 7:
    print("We do not ha a table for that many at the moment, but we will have one in a few minutes.")
else:
    print("Yes, we have a table right now.")
    