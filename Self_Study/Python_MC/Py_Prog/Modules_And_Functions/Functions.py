# *********************************************************************************************************************
#
# Funtion Notes:
#
# In Python, functions are created with the word def followed by function name and a pair of ()s; because the def
# statement introduces a block of code, it MUST be followed by a colon, ':'.
# All Python functions return a result; if you dont tell a function what result to return, it returns 'none' by
# default. Parameters are variables defined in the function definition itself; what's in the ()s
# Purpose for creating functions:  you create a block of code and then call it when you need it.
# - Concatonating strings in a list isnt very efficient, try using list comprehensions
#
#
# *********************************************************************************************************************


def python_food():  # creating the function 'python_food'
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def center_text(*text):  # '*' denotes a variable number of parameters
# example of a function that allows text to be printed centered on a screen;
def center_text(*args, sep=' '): # ,end='\n', file=None, flush=False):
    # text = str(text)
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text  # instead of passing the string on to print to file, we use the return key word
                                    # to indicate that the string should be returned when the function is called

# code syntax to have resulting output/text/data sent to a file
# with open("centered", mode='w') as centered_file:

# calling the function
# python_food()
# print(center_text("spam and eggs")) # ,file=centered_file)
# s1 = center_text("spam and eggs") # this is just another way of writing the code above; we've assigned the value
#                                   # that has been returned from the function center_text, assigned it to a variable
#                                   # and then printed that variable
# print(s1)
# print(center_text("spam, spam and eggs")) # ,file=centered_file)
# print(center_text(12)) # ,file=centered_file)
# print(center_text("spam, spam, spam, and spam")) # ,file=centered_file)
#
# # print("first", "second", 3, 4, "spam")
# print(center_text("first", "second", 3, 4, "spam", sep=':')) # ,file=centered_file)

# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))

with open("menu", "w") as menu:
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text("spam, spam and eggs")
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    s5 = center_text("first", "second", 3,4, "spam", sep=":")
    print(s5, file=menu)
