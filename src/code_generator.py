class Generator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        line = 0
        program = self.ast.code_gen(line)
        program_str = ''

        for line_num, stmt in enumerate(program):
            program_str += str(line_num) + ': ' + stmt + '\n'

        return program_str
