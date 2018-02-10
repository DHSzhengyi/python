#Finding the number of uppercase letters in a string

string = input("Enter word / sentence:")

import re

print(len(re.findall(r'[A-Z]',string)))
