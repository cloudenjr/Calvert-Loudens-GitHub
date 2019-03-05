# the drawback of pickling objects is that the objects all have to be loaded back into memory
# the shelve module, provideds a shelf, think of it as a dictionary, but its stored in a file rather than in memory
# like a dictionary, the shelve holds key value pairs, and the values can be anything that can be pickled; keys
# themselves must be strings, unlike a dictionary, where the keys can be immutable objects, such as tuples.
# difference between shelve and dictionary is that shelves have no literal; u cant initialize a shelve as a literal
# like you can a dictionary; shelve key must be a string while a dictionary will accept any immutable object as a key

import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow, citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# result set below, shows 'fruit' is a shelve; 'with' statement automatically closes the loop

# a sour, yellow, citrus fruit
# a small, sweet fruit growing in bunches
# <shelve.DbfilenameShelf object at 0x1017436a0>


# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We dont have a " + dict_key)

    # description = fruit.get(dict_key, "We dont have a ", +dict_key)
    # print(description)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()  # using the ".sort" function to get the result set in alphabetical order
#
# for f in ordered_keys:
#     print(f + "-" + fruit[f])
# *********************************************************************************************************************

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()

# the preceding codes result set:

# a sweet, orange, citrus fruit
# good for making cider
#     a sour, yellow, citrus fruit
# a small, sweet fruit growing in bunches
# a sour, green citrus fruit
# ValuesView(<shelve.DbfilenameShelf object at 0x10505e4e0>)
# ('orange', 'a sweet, orange, citrus fruit')
# ('apple', 'good for making cider')
# ('lemon', 'a sour, yellow, citrus fruit')
# ('grape', 'a small, sweet fruit growing in bunches')
# ('lime', 'a sour, green citrus fruit')
# ItemsView(<shelve.DbfilenameShelf object at 0x10505e4e0>)


# print(fruit)

# ******************************************************************************************************************

# import shelve
#
# with shelve.open('ShelfTest') as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#             "apple": "good for making cider",
#             "lemon": "a sour, yellow, citrus fruit",
#             "grape": "a small, sweet fruit growing in bunches",
#             "lime": "a sour, green citrus fruit"}
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

# this preceding code is an example of how shelves act differently than dictionaries
# *******************************************************************************************************************