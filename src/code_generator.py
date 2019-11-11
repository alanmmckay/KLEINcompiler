class Generator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        program = self.ast.code_gen()
        return program
