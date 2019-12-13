from sys import argv, path
import os

path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/../../'))
path.insert(0, os.getcwd())

from src.parser import Parser
from src.scanner import Scanner
# have to import some sort of sem analyzer how ever we decide to do that
from src.code_generator import Generator


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

# gen = Generator(ast)

# get a tree
ast = p.parse()

# put that tree into generator objet
gen = Generator(ast)

# run code gen on the node
program = gen.generate()

#  output to a tm file
#FILE_PATH = FILE_PATH.strip(".kln")
FILE_PATH = FILE_PATH[0:-4]
filename = FILE_PATH + ".tm"
output = open(filename, "w")
output.write(program)
print("TM code saved to file {}".format(filename))

