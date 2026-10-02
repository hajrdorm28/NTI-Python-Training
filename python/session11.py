"""class Books:
    pass
    
book1.title = "The Great Gatsby"
book1.author = "F. Scott Fitzgerald"
book1.year = 1925

print(book1.title)  # Output: The Great Gatsby 
print(book1.author)  # Output: F. Scott Fitzgerald
print(book1.year)  # Output: 1925   
"""

"""class Books:
    def __init__(self, title="", author="", year=0):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")

    def get_year(self):
        return self.year

book1 = Books("No Longer Human", "Osamu Dazai", 2018)
book1.display_info() 

book2 = Books("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2.display_info()

book3 = Books("1984", "George Orwell", 1949)
book3.display_info()


class Employee:
    def __init__(a, name="", department="", salary=0):
        a.name = name
        a.department = department
        a.salary = salary

    def display_info(a):
        print(f"Name: {a.name}")
        print(f"Department: {a.department}")
        print(f"Salary: ${a.salary}")

    def get_salary(a):
        return a.salary

emp1 = Employee("Alice Johnson", "HR", 60000)
emp1.display_info()


class Calculator:
    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")

calc = Calculator()
calc.add(10, 5)

class Rectangle:
    def area(self, length, width):
        print(length * width)

rect = Rectangle()
rect.area(2, 4)"""

class BankAccount:
    def __init__(self, owner="", balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Error: Insufficient funds")

    def display_balance(self):
        print(f"Owner: {self.owner}, Balance: ${self.balance}")

account = BankAccount("John Doe", 1000)




print(type(account))

