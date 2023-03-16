print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if size == "S".lower():
    bill += 15
elif size == "M".lower():
    bill += 20
elif size == "L".lower():
    bill += 25
    
if add_pepperoni == "Y".lower():
    if size == "S".lower():
        bill += 2
    elif size == "M".lower():
        bill += 3
    elif size == "L".lower():
        bill += 3
if extra_cheese == "Y".lower():
    bill += 1
print(f"Your final bill is: ${bill}")