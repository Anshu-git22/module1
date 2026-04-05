file = open("students.txt", "w")

file.write("Name: Raj, Phone: 9876543210\n")
file.write("Name: Prit, Phone: 9123456780\n")
file.write("Name: Rahul, Phone: 9988776655\n")

file.close()

file = open("students.txt", "r")

data = file.read()
print("Student Contacts:")
print(data)

file.close()