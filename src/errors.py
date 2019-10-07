import sys
#sys.tracebacklimit=0

class GeneralError():
    def __init__(self, program):
        self.error_type = ""
        self.file_name = "error.txt"
        self.program_string = program
        self.error_string = "General Error"
        self.output_string = ""
        self.output = ""
        self.error_message = "General Error Thrown!"
    
    def open_file(self):
        self.output = open(self.file_name, "w")
        
    def write_file(self, error):
        self.output_string = "!--- "+self.error_type+" ERROR! ---!\n\n\n"
        self.output_string += "---> Input Program: \n"
        self.output_string += self.program_string
        self.output_string += "\n\n\n---> Error Information: \n"
        self.output_string += error
        self.output.write(self.output_string)
        
    def close_file(self):
        self.output.close()
        
    def throw_error(self, msg):
        raise ValueError(msg)
    
    def output_error(self):
        self.open_file()
        self.write_file(self.error_string)
        self.close_file()
        self.throw_error(self.error_message)
        pass

class LexicalError(GeneralError):
    def __init__(self, msg, program, position):
        GeneralError.__init__(self, program)
        self.error_type = "SCANNER"
        self.file_name = "scanner_error.txt"
        self.error_string = "-> Input Program remaining to be scanned: \n"
        self.error_message = msg
        self.pos = position
        while self.pos < len(program):
            self.error_string += program[self.pos]
            self.pos += 1
        self.output_error()
        

# errors thrown by the parser
class ParseError(ValueError):
    pass


# errors thrown by the type checker
class SemanticError(ValueError):
    pass
