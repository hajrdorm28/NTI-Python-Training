#1
student = ("Hajar", 101, "CS")
print("Student:", student)
#2
employee = ("Sarrah", 2001, 75000)
print("Employee Name:", employee[0])
#3
names = ["Khaled", "Ahmed", "Ali", "Ali", "Khaled"]
names = (set(names))
print("Unique names:", names)

a = {1, 2, 3}
b = {3, 4, 5}
#4
print("Union:", a | b)
#5
print("Intersection:", a & b)
#6
print("Difference:", a - b)
#7
movies = {"Inception", "Interstellar", "The Dark Knight","Mary & Max"}
print("Favorite Movies List: ", movies)
#8
math_cs = {"Math", "Data Structures"}
networks_cs = {"Math", "Networks"}
print("Shared subjects:", math_cs & networks_cs)
print("All subjects:", math_cs | networks_cs)