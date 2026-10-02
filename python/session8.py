"""# 1. Create a student dictionary (name, age, grade). 
student = {
    "name": "Hajar",
    "age": 20,
    "grade": 85
}

# 2. Update the student's grade. 
student["grade"] = 90

# 3. Add city and phone number. 
student["city"] ="Cairo"
student["phone"] = "0123456789"
print(student)

# 4. Delete the city key. 
del student["city"]

# 5. Print all keys, values, and items. 
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# 6. Search for a key using get(). 
grade = student.get("grade")
print("Grade:", grade)

# 7. Create a phone book dictionary. 
phone_book = {
    "Sara": "0123456789",
    "Mona": "0123456789",
    "Amany": "0123456789"
}

# 8. Count frequency of numbers using a dictionary. 
numbers = [1, 2, 3, 2, 1, 3, 1]
count = {}
for n in numbers:
    count[n] = count.get(n, 0) + 1
print("Frequency of numbers:", count)

# 9. Count frequency of characters in a string. 
text = "hello"
char_frequency = {}
for char in text:
    char_frequency[char] = char_frequency.get(char, 0) + 1
print("Frequency of characters:", char_frequency)

# 10. Find the student with the highest grade. 
highest_student = max(student, key=student.get)
print("Student with highest grade:", highest_student)

# 11. Create a product dictionary and calculate total price. 
products = {
    "apple": 1.2,
    "banana": 0.8,
    "orange": 1.5
}
total_price = sum(products.values())
print("Total price:", total_price)

# 12. Merge two dictionaries. 
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(dict1 | dict2)
# merged_dict = {**dict1, **dict2}
# print("Merged dictionary:", merged_dict)

# 13. Check if a key exists before accessing it. 
if "name" in student:
    print("Name:", student["name"])

# 14. Create a nested dictionary for 3 students. 
students = {
    "student1": {"name": "Hajar", "age": 20, "grade": 90},
    "student2": {"name": "Sara", "age": 22, "grade": 85},
    "student3": {"name": "Mona", "age": 21, "grade": 88}
}
# 15. Print all student names from the nested dictionary
for student in students.values():
    print("Student name:", student["name"])

for i in students:
    print(students[i]["name"])"""

