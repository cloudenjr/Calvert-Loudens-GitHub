# *********************************************************************************************************************
# Exception Handling Notes:
# - 2 types of errors: Syntax errors & Exceptions
#      - a) Syntax Errors: we make a mistake in the code
#      - b) Exception Errors: when our programs are run and we get other errors related to flaws in the progams logic
#           or conditions we could not predict
#
# - if you dont handle an exception in your code when it occurs then the program crashes
# - Python prints out the details of the exception and a step-trace showing where the exception occurred
# - How to Handle:  wrap your code that's likely to raise an exception within a 'try & except' block and then decide
#   what action to take when an exception is raised
#
# *********************************************************************************************************************

def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)
try:
    print(factorial(900))
# handling multiple exceptions in a single except clause:
except (RecursionError, ZeroDivisionError):
# except RecursionError:
   print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
   print("What are you doing dividing by zero?")

print("Program terminating")
