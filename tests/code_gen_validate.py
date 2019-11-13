from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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

gen = Generator(ast)

program = gen.generate()

print()
print("program being returned in code_gen_validate")
print(program)
print()

# for now I will output my trusty message cow!
# print("------------------------------------")
# print("| This is not yet finished!        |")
# print("------------------------------------")
# print("""         \   ^__^
#           \  (oo)\_______
#              (__)\       )\/
#                  ||----w | \/
#                  ||     ||""")
