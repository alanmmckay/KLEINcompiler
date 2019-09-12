import sys
from src.scanner import Scanner

filename = sys.argv[1]
myfile = open(filename)
program = myfile.read()

scanner = Scanner(program)
