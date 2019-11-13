class Generator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        line = 0
        program = self.ast.code_gen(line)
        return program
