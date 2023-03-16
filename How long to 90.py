age = input("What is your current age? ")

day = 1
week = 52
month = 12
year = day * 365

rest = 90 - int(age)

days = rest * year
weeks = rest * week
months = rest * month

message = f"You have {rest} year, {days} days, {weeks} weeks, and {months} months left until you're 90."
print(message)