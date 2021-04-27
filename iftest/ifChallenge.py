#!/usr/bin/env python3

# Asking your age
toContinue = "Y"

while toContinue == "Y":
    your_Age = (input("Enter your Age to find out best breakfast: "))
    if your_Age.isdigit() == True:
        # test logic with the `if` statement
        if int(your_Age) >= 65:
            print("Your best breakfast meal is Oatmeal")
        elif int(your_Age) >= 45:
            print("Your best breakfast meal is Pancake")
        else:
            print("You are lucky to have anything for the breakfast, Enjoy!!")
    else:
        print("You have not entered the age, try again?")
    toContinue = input("Do you want to continue (Y / N)?").upper()

