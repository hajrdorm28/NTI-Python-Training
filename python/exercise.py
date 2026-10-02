with open("employees.txt", "w") as file:
    file.write("Khaled\nSara\nAhmed\nAli\n")

search_name = "Khaled"
with open("employees.txt", "r") as file:
    found = False
    for line in file:
        if search_name in line:
            found = True
            break
print(found)

fl = open("employees.txt", "r")
data = fl.read()
with open("backup.txt", "w") as copy_file:
    copy_file.write(data)

file1 = open("student.txt", "r")
file2 = open("names.txt", "r")
data1 = file1.read()
data2 = file2.read()
with open("merged_copy.txt", "w") as merged:
    merged.write(data1 + data2)

content = open("merged_copy.txt", "r")
content = content.read()
print(content.upper())

temp = open("student.txt", "r").readlines()
i = 1
for line in temp:
    print(i, line.strip())
    i += 1

lines = open("student.txt", "r").readlines()
longest = lines[0]
for line in lines:
    if len(line) > len(longest):
        longest = line
print(longest)
 
shortest = lines[0]
for line in lines:
    if len(line) < len(shortest):
        shortest = line
print(shortest)
 

src = open("student.txt", "r")
with open("student_copy.txt", "w") as dst:
    dst.writelines(line for line in src if line.strip())

new_content = content.replace("Khaled", "John")
with open("student_new.txt", "w") as f:
    f.write(new_content)