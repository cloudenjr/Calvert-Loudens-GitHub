# Create a program that takes some text and returns a list of all the characters in the
# text that are not vowels, sorted in alphabetical order.
#
# You can either enter the text from the keyboard or initialize a string variable with the
# string.


vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}

text_string = set(input("Please enter a string of text: "))

finalSet = set(text_string).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)