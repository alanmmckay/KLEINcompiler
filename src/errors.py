import sys
#sys.tracebacklimit=0

# errors thrown by the scanner
class LexicalError():
    def __init__(self, msg, position, program):
        self.output_string = "!--- SCANNER ERROR! ---!\n\n\n"
        self.output_string += "---> Input Program: \n"
        self.output_string += program + "\n\n\n"
        self.output_string += "---> Input Program remaining to be scanned: \n"
        self.pos = position
        while self.pos < len(program):
            self.output_string += program[self.pos]
            self.pos += 1
        self.output = open("scanner_error.txt", "w")
        self.output.write(self.output_string)
        self.output.close()
        raise ValueError(msg)
    pass


# errors thrown by the parser
class ParseError(ValueError):
    pass


# errors thrown by the type checker
class SemanticError(ValueError):
    pass
