a_string = "This is\na string split\t\tand tabbed"
print(a_string)

# Raw string literals were introduced to remove the need to double up on backslashes '\\' in a string
# - are sometimes used to specify file paths in Windows, which use the '\' character to separate directory names
raw_string = r"This is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "This is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\follwed by some text"
print(backslash_string)

# Output of the above code.

# This is
# a string split		and tabbed
# This is\na string split\t\tand tabbed
# this is
# a string split		and tabbed
# This is a backslash ollowed by some text
# this is a backslash \follwed by some text

error_string = r"this string ends with \\"
