#!/usr/bin/env python3

# create a list called icecream
icecream = ["flavors", "salty"]

# Appending the integer to icecream
icecream.append(99)
print(icecream)

#Include an input asking for the user name
user_name = input("Enter your name: ")

# display the desired output
print(f"{icecream[-1]} {icecream[0]}, and {user_name} chooses to be {icecream[1]}")
