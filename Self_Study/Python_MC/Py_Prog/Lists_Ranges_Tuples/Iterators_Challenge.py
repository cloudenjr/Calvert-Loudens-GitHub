# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint:  use the len() function rather than counting the number of items in the list.

menu = []
menu.append(["ackee", "salt fish", "dumplings", "bread fruit"])
menu.append(["ackee", "dumplings", "banana", "plantains"])
menu.append(["salt fish", "mackrel", "dumplings", "banana", "plantains"])
menu.append(["ackee", "dumplings", "banana", "bread fruit"])
menu.append(["salt fish", "plantains", "bread fruit", "bully beef"])
menu.append(["ackee", "dumplings", "bully beef"])

print(menu)

my_iterator = iter(menu)

for i in range(0, len(menu)):
    next_item = next(my_iterator)
    print(next_item)

# for meal in menu:
#     if not "bully beef" in meal:
#         print(next(my_iterator))

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))