print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? (£) "))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_multiplier = 1+(tip_amount/100)
people = int(input("How many people are there to split the bill? "))
contribution = round((bill / people) * tip_multiplier, 2)
print(f"Each person should pay: £{contribution}")