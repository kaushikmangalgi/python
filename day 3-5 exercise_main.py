# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cs = name1 + name2
lc_name = cs.lower()
t = lc_name.count("t")
r = lc_name.count("r")
u = lc_name.count("u")
e = lc_name.count("e")
true = t + r + u + e
l = lc_name.count("l")
o = lc_name.count("o")
v = lc_name.count("v")
e = lc_name.count("e")
love = l + o + v + e
tlcal = int(str(true) + str(love))
if tlcal <10 and tlcal >90:
  print(f"Your score is {tlcal}, you go together like coke and mentos.")
elif tlcal >=40 and tlcal <=50:
  print(f"Your score is {tlcal}, you are alright together.")
else:
  print(f"Your score is {tlcal}")


