# Tuples are an ordered set of data that cannot be changed; commas are used to separate the elements
# within a Tuple, however the parentheses are used to remove any syntactic ambiguity
# Tuples support slicing and indexing; tuples are used to contain items of different types

# t = "a", "b", "C"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"),  (3, "Mayhem"), (4, "Kentish Town Waltz")
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)


# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# imelda = imelda[0], "Imelda May", imelda[2]  # since tuples cannot be altered, I used indexing and declaring to change value
# print(imelda)

# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
#
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
#
# title, artist, year = imelda  #  this method is referred to as 'unpacking' the tuple
# print(title)
# print(artist)
# print(year)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imelda May", 2011, 1, "Pulling the Rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish Town Waltz"

print(imelda)

title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
