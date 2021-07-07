# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2)
print(round(BMI, 2))
if BMI <= 18.5:
  print("A very good suggestion is you have to gain weight")
elif BMI <= 25:
  print("You are underweight!")
elif BMI <= 30:
  print("You have maintained your weight")
elif BMI <=35:
  print("Yayy,You are fit and healthy!!")
else:
  print("Check if you are obese")




