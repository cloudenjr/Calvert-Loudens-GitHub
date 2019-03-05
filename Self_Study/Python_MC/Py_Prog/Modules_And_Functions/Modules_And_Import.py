# *******************************************************************************************************************
#
# Turtle Demo:
#
# from turtle import forward, right, done
# import turtle
# import time

# done = "Well done, you have finished your drawing."
#
# from turtle import *
#
# # noinspection PyUnresovledReferences
# # to enable code inspection again, follow path:  Analyze > Con Curr File Analysis > Config Inspections >
# # scroll down to Python (if a change has been made, it'll show in blue) > Unresolved References to make changes
# forward(150) # no need to prefix these commands w/ 'turtle.' b/c we defined which functions from the turtle module
#              # that we actually need
# right(250)
# forward(150)
# circle(75)
#
# # time.sleep(4)
# done()
# print(done)

# ********************************************************************************************************************
#
# Python standard library
#
# print(dir())
# # print(dir(__builtins__)) # result set prints out left to right, makes hard to read
#
# for m in dir(__builtins__): # this code makes list more readable
#     print(m)

import random

help(random.randint)

# help(shelve)


# print(dir())
# print()
# print(dir(shelve))

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)
#
# shelve.Shelf.