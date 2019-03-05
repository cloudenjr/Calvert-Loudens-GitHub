# ********************************************************************************************************************
# Notes:
# - output of this code: each row is printed as a tuple, containing a value for each of the columns in the DB
# - a DB cursor is iterable so we can use a 'for' Loop to iterate over the cursor and print each row
# - we could also unpack the tuple as we go: ' for name, phone, email in cursor: print(name) print(phone) print(email):
# - sqlite wraps things like inserts and deletions in a transaction; common among DBs, idea is that if smthg goes
# wrong, the entire transaction can be rolled back.
# Tim
# 6545678
# Tim@email.com
# ____________________
# Bryan
# 1234
# bryan@email.com
# ____________________
#
# - DO NOT USE ';' to end SQL statements in Python
# - 'fetchone()' function used to return the next row in the cursor
# ********************************************************************************************************************

import sqlite3

db = sqlite3.connect("contacts.sqlite")  #  this line will create the contacts.sqlite DB if it doesnt already exist,
                                         #  otherwise it'll just open it.
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 6545678, 'Tim@email.com')")
db.execute("INSERT INTO contacts VALUES ('Bryan', 1234, 'bryan@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())  # the 'fetchall()' function has returned a list containing a tuple for each row in the DB
                          # - it is possible to get all the rows from a DB into a list, then you can move backwards
                          # and forwards through the items in the list.


print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:  # this is the method for unpacking the tuples, or 'rows w/ data' from a DB
    print(name)
    print(phone)
    print(email)
    print('_' * 20)

# for row in cursor:
#    print(row)

cursor.close()
db.commit()  # 2 important things about the commit function:
             # a) its crucial to commit any changes that you make to the DB if you want those changes to be persistent
             #   - if you fail to commit the changes they will be lost when you close the connection to the DB
             # b) cursors can be very useful, but if you want to run a query and loop through the results, you can
             # execute the query using the connection without explicitly creating the cursor
             # ' db = sqlite3.connect("contacts.sqlite")' - the connections '.execute' method does return a cursor when
             # you execute a SELECT statement but you dont have to worry about explicitly defining one
db.close()
