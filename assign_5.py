#!/usr/bin/env python3

# Created by: Adam Winogron
# Created on: May 19, 2022
# This function calculates the volume of a sphere using functions

# import the math unit
import math


# function that calculates volume
def calculate(user_radius, unit):

    # calculate the volume
    volume = 4 / 3 * math.pi * user_radius**3

    # return volume variable and updated value
    return volume;


# main function
def main():

    # explain the program
    print("If you give me the radius of a sphere I'll tell you it's volume!")
    print()

    # try statement to caatch invalid entries
    try:
        # input
        user_radius = float(input("What's it gonna be?: "))
        print()

        # get unit
        unit = input("Now I'll need the unit of \
measurement (cm, m, km, mm, etc.,: ")

        # function call
        volume = calculate(user_radius, unit)

        # print final volume and round
        print()
        print("The volume of a sphere \
with a radius of {}{} is {:.2f}{} ^3!".format(user_radius, unit, volume, unit))

    # exception
    except Exception:

        # tell the user their entry was invalid
        print()
        print("Sorry, we need a number to do math!")


# call main
if __name__ == "__main__":
    main()
