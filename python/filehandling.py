#file creation
with open("student.txt", "w") as file:
    file.write("""Ali 
    sama 
    Mariam """)

file = open("student.txt", "a")
file.write("Alaa")
file.close()
file = open("student.txt", "r")
print(file.read())
file.close()

# checking if file exists
import os
if os.path.exists("student.txt"):
    print("File exists")


#Lab
# Write names to file
with open("names.txt", "w") as file:
    file.write("Ali\nSama\nMariam\n")

# Read and display content
file = open("names.txt", "r")
print("Initial Content:")
print(file.read())
file.close()

# Append new data
file = open("names.txt", "a")
file.write("Alaa\n")
file.close()

# Display updated content
file = open("names.txt", "r")
print("Updated Content:")
print(file.read())
file.close()

# Read lines into a list to count lines and words
file = open("names.txt", "r")
lines = file.readlines()
file.close()

print("Line count:", len(lines))

# Read whole text to count words
file = open("names.txt", "r")
text = file.read()
file.close()

words = text.split()
print("Word count:", len(words))

# Read from original file
file1 = open("names.txt", "r")
content = file1.read()
file1.close()

# Write into a copy file
file2 = open("names_copy.txt", "w")
file2.write(content)
file2.close()

print("File copied successfully")