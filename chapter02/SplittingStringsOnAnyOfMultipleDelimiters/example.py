#!/bin/python

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# Split a string with space
print(line.split())

# Split a string with different delimiters
result = re.split(r'[;,\s]\s*', line)
print(result)

fields = re.split(r'(,|;|\s)\s*', line)
print("fields :",  fields)

# Extended slicing is used here
#Syntax : list[start:end:step]
values = fields[::2]
print("values :", values)

# Extended slicing is used here
#Syntax : list[start:end:step]
delimiters = fields[1::2] + [' ']
print("Delimiter :",delimiters)

# reform the line using the delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))
