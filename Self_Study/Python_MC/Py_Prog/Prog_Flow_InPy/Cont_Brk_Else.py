# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#         # break is used to stop processing any more lines in the block of code; it essentially exits the 'for loop' and any value in the sequence
#         # that follows is not executed.
#         # continue
#         # continue stops processing any more lines in the block of code and forces the 'for loop' to move on to the next value in the sequence
#     print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages"]

nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")
if nasty_food_item:
        print("Cant I have anything without spam in it? ")