# Iterators object that represents a stream of data; returns this data one element at a time
# for loop uses each interator to return an element in the string below. when there are no more
# elements in the string, the iterator returns an error, which is handled by the for loop.

string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)  # creating your own iterator method using key word 'iter()' then pass in the string within
                            # parentheses.  Doing so creates the iteration but doesnt actually make its way through the
                            # elements just yet.  Need to add 'print(next(my_iterator- or assigned variable)' to start
                            # the loop.

# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

for char in string:
    print(char)

for char in iter(string):
    print(char)