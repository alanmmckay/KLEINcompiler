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

class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.debug_stack_string = ""

    def parse(self):
        stack = []
        push_rule([NonTerminal.Program, TokenType.EOF], stack)
        while stack:
            A = top(stack)
            self.debug_stack_string += "Current Stack: "+str(stack)+"\n"
            self.debug_stack_string += "Top of Stack: "+str(A)+"\n"
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                self.debug_stack_string += "Token Type: "+str(t.token_type)+"\n"
                self.debug_stack_string += "Token Value: "+str(t.token_value)+"\n"
                if A == t.token_type:
                    pop(stack)
                else:
                    msg = 'token mismatch: {} and {}'
                    msg = msg.format(A,t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                self.debug_stack_string += "Token Type: "+str(t.token_type)+"\n"
                if((t.token_type == TokenType.OPERATORS) or (t.token_type == TokenType.DELIMETER) or (t.token_type == TokenType.KEYWORD)):
                    terminal = StaticTerminal(t)
                    terminal = terminal.value
                else:
                    terminal = t.token_type
                self.debug_stack_string += "Terminal Value: "+str(terminal)+"\n"
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
            self.debug_stack_string += "\n"
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            msg = msg.format(t)
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        return True
