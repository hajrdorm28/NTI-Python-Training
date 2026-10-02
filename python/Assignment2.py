"""#Task -----------------------------------------------------------
# 1. Employee Dictionary
employees = {
    101: "Ahmed Mahmoud",
    102: "Omar Ali",
    103: "Sara Hassan"
}

# 2. Product Dictionary
products = {
    "P001": 19.99,
    "P002": 49.50,
    "P003": 5.75
}

# 3. Phone Book
phone_book = {
    "Omar Yousef": "01012345678",
    "Sara Hassan": "01198765432",
    "Ali Mahmoud": "01234567890"
}

# 4. Frequency Counter
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency_counter = {} 
for num in numbers:
    frequency_counter[num] = frequency_counter.get(num, 0) + 1

# 5. Word Counter
text = "programming is fun and programming is useful"
word_counter = {}
for word in text.split():
    word_counter[word] = word_counter.get(word, 0) + 1

# 6. Student Management
student_grades = {
    2026001: 89.5,
    2026002: 92.0,
    2026003: 87.5
}

# 7. Inventory System
inventory = {
    "Laptop": 15,
    "Mouse": 50, 
    "Keyboard": 25
}

# 8. Library System
library_system = {
    "Introduction to Programming": 1112333, 
    "Database Systems": 1112334   
}

#Mini Project -----------------------------------------------------------
students = {}
# 1. Add Student Function
def add_student(s_id, name, age):
    students[s_id] = {"name": name, "age": age}

# 2. Search Student Function
def search_student(s_id):
    return students.get(s_id, "Not found")

# 3. Update Student Function
def update_student(s_id, new_name, new_age):
    if s_id in students:
        students[s_id] = {"name": new_name, "age": new_age}

# 4. Delete Student Function
def delete_student(s_id):
    students.pop(s_id, None)

# 5. Display Students Function
def display_students():
    for s_id, info in students.items():
        print(f"ID: {s_id}, Name: {info['name']}, Age: {info['age']}")

add_student("101", "Ali", 20)
add_student("102", "Sara", 22)

print("Search 101:", search_student("101"))

update_student("101", "Ali Hassan", 21)
delete_student("102")
display_students()
"""


st_manage = {
    "Habiba" : "A",
    "Mohamed" : "B", 
    "Sarah" : "C"
}
name = input("Enter student name: ")
if name in st_manage:
    value = st_manage[name]
    if value == "A":
        print("Excellent")  
    else:
        print("Fail")
else:
    print("Student not found")