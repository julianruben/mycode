#!/usr/bin/env python3
user_name = input("Please enter your name: ")
day_week = input("Please enter day of the week: ")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("\n")
print("Hello {}! Happy {}!".format(user_name, day_week ))
print(f"Hello {user_name}! Happy {day_week}!")
