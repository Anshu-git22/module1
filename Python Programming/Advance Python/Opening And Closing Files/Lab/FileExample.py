f1 = open("Data_file.txt", "w")
f1.write("Hello, this is a sample data file..")
f1.close()

f1=open("Data_file.txt", "r")
data = f1.read()
print(data)
f1.close()