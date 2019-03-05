# *********************************************************************************************************************
# Notes:
#
# importing functions from other modules in your code and getting them to work the way you intend them to;
# sometimes importing functions into other modules has a tendency to run immediately.  You can avoid this
# by creating a facility to hold the module without it immediately running.
# When you import a Python module, its code loaded into memory and then executed; VERY IMPORTANT TO REMEMBER
# You only want to execute the code when the module is run as a script
#
# # blackjack.new_game() is code to run blackjack module, however you get an error msg.  After importing, black jack
# code didnt get a chance to run/ get executed so variables havent been defined, hence the errors

# How do we now get the blackjack module, Setup, to run?  Decide which bits of module you want executed when a module
# is imported and move the test for __name__ to allow that to happen.
#
# By convention, starting a name with an '_' indicates that it should be treated as protected, which means it's not
# intended to be used outside the module that it exists in. Doing so does indicate protection but does not deny
# access to the functions.  Just a good way to denote your code in case someone else does import your module, etc.
# When importing modules like blackjack, use the syntax 'Setup.[]' to indicate which objects you'd like to import
# - if you import a module and call its objects using 'import * ' all protected objects wont be visible
#
# - Using double '_' at the start of a name invokes Python's 'Name Mangling' rules... this convention mainly exists
# to prevent name clashes when subclassing objects; names w/ double '_' to start cant be imported with 'import *'
# - names that start and end with double '_' should not be changed
#
# *********************************************************************************************************************

import Setup
from Setup import *  # Great syntax to call all the objects of the imported module

# print(__name__)  # Python way of calling module file name w/o path or extension; '__name__' is an attribute of the
                   # module
# g = sorted(globals())
#
# for x in g:
#     print(x)

Setup._deal_card(Setup.dealer_card_frame)
Setup.play()