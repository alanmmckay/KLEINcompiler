from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.scanner import Scanner

# set file path
FILE_PATH = argv[1]

# turn prgm into a string
FILE_PATH = FILE_PATH.strip("\r")
with open(FILE_PATH, "r") as klein:
    klein_program = klein.read()

# run program on scanner and get token
s = Scanner(klein_program)
tokens = s.get_next_token()

#go through all tokens in the file
while True:
    if tokens.__repr__() == "end_of_stream":
        print(tokens.__repr__())
        break
    else:
        print(tokens.__repr__())
        tokens = s.get_next_token()