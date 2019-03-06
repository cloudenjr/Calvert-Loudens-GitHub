import sys


def my_range(n: int):   # syntax for defining variable 'n' in my_range as an integer
    print("my_range starts.")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1

# _ = input("line 12")  # underscores here indicate to Python that we are not interested in the value of the variable
# big_range = range(5)
big_range = my_range(5)
# _ = input("line 15")

print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# Create a list containing all the values in big_range
big_list = []   # list is being initialized here by creating an empty list to store values from big_range

# _ = input("line 22")
for val in big_range:
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
# for i in big_range:
for i in my_range(5):
    print("i is {}".format(i))












# ********************************************************************************************************************
# Notes on Generators:
# - bad idea to assign a range to a variable b/c if/when using for/while loops, if the variable is called before loop
# begins, the 'next' variable in the range will be the first item iterated over within the loop, puttings results off
# - using the variable big_range again in the next for loop doesnt work b/c the function itself has been exhausted and
# run its course.  If you want to use the range again in a loop, you must call the function itself my_range(n) instead
# of the variable
# - 'range' class behaves like an iterable and resets each time its used/called
#
#
#
