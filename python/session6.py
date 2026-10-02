"""students = ("Heba", "Khaled", "Hajar", "Saeed", "Sara")
print("First student:", students[0])
print("Last student:", students[-1])
print("Number of students:", len(students))"""


"""t = (1,4,5,6,7)
print(len(t))

a, b, c, d, e = t
print(a, b, c, d, e)

list1 = [1, 2, 3, 4, 5]
set1 = set(list1)

set2 = {1,2,3,3,1,9,0,8,7,2,4,5}
print(set2)

set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8}
print("--------------------------------")
print(set3.union(set4))
print("--------------------------------")
print(set3|set4)
print("--------------------------------")
print(set3.intersection(set4))
print("--------------------------------")
print(set3&set4)
print("--------------------------------")
print(set3.difference(set4))
print("--------------------------------")
print(set3-set4)"""
"""
#1. Create a tuple of five student names and print the first and last name. 
students = ("Heba", "Khaled", "Hajar", "Saeed", "Sara")
print(students[0], students[-1])

#2. Create a tuple of coordinates and unpack it into x and y. 
coordinates = (10, 20)
x, y = coordinates  
print("x:", x)
print("y:", y)

#3. Count how many times the number 5 appears in a tuple. 
numbers = (1, 2, 3, 4, 5, 5, 6, 7, 5)
print(numbers.count(5))

#4. Find the index of 'Python' in a tuple. 
lan = ("Java", "C++", "Python", "JavaScript")
print(lan.index("Python"))"""

#5. Convert a list with duplicate values into a set. 
l = [1, 2, 2, 3, 4, 4, 5]
s = set(l)
print(s)

#6. Add a new item to a set. 
s.add(6)
print(s)

#7. Remove an item from a set. 
s.remove(3)
print(s)

#8. Find the union of two sets. 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

#9. Find the intersection of two sets. 
print(set1 & set2)

#10. Find the difference between two sets. 
print(set1 - set2)

#11. Check whether a value exists in a set. 
if 2 in set1:
    print("2 exists in set1")

#12. Create a program that removes duplicate names from user input.
names = input("Enter a list of names separated by commas: ").split(",") 
unique_names = set(names)
print(unique_names)

#1-tuple
#2-set
#3-()
#-No
#5-add()
#6-{1,2,3}
#7-intersection
#8-count()
#9-False
#10-False

#1
def unique_elements (numbers) :
  return set(numbers)
num=[1,2,3,2,4,4,5]
result= unique_elements (num)
print(result)

#2
A={10,30,5,4}
B={5,4,7,8}
print(A&B)

#3
rgb = (25, 30, 35)
for value in rgb:
    print(value)