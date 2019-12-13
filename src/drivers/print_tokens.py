from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/../../'))
path.insert(0, os.getcwd())
from src.scanner import Scanner

# define file path
FILE_PATH = argv[1]

# turn prgm into a string and strip return off FILE_PATH
FILE_PATH = FILE_PATH.strip("\r")
with open(FILE_PATH, "r") as klein:
    klein_program = klein.read()

# run program through scanner
s = Scanner(klein_program)

# go through all tokens in the file
while True:
    tokens = s.get_next_token()
    if tokens.__repr__() == "end_of_stream":
        print(tokens.__repr__())
        break
    else:
        print(tokens.__repr__())
