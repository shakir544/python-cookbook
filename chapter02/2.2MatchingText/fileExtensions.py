# Python program to find the extensions of files in the current directory
import os
import logging

logging.basicConfig(filename='fileExtensions.log',level=logging.DEBUG)
# list the files/dirs in the current directory
file_names = os.listdir('.')
files_with_extensions = [name for name in file_names if name.endswith(('.cpp','java'))]
logging.info(files_with_extensions)
tuple_with_py = any(name.endswith('.py') for name in file_names)
logging.info(tuple_with_py)

