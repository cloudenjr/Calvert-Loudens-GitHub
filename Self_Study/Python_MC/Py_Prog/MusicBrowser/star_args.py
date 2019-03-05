# ********************************************************************************************************************
# * Args Notes:
# - '*args' is the magic that lets a function or method take a variable # of arguments
# - the '*' in '*args' is used to unpack a tuple
# - '*args' should be the last parameter specified; anything that follows it must be a keyword parameter
#
# Challenge:
#
# Write a function called build_tuple that takes a variable number of arguments, and returns a tuple containing the
# values passed to it.
#
# Challenge 2:
#
# A function that takes a variable number of words, and returns the average word length.
#
# A function that returns the smallest or largest of the numbers passed to it.
#
# A function to print all the words passed to it backwards, in reverse order. So the output will read correctly from
# right to left. Hint: We saw how to reverse a string using a slice of [::-1], and that can also be used with tuples
#
# Create a list, let's say you called it 'words.' Print the list, but also print '*words', to see that '*' can be used
# to unpack a list as well as a tuple.
# 
# ********************************************************************************************************************
# from __future__ import print_function  #  synatx to make make Python 3 feature available within a Python 2.7 framework

# word_list = []
#
# iter_list = list(''.join(word_list))


def build_tuple(*args):
    return args


def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def avg_word_length(*args):
    word_list = [print(*args)]
    num_of_char = 0
    for char in iter_list:
        num_of_char += char
    return num_of_char / int(*args)


# print(average(1, 2, 3, 4))
# print(build_tuple('my', 'favorite', 'soccer', 'player', 'is', 'ronaldinho'))

