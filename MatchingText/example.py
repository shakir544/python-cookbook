# Matching Text starts with and ends with

filename = "spam.txt"
filename.endswith('.txt')

if filename.endswith('.txt') :
    print("yes it ends with .txt")

if filename.startswith('file:'):
    print("yes filename starts with file:")
else:
    print("No the filename:",filename )

url = 'http://python.org'
url.startswith('http')