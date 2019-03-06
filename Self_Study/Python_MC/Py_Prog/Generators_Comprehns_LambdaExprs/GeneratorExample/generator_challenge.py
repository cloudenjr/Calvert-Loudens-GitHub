# *******************************************************************************************************************
# Challenge:
# Create a generator to return an infinite sequence of odd numbers, starting at 1.
#
# Print the first 100 numbers, to check that the generator's working correctly.
#
# Note that this is just for testing. We're going to need far more than 100 numbers, and don't know in advance how
# many, so that's why we're creating our own generator, instead of just using range.
#
# ********************************************************************************************************************
import sys

def odd_range():
    n = 1
    while True:
        yield n
        n += 2

# odds = odd_range()

# test code:
# for i in range(100):
#     print(next(odds))

def pi_series():
    odds = odd_range()
    approximation = 0
    while True:   # this syntax sets an infinite loop
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(1000000):
    print(next(approx_pi))
