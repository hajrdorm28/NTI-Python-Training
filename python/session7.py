"""student = {
    "name": "Hajar",
    "age": 20,
    "grade": "A"
}
student["grade"] = "A+"
student["city"] = "Cairo"
student["p_number"] = "123456789"

print(student)"""
"""
# 1. Create a student dictionary
student = {
    "name": "Ali",
    "age": 20,
    "city": "Cairo"
}

# 2. Update age
student["age"] = 21

# 3. Add email
student["email"] = "ali@gmail.com"

# 4. Delete city
del student["city"]

# 5. Print keys
student.keys()

# 6. Print values
student.values()

# 7. Print all items
student.items()
"""
# 8. Count frequency of characters in a string
text = "hello"
freq = {char: text.count(char) for char in set(text)}
print("Character frequency:", freq)

string = "Hello"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")

"""
char : text.count(char)
h : 1
e : 1
l : 2
o : 1
store them in a dictionary then convert it to a list of tuples and print the result
"""