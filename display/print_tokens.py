import sys
from src.scanner import Scanner

# make sure the file is where it is suppose to be
filename = sys.argv[1]

# read in prgm, turn to string
myfile = open(filename)
program = myfile.read()

# kick of scanner with prgm
s = Scanner(program)
token = s.get_next_token()

# while scanner gets tokens print out type and value
while True:
    for tokens in token:
        print(s.token.token_type, s.token.token_value)