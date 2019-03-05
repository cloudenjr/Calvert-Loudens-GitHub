# *********************************************************************************************************************
# Exceptions Challenge:
#
# Create a new Python file, and write a short program to ask the user to type in two integer numbers, then print out
# their first number divided by their second.
#
# The program shouldn't crash, no matter what the user types in (although you don't have to worry about Ctrl keys).
#
# Hint: If you have to do the same thing more than once, that sounds like a good use for a function.
#
# *********************************************************************************************************************
import sys


def get_int(prompt):
    while True:
        try:
            # number = int(input("Please enter an number: "))
            number = int(input(prompt)) # use of prompt here as a Var to vary message when asking for 1st or 2nd number
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:  # if you use a finally clause, it MUST come after ALL exception clauses
            print("The finally clause always executes. ")  # finally clause ALWAYS executes whether an exception was
                                                           # handled or not

# Finally block uses:
# - ideal place for performing any tidying up that may be required before your code finishes
# - closing a database cursor or connection, closing any open files

# x = int(input("Please enter a number: "))  # this syntax is a test we can use to crash the program and determine what
                                           # error msg we need to write an exception for; try entering anything but a #

first_number = get_int("Please enter first number: ")
second_number = get_int("Please enter second number: ")

try:
    print("{} divided by {} is {}".format(first_number,second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero.")
    sys.exit(2)
else:
    print("Division performed successfully. ")

# How is the 'else' block here different than the 'finally' clause?
# - well, the code in the else clause only executes if the try block completed w/o raising an exeception