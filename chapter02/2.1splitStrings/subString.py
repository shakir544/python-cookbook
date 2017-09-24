# find the sub String from a string
import re

string, sub_string = input().strip(), input().strip()

print(len(re.findall(sub_string,string)))


for i in range(len(string) - len(sub_string)+1):
    if string[i:len(sub_string)-1] == sub_string:
        sum +=1
print(sum)