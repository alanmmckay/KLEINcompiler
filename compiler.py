import sys
from scanner import Scanner
from k_token import Token

filename = sys.argv[1]
myfile = open(filename)
program = myfile.read()

scanner = Scanner(program)
