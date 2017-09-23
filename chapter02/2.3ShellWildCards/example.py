# Matching Strings using Shell wildcard patterns

from fnmatch import fnmatch, fnmatchcase

fnmatch('sample.txt','*.txt')
fnmatch('sample.txt','?ample.txt')
fnmatch('Data45.csv','Data[0-9]*.csv')
names =['Dat1.csv','Dat2.csv','config.xml','foo.py']

print([name for name in names if fnmatch(name,'*.csv')])

# If the case is important then use fnmatchcase() function

fnmatchcase('foo.txt','*.TXT')  # false
fnmatchcase('TEST.txt','*.txt') # true

address = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in address if fnmatch(addr,'* ST')])
print([addr for addr in address if fnmatch(addr,'54[0-9][0-9] *CLARK*')])