from src.scanner import Scanner
from src.errors import ParseError
from src.parse_table import NonTerminal, parse_table
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

    def parse(self):
        stack = []
        push_rule([NonTerminal.Program, TokenType.EOF], stack)
        while stack:
            A = top(stack)
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                if A == t.token_type:
                    pop(stack)
                else:
                    msg = 'token mismatch: {} and {}'
                    raise ParseError(msg.format(A, t))
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                rule = parse_table.get((A, t.token_type))
                if rule is not None:
                    pop(stack)
                    push_rule(rule, stack)
                else:
                    msg = 'cannot expand {} on {}'
                    raise ParseError(msg.format(A, t))
            else:
                msg = 'invalid item on stack: {}'
                raise ParseError(msg.format(A))

        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            raise ParseError(msg.format(t))

        return True
