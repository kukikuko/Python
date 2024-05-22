#Day 2 Project - Tip Calculator

#==============================================================

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = float(input("What was hte total bill? $"))
tip_rate = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_rate  = 1 + (tip_rate / 100)
pay = bill * tip_rate / people

print(f"Each person should pay: ${pay:.2f}")
