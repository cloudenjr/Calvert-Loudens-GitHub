# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, # flush=True) # the '=' here is used to provide a named argument
                                    # in place of a file parameter instead of normally
                                    # being used for assignment, i.e "i = 5"
# preceeding syntax is code for writing the list to txt.file and storing it in the defined path
# ***************************************************************************************************************

# cities = []
#
# with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city) # you could rid result set of newline (\n) by using
#                             # 'cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)  # you could use 'print(city, end='')' to rid result set of newline
    # preceeding code prints this:
    # ['Adelaide\n', 'Alice Springs\n', 'Darwin\n', 'Melbourne\n', 'Sydney\n']
    # Adelaide

    # Alice Springs

    # Darwin

    # Melbourne

    # Sydney

# result set is printed with a space/newline (\n) between the cities.
# use the strip function from a string to remove the newline (\n) from a string.

# ***************************************************************************************************************

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/Py_Prog/Input_And_Output-(IO)/imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
#     # writing list to a txt.file and storing in the defined path
# **********************************************************************************************************************

with open("/Volumes/LACIE SETUP/Data_Science/Python_MC/Py_Prog/Input_And_Output-(IO)/imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
