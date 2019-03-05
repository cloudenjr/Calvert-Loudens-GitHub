car = 'audi'

dream_list = ['aston martin', 'bmw x6', 'audi s5', 'audi r8', 'audi qs5', 'roles royce', 'wrangler']

my_age = 35


print("Is car == 'audi'? I predict true.")
print(car == 'audi')

print("\nIs car == 'bmw'? I predict false.")
print(car == 'bmw')

print("Conditional Test 1: ")
print("Is 'audi' equal to 'Audi'?:")
print('audi' == 'Audi')
print('audi' == 'Audi'.lower())

print("Conditional Test 2: \n")

print("Is my age equal to: " + str(my_age) + " ? I predict True.")
print(my_age == 35)
print('-' * 40)
print("Is my age not equal to: " + str(my_age) + " ? I predict False.")
print(my_age != 35)
print('-' * 40)
print("Is my age greater than: " + str(my_age) + " ? I predict False.")
print(my_age > 35)
print('-' * 40)
print("Is my age less than: " + str(my_age) + " ? I predict False.")
print(my_age < 35)
print('-' * 40)
print("Is my age greater than or equal to: " + str(my_age) + " ? I predict True.")
print(my_age >= 35)
print('-' * 40)
print("Is my age less than or equal to: " + str(my_age) + " ? I predict True.")
print(my_age <= 35)
print('-' * 40)


print("Conditional Test 3: \n")
print("Is my age: " + str(my_age) + " , greater than 21 and less than 49? I predict True.\n")
print((my_age > 21) and (my_age < 49))

print("Conditional Test 4: \n")
print("Is bmw x6 in the list dream_list? I predict True")
print('bmw x6' in dream_list)
print("Is nissan maxima in the list dream_list? I predict False.")
print('nissan maxima' in dream_list)
