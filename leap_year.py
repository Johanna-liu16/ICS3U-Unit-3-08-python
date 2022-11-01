#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import random


def main():
    # this is a number guessing game

    # input
    print("This program identifies a leap year.")
    str_year = input("Enter year: ")

    # process
    try:
        int_year = int(str_year)
        if int_year < 0:
            print("Invalid year")
        else:
            if int_year % 4 == 0 or int_year % 400 == 0:
                if int_year % 100 == 0 and int_year % 400 != 0:
                    print("This is not a leap year")
                else:
                    print("This is a leap year.")
            else:
                print("This is not leap year.")
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
