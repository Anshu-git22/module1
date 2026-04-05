file = open("string.txt", "w")

text = input("Enter a string: ")
file.write(text)
file.close()

print("You entered:", text)