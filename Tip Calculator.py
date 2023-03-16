print("Welcome to the tip calculator! \n")
bill = input("What was the total bill? $")
tip_per = input("What percentage tip would you like to give? %")
people = input("How many people to split the bill? ")

tip_total = float(tip_per) / 100 * float(bill)
tip_result = float(tip_total) / float(people)

pay = float(bill) / float(people) + float(tip_result)

result = round(pay, 2)

result = "{:.2f}".format(pay)

print(" ")
print(f"Each person shoult pay ${result}")

