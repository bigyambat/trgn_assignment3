#!/user/bin/python

import re
file = open("mytextfile.txt")
text = file.read()

pattern1 = r"\d{3}-\d{3}-\d{4}"
pattern2 = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"

phone_number_pattern1 = re.findall(pattern1, text)
phone_number_pattern2 = re.findall(pattern2, text)


print(phone_number_pattern1)
print(phone_number_pattern2)

import re

file = open("mytextfile.txt")
text = file.read()

pattern1 = r"\d{3}-\d{3}-\d{4}"
pattern2 = r"+\d{2}-\d[{2}-\d{4}-\d{4}"

phone_number_pattern1 = re.findall(pattern1, text)

print(phone_number_pattern1) 
        




