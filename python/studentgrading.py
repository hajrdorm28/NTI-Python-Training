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