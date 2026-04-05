import re

text = "Tops Technologies"

word = input("Enter word to match: ")

result = re.match(word, text)

if result:
    print("Word matched at the beginning!")
else:
    print("No match")