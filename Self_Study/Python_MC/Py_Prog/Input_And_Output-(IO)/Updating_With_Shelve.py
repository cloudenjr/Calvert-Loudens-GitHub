# ******************************************************************************************************************
# Notes:
# Updating values stored in a shelve; also a common way to increase performance
# Keys must be stings, but values can be any Python objects; ie. 'dictionaries containing lists, as objects'
# Values are pickled before being stored in any underlying database fields, so the same rules from pickle apply to
# shelve;
# Disadvantages to Shelve:
# B/c values are pickled before being stored and unpickled when the values are read back, if the values are really
# complex, they may impose a signifcant overhead and impact performance, slow down application
# If application data being stored in the shelve module ever has to move to a different environment, the shelve
# module may not be supported and operate/perform as designed in that new environment; Concurrent access can be a
# problem with shelves, although concurrent read access is safe, if a prog is writing to the shelve then no other
# prog should have it open or attempt to open it.  Although shelves can be optimal at times, its better to store
# data in a database
# *********************************************************************************************************************

# import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # appending items, or adding to the file/list using the append function
    # what we've done below is append items to a copy of the list that's been
    # read into memory but when the code is run, the shelve function
    # isnt provided a trigger to know the items within the list have changed

    # blt ['bacon', 'lettuce', 'tomato', 'bread']
    # scrambled_eggs ['eggs', 'butter', 'milk']
    # beans_on_toast ['beans', 'bread']
    # pasta ['pasta', 'cheese']
    # soup ['tin of soup']

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # this below method, is how you fix the above problem/issue, so now if you
    # comment out the code below, (after its been run itially) the result set
    # should now contain the updates to 'blt' and 'pasta'; benefits of this approach
    # is that you now get to work with objects in memory w/ all the performance benefits
    # and much faster than reading/writing to disc, but disadvantage is having to reassign
    # any immutable objects that have changed back to their keys in the shelve (code 64 - 70)
    # The 'writeback' method is less coding, but takes up more memory space (heavier memory
    # usage, which can be cumbersome depending on data) and is less efficient;
    # when you use 'writeback', Python cases the object in memory which doesnt actually
    # update the shelve file until you close it or use the 'sync' method; if there's been a lot
    # of changes, closing the shelve can take quite a while b/c everything needs to be
    # written to disc at once.
    # The 'Sync' method, sync itself causes all entries in the cache to be written to disc but
    # it also clears the cache out as well; sync function is called automatically when the shelve
    # is closed, but you can use it anytime you want to force the data files to be updated

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # recipes["soup"].append("croutons") # probably the best method to use to update objects if using shelve
    # the 'sync' method below has a result set that shows no update of 'soup' and thats b/c
    # the soup list object is stored in the cache, and the sync function causes the cache
    # to be cleared
    # recipes["soup"] = soup
    # recipes.sync()
    # soup.append("cream") # this line of code does append "cream" to the list but there's no
    #                      # corresponding list object in the cache anymore b/c we called
                         # recipes.sync(). So when we loop through the shell printing the list
                         # we're actually retrieving the list from disc again

    # result set for above code:
    # scrambled_eggs ['eggs', 'butter', 'milk']
    # blt ['bacon', 'lettuce', 'tomato', 'bread', 'butter']
    # beans_on_toast ['beans', 'bread']
    # pasta ['pasta', 'cheese', 'tomato']
    # soup ['tin of soup']


# for snack in recipes:
#         print(snack, recipes[snack])

# ********************************************************************************************************************

# Common source of error when converting a dictionary that is initialized using a literal into a shelve; Error below...

# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# "/Volumes/LACIE SETUP/Data_Science/Python_MC/Py_Prog/Input_And_Output-(IO)/Updating_With_Shelve.py"
# Traceback (most recent call last):
# File "/Volumes/LACIE SETUP/Data_Science/Python_MC/Py_Prog/Input_And_Output-(IO)/Updating_With_Shelve.py", line 109, in <module>
# print(books["recipes"]["soup"])
# TypeError: tuple indices must be integers or slices, not str

# error is made by leaving the comma at the end of each value; to fix error, remove commas from lines 112-17, remove "soup"
# from line 120 and comment out 121 and 123.


import shelve # conversion to a shelve;

books = shelve.open("books")


books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambled_eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]},
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])

print(books["maintenance"]["loose"])
books.close()
