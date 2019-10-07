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

    def parse(self):
        self.scanner.peek()# this kicks the NoneType that's created by comments out
        print(" ", file=open("parse_tack_trace.txt","w"))
        stack = []
        push_rule([NonTerminal.Program, TokenType.EOF], stack)
        while stack:
            A = top(stack)
            print("current stack: "+str(stack), file=open("parse_tack_trace.txt", "a"))
            print("top of stack: "+str(A), file=open("parse_tack_trace.txt", "a"))
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                print("token type: "+str(t.token_type), file=open("parse_tack_trace.txt", "a"))
                print("token value: "+str(t.token_value), file=open("parse_tack_trace.txt", "a"))
                if A == t.token_type:
                    pop(stack)
                else:
                    msg = 'token mismatch: {} and {}'
                    raise ParseError(msg.format(A, t))
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                print("token type: "+str(t.token_type), file=open("parse_tack_trace.txt", "a"))
                if((t.token_type == TokenType.OPERATORS) or (t.token_type == TokenType.DELIMETER) or (t.token_type == TokenType.KEYWORD)):
                    terminal = StaticTerminal(t)
                    terminal = terminal.value
                else:
                    terminal = t.token_type
                print("terminal value: "+str(terminal), file=open("parse_tack_trace.txt", "a"))
                rule = parse_table.get((A, terminal))
                print("indexing into table: "+str(A)+", "+str(terminal), file=open("parse_tack_trace.txt", "a"))
                if rule is not None:
                    pop(stack)
                    push_rule(rule, stack)
                else:
                    msg = 'cannot expand {} on {}'
                    raise ParseError(msg.format(A, t))
            else:
                msg = 'invalid item on stack: {}'
                raise ParseError(msg.format(A))

            print("\n", file=open("parse_tack_trace.txt", "a"))
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            raise ParseError(msg.format(t))

        return True
