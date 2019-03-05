# ********************************************************************************************************************
# Notes on Kwargs:
# - '**' annotation allows us to unpack a dictionary
# - when using the '**kwargs' parameter, whatever is passed to the print function will get printed
#
# Challenge:
#
# Fix the 'print_backwards' function, so that it correctly handles the case when the calling code also specifies the
# 'end' keyword argument.
#
# Tip: You may want to remove the 'file=backwards' from the call to 'print_backwards', so you dont have to keep opening
# the file to check the results.
# ********************************************************************************************************************


# def print_backwards(*args, file=None):
# def print_backwards(*args, end=' ', **kwargs):

# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:  # change the range
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)  # which means we dont need this line
    print(args[0][::-1], end=end_character, **kwargs)  # and print the first word separately

# syntax code to print backwards; the function 'print_backwards' was just an example to demostrate the
# functionality of kwargs; not a actually good way to code this function. this next example is though

def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another string")

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
