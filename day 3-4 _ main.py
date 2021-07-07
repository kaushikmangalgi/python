# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ap = add_pepperoni
ec = extra_cheese
bill = 0
if size == "S":
  bill = 15
  if ap == "Y":
    bill += 2

elif size == "M":
  bill = 20
  if ap == "Y":
    bill += 3
elif size == "L":
  bill = 25
  if ap == "Y":
    bill += 3
       
if ec == "Y":
  bill +=1
   
print(f"This is your final {bill}  ")






