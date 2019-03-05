# *********************************************************************************************************************
# Notes:
# - Constructor: refers to a special method that is executed when an instance of a class is created or constructed (__init__)
#
#
#
# *********************************************************************************************************************

class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):  # 'self' is a reference to the instance of the class
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# b/c 'kenwood & hamilton' are objects, we can specify their attributes in the replacement fields.
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"  # changing class attribute changes all similar attributes of children functions
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
