#if condition
# 1. Write a program that checks whether a number is positive, negative, or zero. 
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# 2. Write a program that checks whether a number is even or odd. 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# 3. Ask the user for their age. Print whether they are eligible to vote (age 18 or above). 
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# 4. Write a program that asks for two numbers and prints the larger number. 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("Larger number:", a)
else:
    print("Larger number:", b)
# 5. Write a program that asks for three numbers and prints the largest one. 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
# 6. Ask the user for a student's grade and print: A for 90+, B for 80–89, C for 70–79, D for 60–69, and F below 60. 
grade = float(input("Enter student's grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
# 7. Write a program that checks whether a given year is a leap year. 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# 8. Ask the user for a username and password. Print 'Login Successful' only if both are correct.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed") 
# 9. Write a program that checks whether a number is divisible by both 3 and 5. 
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5.")
else:
    print(num, "is not divisible by both 3 and 5.")
# 10. Write a program that calculates a discount: if the price is greater than or equal to 1000, give 20% discount; otherwise give 10%.
price = float(input("Enter the price: "))
if price >= 1000:
    discount = price * 0.20
else:
    discount = price * 0.10
final_price = price - discount
print("Discount:", discount)
print("Final Price:", final_price)


#for loop
# 11. Print the numbers from 1 to 10 using a for loop. 
for i in range(1, 11):
    print(i)
# 12. Print all even numbers from 2 to 20 using a for loop. 
for i in range(2, 21, 2):
    print(i)
# 13. Print all odd numbers from 1 to 19 using a for loop. 
for i in range(1, 20, 2):
    print(i)
# 14. Ask the user for a number n and print numbers from 1 to n. 
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)
# 15. Calculate and print the sum of numbers from 1 to 100. 
sum = 0
for i in range(1, 101):
    sum += i
print("Sum:", sum)
# 16. Ask the user for a number and print its multiplication table from 1 to 12. 
num = int(input("Enter a number: "))
for i in range(1, 13):
    print(num, "x", i, "=", num * i)
# 17. Count how many numbers between 1 and 100 are divisible by 7. 
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("Count:", count)
# 18. Print the square of every number from 1 to 10. 
for i in range(1, 11):
    print(i ** 2)
# 19. Ask the user for 5 numbers and calculate their total sum. 
total = 0
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    total += num
print("Total sum:", total)
# 20. Find the largest number in a list using a for loop without using max().
numbers = [23, 67, 12, 89, 45, 90, 5]  # example list
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("List:", numbers)
print("Largest number:", largest)
#While loop
# 21. Print numbers from 1 to 10 using a while loop. 
i = 1
while i <= 10:
    print(i)
    i += 1
# 22. Print numbers from 10 down to 1 using a while loop. 
i = 10
while i >= 1:
    print(i)
    i -= 1
# 23. Ask the user for a positive number. Keep asking until they enter a positive number.
num = float(input("Enter a positive number: "))
while num <= 0:
    print("That's not positive. Try again.")
    num = float(input("Enter a positive number: "))
print("Thank you! You entered:", num)
# 24. Create a program that keeps asking the user to enter a password until the correct password is entered. 
correct_password = "python123"
password = input("Enter password: ")
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter password: ")
print("Access Granted!")
# 25. Calculate the sum of numbers from 1 to n using a while loop.
n = int(input("Enter a number n: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of 1 to {n} is:", total) 
# 26. Count the number of digits in an integer using a while loop. 
num = int(input("Enter an integer: "))
count = 0
temp = abs(num)
if temp == 0:
    count = 1
while temp > 0:
    temp //= 10
    count += 1
print("Number of digits:", count)
# 27. Create a simple guessing game. The program stores a secret number, and the user keeps guessing until they find it.
import random
secret = random.randint(1, 100)
guess = None
while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it!") 
# 28. Ask the user to enter numbers repeatedly. Stop when they enter 0, then print the sum of all entered numbers.
total = 0
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum of all entered numbers:", total)

#Nested loops
# 29. Use nested loops to print a 5 × 5 square of stars. 
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
# 30. Print the following pattern using nested loops: * ** *** **** ***** 
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print() 
# 31. Print a multiplication table from 1 to 5 using nested loops. 
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()
# 32. Print this pattern: 1 12 123 1234 12345
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Mixed challenges
# 33. Write a program that prints all prime numbers between 1 and 100. 
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
# 34. Write a program that asks for a number and determines whether it is prime. 
num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not prime.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
# 35. Ask the user for 10 numbers and count how many are positive, negative, and zero.
positives = 0
negatives = 0
zeros = 0

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1

print(f"Positive numbers: {positives}")
print(f"Negative numbers: {negatives}")
print(f"Zeros: {zeros}") 
# 36. Create a program that calculates the factorial of a number using a loop. 
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
# 37. Write a program that reverses a number using a while loop. Example: 1234 → 4321. 
num = int(input("Enter an integer: "))
original_num = num
reversed_num = 0
num = abs(num)
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10
if original_num < 0:
    reversed_num = -reversed_num
print(f"Reversed number: {reversed_num}")
# 38. Create a simple ATM menu using a while loop: 1-Check Balance, 2-Deposit, 3-Withdraw, 4-Exit. 
balance = 3000.0
while True:
    print("--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ${balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount.")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. Remaining balance: ${balance:.2f}")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please pick between 1 and 4.")
# 39. Write a program that asks for a student's name and 3 grades, calculates the average, and prints Pass if the average is at least 50; otherwise Fail. 
name = input("Enter student name: ")
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
average = (grade1 + grade2 + grade3) / 3
print(f"Student: {name}")
print(f"Average Grade: {average:.2f}")
if average >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")
# 40. Challenge: Create a number guessing game with a maximum of 5 attempts. Print whether the user won or lost.
import random
target_number = random.randint(1, 100)
attempts_left = 5
won = False
print("Guess the secret number between 1 and 100! You have 5 attempts.")
while attempts_left > 0:
    guess = int(input(f"\nAttempts remaining ({attempts_left}): Enter your guess: "))
    
    if guess == target_number:
        won = True
        break
    elif guess < target_number:
        print("Too low!")
    else:
        print("Too high!")
        
    attempts_left -= 1

if won:
    print(f"\nCongratulations! You guessed the correct number: {target_number}")
else:
    print(f"\nGame Over! You've used all attempts. The secret number was {target_number}.")

#Bonus
# 41. Find and fix the error: for i in range(1, 10) print(i) >>> for i in range(1, 10): print(i)
# 42. Find and fix the error: if age >= 18 print('Adult') >>> if age >= 18: print('Adult')
# 43. What is wrong with this code? while x < 10: print(x) Explain why it may become an infinite loop. >>> there is no condition to stop 
# 44. What will be the output? for i in range(3): print(i) >>> 0 1 2
# 45. What will be the output? for i in range(2, 10, 2): print(i) >>> 2 4 6 8