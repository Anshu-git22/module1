import re

text = "I am learning Python at Tops Technologies"

word = input("Enter word to search: ")

result = re.search(word, text)

if result:
    print("Word found!")
else:
    print("Word not found")