from src.scanner import Scanner
from src.errors import ParseError
from src.parse_table import NonTerminal, Terminal, StaticTerminal, parse_table
from src.k_token import Token, TokenType


def top(stack):
    return stack[-1]


def pop(stack):
    stack.pop()


def push_rule(lst, stack):
    for element in reversed(lst):
        stack.append(element)


#--- NOTE! The print statements are outputing to a text file. ---#
#--- This text file represents the stack of the parse table ---#

class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.debug_stack_string = ""

    def parse(self):
        # this initial peek kicks the NoneType that's created by comments out
        self.scanner.peek()
        #print(" ", file=open("parse_tack_trace.txt","w"))
        stack = []
        push_rule([NonTerminal.Program, TokenType.EOF], stack)
        while stack:
            A = top(stack)
            #print("current stack: "+str(stack), file=open("parse_tack_trace.txt", "a"))
            self.debug_stack_string += "Current Stack: "+str(stack)+"\n"
            #print("top of stack: "+str(A), file=open("parse_tack_trace.txt", "a"))
            self.debug_stack_string += "Top of Stack: "+str(A)+"\n"
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                #print("token type: "+str(t.token_type), file=open("parse_tack_trace.txt", "a"))
                self.debug_stack_string += "Token Type: "+str(t.token_type)+"\n"
                #print("token value: "+str(t.token_value), file=open("parse_tack_trace.txt", "a"))
                self.debug_stack_string += "Token Value: "+str(t.token_value)+"\n"
                if A == t.token_type:
                    pop(stack)
                else:
                    msg = 'token mismatch: {} and {}'
                    msg = msg.format(A,t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                #print("token type: "+str(t.token_type), file=open("parse_tack_trace.txt", "a"))
                self.debug_stack_string += "Token Type: "+str(t.token_type)+"\n"
                if((t.token_type == TokenType.OPERATORS) or (t.token_type == TokenType.DELIMETER) or (t.token_type == TokenType.KEYWORD)):
                    terminal = StaticTerminal(t)
                    terminal = terminal.value
                else:
                    terminal = t.token_type
                #print("terminal value: "+str(terminal), file=open("parse_tack_trace.txt", "a"))
                self.debug_stack_string += "Terminal Value: "+str(terminal)+"\n"
                #print("indexing into table: "+str(A)+", "+str(terminal), file=open("parse_tack_trace.txt", "a"))
                self.debug_stack_string += "Indexing into table: "+str(A)+", "+str(terminal)+"\n"
                rule = parse_table.get((A, terminal))
                if rule is not None:
                    pop(stack)
                    push_rule(rule, stack)
                else:
                    msg = 'cannot expand {} on {}'
                    msg = msg.format(A,t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            else:
                msg = 'invalid item on stack: {}'
                msg = msg.format(A)
                raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

            #print("\n", file=open("parse_tack_trace.txt", "a"))
            self.debug_stack_string += "\n"
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            msg = msg.format(t)
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        return True
