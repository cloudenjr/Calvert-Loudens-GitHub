# *********************************************************************************************************************
# Notes:
# Object Oriented Programming:
# - aims to combine the data and the processes that act on that data into objects, which is called encapsulation
# - OOP makes use of imperative programming within the methods that objects use to manipulate their data
# - in OOP, replacing one object with another that performs the same task w/o having to concern ourselves with the
#   details of how it performs the task is a central concept
# - OOP uses classes & methods(functions) to provide objects that encapsulate both data and the functions that operate
#   on that data
# - when a function is part of a class in Python, we call it a 'method'
# - 2 different paradigms of programming:
#   - Imperative: involves providing a series of instructions for the computer to follow in a defined order
#
#
#
#
# Classes:
# - think of a class as a template from which objects can be created; all objects created within the same class share
#   the same characteristics
# - an instance is just another name for an object created from a class definition
# - when a variable is bound to an instance of a class, then it is referred to as a 'data attribute'
# - classes are dynamic and can be modified after they've been created
#
# *********************************************************************************************************************

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))