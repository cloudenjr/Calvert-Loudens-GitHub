# cerealization is the method of saving objects to a file so that they can be restored from the file later;
# Python provides a mechanism for cerealizing objects called pickling; when an object is pickled, it is
# written to a file in a format that contains the object's data together with enough information to allow that
# object to be recreated when its loaded back in.

# import pickle  #  we have to call the pickle method first, in order to use it; this is the method

# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open("imelda.pickle", 'wb') as pickle_file:  # writing the binary file
#     pickle.dump(imelda, pickle_file)

# the format of this data is specific to Python

# with open("imelda.pickle", 'rb') as imelda_pickled:  # reading the binary file
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

# Result set from the syntax above:
# ('More Mayhem', 'Imelda May', '2011', ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')))
# More Mayhem
# Imelda May
# 2011
# 1 Pulling the Rug
# 2 Psycho
# 3 Mayhem
# 4 Kentish Town Waltz

# reading the data out of the imelda.pickle file you've created and storing it in the 'imelda2' object/variable;
# this is just an example of how to read a file and store the information/data in another object/variable
# to call upon in your code later
# Once you open a file for writing, you can pickle as many objects within the file as you may choose

# ******************************************************************************************************************

# import pickle  #  we have to call the pickle method first, in order to use it; this is the method
#
# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", 'wb') as pickle_file:  # writing the binary file
#     pickle.dump(imelda, pickle_file, protocol=0)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=0)
#     pickle.dump(2998302 , pickle_file, protocol=0)
#
# with open("imelda.pickle", 'rb') as imelda_pickled:  # reading the binary file
#     imelda2 = pickle.load(imelda_pickled)
#     even_list = pickle.load(imelda_pickled)
#     odd_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
#
# print('=' * 40)
#
# for i in even_list:
#     print(i)
#
# print('=' * 40)
#
# for i in odd_list:
#     print(i)
#
# print('=' * 40)
#
# print(x)

# objects must be read back in the same order that they are written; very important to remember
# very few objects in Python that cannot be saved by pickling them; you should only be pickling
# data from trusted sources
# *************************************************************************************************

import pickle

pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.") # code to remove a file on a linux/Mac machine
# keep note of the action here, 'loading a file' which in turn, deleted another

