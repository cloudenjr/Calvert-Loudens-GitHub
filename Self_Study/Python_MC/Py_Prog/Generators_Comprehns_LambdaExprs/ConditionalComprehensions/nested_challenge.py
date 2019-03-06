# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.
 
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print()

times_tables = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(times_tables)

for x, y in  [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)


# syntax for creating a 'generator expression'... use () instead of []; isnt creating the entire list in memory
# generator expressions calculate the value as they're requested, the only value that exists is the one that has
# just been returned.
# - consider using a generator expression rather than a list comprehension if you're not going to be using the list
# more than once
# - not clear if performance suffers using one method vs. the other
for x, y in  ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)
