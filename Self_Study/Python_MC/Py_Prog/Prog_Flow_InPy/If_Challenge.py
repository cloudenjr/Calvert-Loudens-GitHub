# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday. (They must be
# over 18 and under 31 years of age.)
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to club 18-30, {0}".format(name))
else:
    print("We're sorry, but club 18-30 is for seriously cool people, {0}".format(name))