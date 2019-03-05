a = 12
b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
#
# for i in range(1, a//b):
#     print(i)
#
# print(a + b / 3 - 4 * 12)
# print(8 / 2 * 3)
# print(8 * 3 / 2)
#
# print((((a+b) / 3) - 4) * 12)
#
# c = a + b
# d = c / 3
# e = d - 4
# print(e *12)
#
# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot [3])
# print(parrot [-1])
# print(parrot [0:6])
# print(parrot [:6])
# print(parrot [6:])
# print(parrot [-4:-2])
# print(parrot [0:6:2])
# print(parrot [0:6:3])
#
# number = "9,223,372,036,854,775,807"
# print(number [1::4])
# numbers = "1, 2, 3, 4, 5, 6, 7, 8, 8, 9"
# print(numbers [0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
# code below allows you to concatenate strings without the use of the '+' operator since all the objects are strings
print("he's " "probably " "pining")
print("hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")
today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")

age = 24
print("My age is " + str(age) + " years")
# python allows you to store variables as data types for conversion and concatenation

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} ".format(31, "January", "March", "May", "July", "August", "October", "December"))
# python's replacement field syntax;  the {} and .format(defined variable) above and below
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" % ( 22 / 7))

for i in range(1, 12):
        print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i **2, i **3))

        print("Pi is approximately {0:12.50f}".format( 22 / 7))
