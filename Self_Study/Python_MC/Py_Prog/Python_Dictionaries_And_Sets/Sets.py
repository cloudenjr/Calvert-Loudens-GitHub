# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("*" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# # times when you need to use the set function:  when you're creating empty sets; can't use curly braces b/c that
# # creates an empty dictionary
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set2 = {} this method creates a dictionary and dictionaries do not use/call the 'add' function  to update
# a dictionary
# empty_set.add("a")
# empty_set2.add("a")

# even = set(range(0, 40, 2))
# print(even)
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares))) #  union operator is combining the two sets
#
# print(squares.union(even))
#
# print("-" * 40)
#
# # ways of calling the 'intersection' method; using the function itself or the '&' symbol
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# # just another method on how to use the 'difference' or 'subtract' operator with/out sets
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# # here, 'difference_update' is subtracting common numbers shared with squares from
# # the even set, resulting in a smaller set size.
# print("*" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# Symetric difference between two sets is all the members that are in one set or the other
# but not both; symmetric diff is often referred to as the opposite of intersection

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# # print(sorted(squares))
# print(squares)

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# 2 ways to remove items from a set, 'discard' and 'remove';  only diff btwn them is if
# item to be removed doesnt exist, you'll get an error msg and using discard wont

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, does nothing b/c 8 is not a part of the set
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")



# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")


# frozen sets are immutable sets and cannot be changed; frozen sets have no 'add' attributes to
# manipulate the set. Outside of the inability to add or remove members, frozen sets can be used
# to create unions, intersections and can be subtracted from other sets

even = frozenset(range(0, 100, 2))

print(even)
even.add(3)