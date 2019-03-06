# ********************************************************************************************************************
# Challenge:
# Create a generator that will return the complete filename of all emp3 files.
#
# The generator should start at a specified directory, the start, which will be provided as an argument to the
# generator function.
#
# The filenames should include the full path from the specified start directory. So it'll return a relative path.
#
# It's a good idea to make your generator function a bit more generic, so it can handle files with any extension.
# So pass the extension as a second parameter to the function.
#
# Challenge 2:
# Modify the program to handle any exceptions that are raised by the id3reader module.
#
# If an exception is found, record the filename in a list, and move on to the next file.
#
# Once the loop finishes, print out all the files that caused an error.
# ********************************************************************************************************************

import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)       #  syntax to create an absolute path
            yield os.path.join(absolute_path, file)              # use it in yielded values


error_list = []
for f in find_music('music', 'emp3'):
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        error_list.append(f)

for error_file in error_list:
    print(error_file)

