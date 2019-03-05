# *********************************************************************************************************************
# Challenge 1:
# Create a Vampire class that's a subclass of Enemy.
#
# Vampires have 3 lives, and take 12 hitpoints of damage.
#
# You can create a new Python file for the Vampire if you like, but I'd suggest adding it to the existing enemy.py file
#
# Test your class by creating one or two Vampire instances and displaying their details. Also inflict some damage to
# make sure the 'take_damage' method works ok.
# Also make sure that the trolls can also take damage, because we haven't tested that yet.
#
# *********************************************************************************************************************
# *********************************************************************************************************************
# Challenge 2:
# Create a VampireKing subclass of Vampire. A VampireKing is going to be incredibly powerful, and any points of damage
# inflicted will be divided by 4.
#
# VampireKing objects will also start off with 140 hit points.  So extend the Vampire class to create a VampireKing
# subclass with those additional properties
#
# Test the new class by creating a new VampireKing object and checking that it does start with 140 hit points and only
# takes a quarter of the damage inflicted
# *********************************************************************************************************************
import random

class Enemy:
# class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Hit points: {0._hit_points}, Lives: {0._lives}".format(self)

class Troll(Enemy):  #  this is how you create a subclass; troll class will inherit from 'Enemy' class
    # pass # doesn't actually do anything but unlike a comment, 'pass' doesn't get ignored by the compiler
    def __init__(self, name):
        Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # to ensure class attributes are initialized, we've called the 'Enemy' superclass '__init__' method by
        # prefixing the method name with the class name; impt to provide correct number of parameters

        # If you want to cope with multiple inheritance, you must use the super instead of specifying the base class
        # name. See below syntax
        super(Troll, self).__init__(name=name,lives=1, hit_points=23)
        # super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=3, hit_points=12)
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        # import random  # just showing that it can be imported here but its customary to place it at beginning of Module
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

    def mantra(self):
        print("I am {0._name}. I want to suck your blood! Ha, Ha, Ha!".format(self))


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
