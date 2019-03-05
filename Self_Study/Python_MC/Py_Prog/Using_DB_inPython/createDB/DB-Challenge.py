# *********************************************************************************************************************
# DB Challenge 1:
# Create a new Python file, and write the code to print out all the records in the contacts.sqlite database
#
# Check the result, and explain why it's not what we'd expect.
#
# DB Challenge 2:
# Modify the DB-Challenge.py program so that it asks the user to enter a name, then use a where clause in the SQL
# statement to retrieve just the row for that one person.
#
# It seems simple, but if you find yourself struggling with the Python syntax, then go back and watch the 'Tuple'
# videos in Section 7.
#
# Before you start, remember to change the table name back to 'contacts' - we changed it to sqlite_master earlier.
# *********************************************************************************************************************

import sqlite3

db = sqlite3.connect("contacts.sqlite")  #  this line will create the contacts.sqlite DB if it doesnt already exist,
                                         #  otherwise it'll just open it.

new_name = input("Please enter a name: ")

# for row in db.execute("SELECT * FROM contacts WHERE name = ?", (new_name,)):   # '=' clause here is specific
#    print(row)

for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (new_name,)):
    print(row)

db.close()
