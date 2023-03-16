number = int(input("Which number do you want to check? "))

divided_num = int(number % 2)

if divided_num == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
