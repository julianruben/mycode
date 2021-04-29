#!/usr/bin/env python3

# function to add
def callAdd(firstVal, secondVal): 
    return firstVal + secondVal

# function to subtract
def callSub(firstVal, secondVal):
    return firstVal - secondVal

# function to multiply
def callMul(firstVal, secondVal):
    return firstVal * secondVal

# function to division
def callDiv(firstVal, secondVal):
    return firstVal // secondVal

# start our main script
def main():

    # To get first value
    firstVal = input("Enter the first digit \n")
    while not firstVal.isdigit():
        print("You have not entered a valid number. \n")
        firstVal = input("Enter the first digit \n")
    firstVal = int(firstVal)

    # To get second value
    secondVal = input("Enter the second digit \n")
    while not secondVal.isdigit():
        secondVal = input("You have not entered a valid number, please enter the second digit again \n")
    secondVal = int(secondVal)
    
    # To get arithmetic operation
    arit_Opt = input("What operation you want to perform (+ or - or * or /) \n")
    
    if arit_Opt == "+":
        print(f"The answer is = {callAdd(firstVal,secondVal)}")
    elif arit_Opt == "-":
        print(f"The answer is = {callSub(firstVal,secondVal)}")   
    elif arit_Opt == "*":
        print(f"The answer is = {callMul(firstVal,secondVal)}")
    elif arit_Opt == "/":
        while secondVal == 0 or secondVal>firstVal:
            secondVal = input("You can not divide by a Zero or greater value, enter second value again \n")
            while not secondVal.isdigit():
                secondVal = input("You have not entered a valid number, please enter the second digit again \n")
            secondVal = int(secondVal)
        print(f"The answer is = {callDiv(firstVal,secondVal)}")        
# call our main function

toContinue = "Y"

while toContinue == "Y":
    main()
    toContinue = input("Do you want to continue (Y / N)?").upper()

