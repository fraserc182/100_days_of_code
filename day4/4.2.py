# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

items_in_list = len(names)

random_int = random.randint(0, items_in_list)

print(f"{names[random_int]} has to pay the bill tonight.")