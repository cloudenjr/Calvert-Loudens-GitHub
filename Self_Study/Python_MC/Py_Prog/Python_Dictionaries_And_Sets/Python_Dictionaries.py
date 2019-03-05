# Dictionaries and sets are unordered collections and they both also guarantee there will be no
# duplicates within the collection. Sets are similar to lists in that they store similar items
# but you cant access individual items using an index because the set is unordered. Dictionaries
# are unordered and contain key value pairs and cannot be accessed by index but by means of a key.
# In the example below, the key is denoted by the string ending in a ':'

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# print(fruit["lemon"])
# # how to add an entry to the dictionary; need to do it this way b/c unlike lists, there is no way to
# # insert or append items to the dictionary;  need to put the key in [] brackets
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila" # how to override the value of an item. You can add this to the list
# # above, however it will only override the value of the duplicate key.
# print(fruit)
# del fruit["lemon"] # how to delete an item from the dictionary - notice the use of [] brackets instead of parens.
# # if you dont specify a key to delete, it will delete the entire dictionary so be careful using this!
# # fruit.clear() removes all items in the dictionary without deleting the dictionary itself
# print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We dont have a " + dict_key)
#     print(description)
    # fruit.has_key(dict_key) is a Python 2 code syntax and is equivalent to the (" if dict_key in fruit: ")
    # use the method below to perform an action/decision (" If/Else ") after testing whether the inputted value exists within the
    # dictionary defined in the code.
    #
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have a " + dict_key)

# the syntax below prints out the value of each key without the assigned key. when the code is run, there is no
# guarantee the list will appear in the same order when run, hence the association with an "unordered list." - Each
# execution results in a different order to the result set/dictionary or set.

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " +  fruit[snack])
#     print('-' * 40)

# if you want your results to be displayed in a particular order, do not attempt to do so while
# creating your dictionary/set.  Only do so when you are ready to print/process the code in that
# particular order. To do so you create a list from the dictionary keys, sort the list and iterate
# over the list to display the results.  ex below

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# # ordered_keys = sorted(list(fruit.keys())) is equivalent to the two lines of code above
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# Syntax for completing the above code all in two lines. Use the '.keys' command when you need to
# sort the result set you are iterating through.  Otherwise, " for f in fruit: " would work.
# for f in sorted(fruit.keys()):
#   print(f + " - " + fruit[f])

# *************************************************************************************************
# for val in fruit.values():
#   print(val)
#
# for key in fruit:
#   print(fruit[key])  this method is far more efficient than the above equivalent.  Great way to
#                      optimize code
# *************************************************************************************************

# *********************************************************************************************
# both return list-like objects. 'fruit.keys' returns 'dict_keys' objects and 'fruit.values'
# returns 'dict_values' objects. Both of these are called "view objects" and if the underlining
# dictionary changes then these objects will as well.
#
# print(fruit.keys())
#
# print(fruit.values())

# *********************************************************************************************


# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items()) # taking a list and storing it as a variable to call upon later
                               # in your code.
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

# preceeding code explains how a dictionary can be created from a tuple or list;














