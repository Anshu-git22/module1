file = open("Str.txt", "w")

strings = ["Hello", "Welcome", "Python", "Programming"]

for s in strings:
    file.write(s + "\n")

file.close()