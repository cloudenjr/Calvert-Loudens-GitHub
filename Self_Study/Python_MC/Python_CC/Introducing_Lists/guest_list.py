guest_list = ["Barack Obama", "Ronaldinho", "Joan of Ark", "Alana Aaron"]

for guest in guest_list[0:4]:
    print(guest + " I'd like to invite you over for dinner at my place. Say, seven o'clock?\n".format(guest_list[0:4]))

print(guest_list[0] + " says that he cannot attend and is truly sorry.\n")

del guest_list[0]
guest_list.insert(0, 'Bob Marley')

print(guest_list)

for guest in guest_list[0:4]:
     print(guest + " I'd like to invite you over for dinner at my place. Say, seven o'clock?\n")

print("I've found a bigger table and can invite 3 more guests! Whooo hoooo.\n")

guest_list.insert(0, 'Messi')
guest_list.insert(2, 'Iniesta')
guest_list.append('Xavi')

print(guest_list)

for guest in guest_list[0:8]:
    print(guest + " I'd like to invite you over for dinner at my place. Say, seven o'clock?\n")

print("I have bad news everyone. My new table wont arrive in time for dinner to accommodate everyone. Im forced"
      " to only invite two people to dinner. Again, I am truly sorry for the inconvenience.")

for guest in guest_list[0:8]:
    if guest == 'Ronaldinho' or 'Bob Marley':
        print("Sorry for the mixup, " + guest + " but you are still invited to dinner, if you can make it?\n")
    else:
        print("Sorry for the inconvenience, but we'll have to schedule dinner together another time.")
        guest_list.pop(0,8)
