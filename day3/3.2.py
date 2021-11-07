# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h2 = float(height)**2
bmi = int(float(weight) / h2)

print(bmi)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight")
elif 18.5 < bmi < 25:
  print(f"Your bmi is {bmi}, you are normal weight")
elif 25 < bmi < 30:
  print(f"Your bmi is {bmi}, you are slightly overweight")
elif 30 < bmi < 35:
  print(f"Your bmi is {bmi}, you are overweight")
elif bmi > 35:
  print(f"Your bmi is {bmi}, you are clinically obese")