from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/../../'))
path.insert(0, os.getcwd())
from src.parser import Parser
from src.scanner import Scanner

# define file path
FILE_PATH = argv[1]

# turn prgm into a string and strip return off FILE_PATH
FILE_PATH = FILE_PATH.strip("\r")
with open(FILE_PATH, "r") as klein:
    klein_program = klein.read()

# run program through scanner
s = Scanner(klein_program)

# run s through parser
p = Parser(s)

result = p.parse()

if result:
    print("Program is valid")

    print("------------------------------------")
    print("|          Yep it works!           |")
    print("------------------------------------")
    print("""         \   ^__^
              \  (oo)\_______
                 (__)\       )\/
                     ||----w | \/
                     ||     ||""")