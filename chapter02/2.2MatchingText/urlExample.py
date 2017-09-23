# Python matching urls

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:','https:','ftp')):
        return urlopen(name).read()
    else :
        with open(name) as f:
            return f.read()
