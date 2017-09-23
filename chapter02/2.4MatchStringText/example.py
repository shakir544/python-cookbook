# Matching and searching for Text Patterns
import re

text = 'yeah, but no, but yeah, but no, but yeah'

# excat match
text == 'yeah'

# using startswith
text.startswith('yeah')
# using endswith
text.endswith('no')

# Search for the location of first occurance
text.find('no')

# for more complicated searching use regular expression
text1= '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+',text1):
    print("Yes")
else :
    print("No")

if re.match(r'\d+/\d+/\d+',text2):
    print("Yes")
else :
    print("No")

# Recompile the regular expression
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print("Yes")
else :
    print("No")

