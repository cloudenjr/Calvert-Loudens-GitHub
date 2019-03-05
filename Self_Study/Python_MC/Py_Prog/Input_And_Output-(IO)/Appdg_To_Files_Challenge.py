# we can append to a text file by using 'a' as the mode. opening a text file in
# append mode causes the data to be written to the end of the file without
# overwriting the existing contents.

# Write a program to append the times tables to our jabberwocky poem in sample.txt.
# We want the tables from 2 to 12 (similar to the output from the For loops part 2
# lecture in section 6).
#
# The first column of numbers should be right justified. As an example, the 2 times
# table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
# ----------------------


with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'a') as challenge:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=challenge)
        print("-" * 25, file=challenge)

# the "{:>2}" in the preceding code represents the first character alignment; the
# ":" indicates your intention to format the variable and the ">2" dictates what
# direction you want your alignment to have.
# because this file is being appended, every time its run, it appends to what
# already exists, w/o overwriting it. if you change the 'a' to a 'w' then the file
# will be writen again, creating a new file (you'll obv have to change the name
# of course). 


