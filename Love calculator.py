print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = name1.lower() + name2.lower()
trueall = true.count("t") + true.count("r") + true.count("u") + true.count("e")

love = name1.lower() + name2.lower()
loveall = love.count("l") + love.count("o") + love.count("v") + love.count("e")

result = int(f"{trueall}{loveall}")

if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
    
elif result >= 40 and result <=50:
    print(f"Your score is {result}, you are alright together.")

else:
    print(f"Your score is {result}.")
    
