#!/usr/bin/env python3

toContinue = "Y"

while toContinue == "Y":
    askQ1 = input("Are you a Horse? (Y/N/M(aybe)) ").upper()
    # test logic with the `if` statement
    if askQ1 in ["Y", "M"]:
        askQ2 = input("How many legs do you walk on? 2 0r 4 ")
        while askQ2.isdigit() != True:
            print("Wrong input, try again")
            askQ2 = input("How many legs do you walk on? 2 or 4 ")
        askQ2 = int(askQ2)
        if askQ2 == 2:
            print("You are not a Hhorse")
        elif askQ2 == 4:
            askQ3 = input("Can you READ or WRITE? (Y/N) ")
            if askQ3 == "Y":
                print("You are not a Horse")
            else:
                print("Liar you are reading this and not a horse")
        else:
            print("You are not a Hourse")
    else:
        print("You are not a Horse")
    toContinue = input("Do you want to continue (Y / N)?").upper()
