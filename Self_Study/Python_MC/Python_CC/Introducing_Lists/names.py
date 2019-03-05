names = ["James", "Jared", "Jeremy", "Kim", "Kenny", "Jason", "Eddie", "Adam", "Vinny", "Davon", "Nate"]

cars = ["audi", "bmw", "acura", "lexus", "volkswagen"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])
# print(names[7])
# print(names[8])
# print(names[9])
# print(names[10])

for name in names[0:10]:
    print("Hello " + name + " it's great to see you!")

print('*' * 40)

for car in cars[0:4]:
    if car == "bmw":
        print("I'd like to own a " + car.upper() + " one day!")
    else:
        print("I'd like to own a " + car.title() + " one day!")
