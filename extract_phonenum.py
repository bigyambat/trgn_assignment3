#!/usr/bin/python
import re
import sys 

#Now using sys to allow user to specify file 

file = open('mytextfile.txt', 'r')
phone_nums = file.read()

phone_pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

pulled_nums = re.findall(phone_pattern, phone_nums)

#print(pulled_numbs)

for each_num in pulled_nums:
    print(each_num)   
