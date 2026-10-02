import math
import random


"""radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

area2 = math.pi * math.pow(radius, 2)


colors = ["red", "green", "blue", "yellow", "orange"]
random_color = random.choice(colors) 
print(random_color)

def toss_coin():
    return random.choice(["Heads", "Tails"])

def roll_dice():
    return random.randint(1, 6)

while True:
    user_input = input("Enter '1' to toss a coin, '2' to roll a dice or '3' to quit: ")
    if user_input == "1":
        print(toss_coin())
    elif user_input == "2":
        print(roll_dice())
    elif user_input == "3":
        print("Quitting...")
        break
    else:
        print("Invalid input. Please try again.")
"""

# 1. Find the square root of 121 
print("Square root of 121:", math.sqrt(121))

# 2. Find the square root of 196 
print("Square root of 196:", math.sqrt(196))

# 3. Find the square root of 400 
print("Square root of 400:", math.sqrt(400))

# 4. Find 2^5 using math.pow() 
print("2^5:", math.pow(2, 5))

# 5. Find 3^4 using math.pow() 
print("3^4:", math.pow(3, 4))

# 6. Find 10^2 using math.pow() 
print("10^2:", math.pow(10, 2))

# 7. Find the factorial of 5 
print("Factorial of 5:", math.factorial(5))

# 8. Find the factorial of 7 
print("Factorial of 7:", math.factorial(7))

# 9. Find the factorial of 8 
print("Factorial of 8:", math.factorial(8))

# 10. Print math.pi 
print("Value of π:", math.pi)

# 11. Generate a random number from 1 to 10 
print("Random number from 1 to 10:", random.randint(1, 10))

# 12. Generate a random number from 1 to 100 
print("Random number from 1 to 100:", random.randint(1, 100))

# 13. Generate a random number from 50 to 80 
print("Random number from 50 to 80:", random.randint(50, 80))

# 14. Choose a random color 
print("Random color:", random.choice(["red", "green", "blue", "yellow", "orange"]))

# 15. Choose a random fruit 
print("Random fruit:", random.choice(["apple", "banana", "cherry", "date", "elderberry"]))

# 16. Choose a random day 
print("Random day:", random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]))

# 17. Simulate a dice roll 
print("Dice roll:", random.randint(1, 6))

# 18. Simulate a coin toss 
print("Coin toss:", random.choice(["Heads", "Tails"]))

# 19. Generate five random numbers 
print("Five random numbers:", [random.randint(1, 100) for x in range(5)])

# 20. Generate ten random numbers 
print("Ten random numbers:", [random.randint(1, 100) for y in range(10)])

# 21. Ask the user for a number and print its square root 
number1 = float(input("Enter a number: "))
print("Square root of", number1, "is", math.sqrt(number1))

# 22. Ask the user for a number and print its factorial 
number2 = int(input("Enter a number: "))
print("Factorial of", number2, "is", math.factorial(number2))

# 23. Generate a lucky number 
print("Lucky number:", random.randint(1, 100))

# 24. Create a random password digit 
print("Random password digit:", random.randint(0, 9))

# 25. Generate a random month 
print("Random month:", random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]))

# 26. Find area of a circle using math.pi 
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("Area of the circle:", area)

# 27. Generate three random colors 
print("Three random colors:", [random.choice(["red", "green", "blue", "yellow", "orange"]) for n in range(3)])

# 28. Generate three random fruits 
print("Three random fruits:", [random.choice(["apple", "banana", "cherry", "date", "elderberry"]) for m in range(3)])

# 29. Print square roots from 1 to 10 
for i in range(1, 11):
    print(f"Square root of {i}: {math.sqrt(i)}")

# 30. Create a lottery number generator
print("Lottery numbers:", [random.randint(1, 50) for s in range(6)])


char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = ""
for i in range(12):
    password += random.choice(char)
print("Random password: ", password)
