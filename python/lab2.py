def sub(x, y):
    num1= float(input("Enter first number: "))
    num2= float(input("Enter second number: "))
    print(num1 - num2)
sub(0, 0)

def sqr(x):
    num= float(input("Enter a number: "))
    print(num ** 2)
sqr(0)


def cube(x):
    num= float(input("Enter a number: "))
    print(num ** 3)
cube(0)

def even(x):
    num= float(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
even(0)

def max(x, y):
    num1= float(input("N1: "))
    num2= float(input("N2: "))
    if num1 > num2:
        print(num1)
    else:
        print(num2)
max(0, 0) 

def trial(*nums):
    print(nums) 
trial(1, 2, 3, "n", 5)






student = ["yousef","hager","ahmed","fatma"]
student.append("khaled")
student.remove("hager")
print(student)
for i in student:
    print(i)


grades = [10,60,70,80]
def add_grade(grade):
    grades.append(grade)

def remove_grade(grade):
    if grade in grades:
        grades.remove(grade)
    else:
        print("Grade not found.")

def print_grades():
    print("Grades:", grades)

def calculate_average():
    if grades:
        avg = sum(grades) / len(grades)
        print("Average: ",avg)
    else:
        print("No grades to calculate average.")

def find_highest_grade():
    if grades:
        print("Highest: ", max(grades))
    else:
        print("No grades found.")

print_grades()
calculate_average()
find_highest_grade()

remove_grade(10)
print_grades()