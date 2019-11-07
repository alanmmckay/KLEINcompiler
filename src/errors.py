import sys
sys.tracebacklimit=0

class Error():
    def __init__(self, program):
        
        #Every error will need to be passed the program:
        #-this is accessed by the scanner's get_program_string method
        self.program_string = program
        self.error_message = "\n--\n"
        self.error_type = ""
        self.file_name = "error.txt"
        #error_string is manipulated by each subclass
        self.error_string = ""
        #output_string is only manipulated by this superclass
        self.output_string = ""
        #output represents the file to be written
        self.output = ""
    
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
        
    def throw_error(self):
        self.error_message +="\n--\nError log written to "+self.file_name
        raise ValueError(self.error_message)
    
    def output_error(self):
        self.open_file()
        self.write_file(self.error_string)
        self.close_file()
        self.throw_error()
        pass
#end class Error()


class GeneralError(Error):
    def __init__(self, msg, program):
        Error.__init__(self, program)
        self.error_message += msg
        self.error_string = msg
        self.output_error()
#end class GeneralError


class LexicalError(Error):
    def __init__(self, msg, program, position):
        Error.__init__(self, program)
        self.error_type = "SCANNER"
        self.file_name = "scanner_error.txt"
        self.error_message += msg
        self.error_string = msg
        self.error_string += "-> Input Program remaining to be scanned: \n"
        self.pos = position
        while self.pos < len(program):
            self.error_string += program[self.pos]
            self.pos += 1
        self.output_error()
#end class LexicalError

# errors thrown by the parser
class ParseError(Error):
    def __init__(self, msg, program, trace):
        Error.__init__(self,program)
        self.error_type = "PARSER"
        self.file_name = "parser_error.txt"
        self.error_message += msg
        self.error_string = msg
        self.error_string += "\n-> Parse Stack Trace: \n"
        self.error_string += trace 
        self.output_error()
#end class ParseError

# errors thrown by the type checker
class SemanticError(Error):
    def __init__(self, msg, program = ""):
        Error.__init__(self,program)
        self.error_type = "PARSER"
        self.file_name = "parser_error.txt"
        self.error_message += msg
        self.error_string = msg
        self.output_error()
