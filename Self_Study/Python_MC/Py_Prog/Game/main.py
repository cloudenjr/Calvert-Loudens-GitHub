# ********************************************************************************************************************
# Notes on Getters and Setters in Python:
#
# Getters are a method that is used to get the value of a data attribute
# - ' print(tim.get_name()) ' where 'get_name' is a getter where it returns the value of the corresponding variable
#
# Setters are a method that is used to set the value of a class data attribute
# - ' tim.set_lives(300) ' where 'set_lives' is the setter; setters are useful in checking the value before updating
#     the attribute
# - data attribute musn't have the same name as the property
# *********************************************************************************************************************
#import Player
# from player import Player
#
# #tim = Player.Player("Tim")
# tim = Player("Tim")
#
# # print(tim.name)
# # print(tim.lives)
# # tim.lives -= 1
# # print(tim)  # the '.lives' function was removed from tim due to us creating the '__str__' function in Player Module
# #
# # tim.lives -= 1
# # print(tim)
# #
# # tim.lives -= 1
# # print(tim)
# #
# # tim.lives -= 1
# # print(tim)
# #
# # tim._lives = 9
# # print(tim)
# #
# # tim.level = 2
# # print(tim)
# #
# # tim.level += 5
# # print(tim)
# #
# # tim.level = 3
# # print(tim)
# #
# # tim.score = 500
# # print(tim)
#
# from enemy import Enemy, Troll, Vampire, VampireKing
#
# # random_monster = Enemy("Basic enemy", 12, 1)
# # print(random_monster)
# #
# # random_monster.take_damage(4)
# # print(random_monster)
# #
# # random_monster.take_damage(8)
# # print(random_monster)
# #
# # random_monster.take_damage(9)
# # print(random_monster)
#
# dracula = VampireKing("Dracula")
# print(dracula)
# dracula.take_damage(12)
# print(dracula)
                                                                             
# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vampire_1 = Vampire("Dragor")
# print("Dragor - {}".format(vampire_1))
# vampire_1.take_damage(5)
# print(vampire_1)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
#
# while vampire_1._alive:
#     vampire_1.take_damage(1)
#         # print(vampire_1)

a = 3
b = "tim"
c = 1, 2, 3

print(a)
print(b)
print(c)
