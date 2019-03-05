# jabber = open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r')
# open is the built in function to open a file; code below is reading text from a text file in read mode, ('r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         # print(line)
#         print(line, end='')
#
# jabber.close()

# syntax for opening and reading a text file without having to code in clossing the file after reading. this is
# accomplished with the use of the 'with' statement

#  with open("Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()  # using the while loop here to iterate through each line of the txt file

# with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r') as jabber:
#     lines = jabber.readlines() # readlines reads the entire file in one go
# print(lines)
#
# for line in lines:
#     print(line, end='')


with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r') as jabber:
    lines = jabber.readlines() # readlines reads the entire file (read into memory) but gives a list of strings rather than just
                               # a single string;  read line reads a single line from a file and returns a string
print(lines)

for line in lines[::-1]:
    print(line, end='')


with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/sample.txt", 'r') as jabber:
    lines = jabber.read()  # reads entire file and if a text file, returns a string containing the contents of the file

for line in lines[::-1]:  # this syntax prints strings in reverse order;
    print(line, end='')


