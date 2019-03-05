# *********************************************************************************************************************
# Notes:
# - in Python, when you want to just iterate over the resulting dataset, Python allows you to execute queries using the
# connection w/o having to create a cursor
# - you really should commit the changes after performing the update
# - use the cursor to commit the changes rather than the connection: cursor objects themselves don't have a 'commit'
# method, but they do have a 'connection' property that we can use to get a reference to the connection that the
# cursor's using.
#
# *********************************************************************************************************************

import sqlite3

db = sqlite3.connect("contacts.sqlite")  #  this line will create the contacts.sqlite DB if it doesnt already exist,
                                         #  otherwise it'll just open it.

new_email = "newemail@update.com"
phone = input("Please enter the phone number ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
# update_cursor.executescript(update_sql)  # '.executescript' function allows Python to execute multiple statements
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are the connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):  # upacking the tuple method syntax
    print(name)
    print(phone)
    print(email)
    print('_' * 20)

# for row in db.execute("SELECT * FROM contacts"):  #  displays each row in the DB as a list containing values based on
#    print(row)                                     #  column data types

db.close()
