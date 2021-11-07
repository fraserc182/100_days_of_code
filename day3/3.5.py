# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1.lower() + name2.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true_score = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love_score = l + o + v + e

true_love_score = str(true_score) + str(love_score)

if int(true_love_score) < 10 or int(true_love_score) > 90 :
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif 40 < int(true_love_score) < 50:
  print(f"Your score is {true_love_score}, you are alright together.")
else:
  print(f"Your score is {true_love_score}")