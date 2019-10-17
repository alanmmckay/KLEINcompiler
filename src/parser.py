from src.scanner import Scanner
from src.errors import ParseError
from src.parse_table import NonTerminal, Terminal, StaticTerminal, parse_table
from src.k_token import Token, TokenType
from src.AST_node import ASTnode


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
        parse_stack = []
        semantic_stack = []

        push_rule([NonTerminal.Program, TokenType.EOF], parse_stack)
        while parse_stack:
            A = top(parse_stack)
            self.debug_stack_string += "Current Stack: " + str(parse_stack) + "\n"
            self.debug_stack_string += "Top of Stack: " + str(A) + "\n"
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                self.debug_stack_string += "Token Type: " + str(t.token_type) + "\n"
                self.debug_stack_string += "Token Value: " + str(t.token_value) + "\n"
                if A == t.token_type:
                    pop(parse_stack)
                else:
                    msg = 'token mismatch: {} and {}'
                    msg = msg.format(A, t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                self.debug_stack_string += "Token Type: " + str(t.token_type) + "\n"
                if ((t.token_type == TokenType.OPERATORS) or (t.token_type == TokenType.DELIMETER) or (
                        t.token_type == TokenType.KEYWORD)):
                    terminal = StaticTerminal(t)
                    terminal = terminal.value
                else:
                    terminal = t.token_type
                self.debug_stack_string += "Terminal Value: " + str(terminal) + "\n"
                self.debug_stack_string += "Indexing into table: " + str(A) + ", " + str(terminal) + "\n"
                rule = parse_table.get((A, terminal))
                if rule is not None:
                    pop(parse_stack)
                    push_rule(rule, parse_stack)
                else:
                    msg = 'cannot expand {} on {}'
                    msg = msg.format(A, t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

            ##############################
            elif issubclass(A, ASTnode):
                pop(parse_stack)
                push_rule(rule,semantic_stack)

            #################################
            else:
                msg = 'invalid item on parse_stack: {}'
                msg = msg.format(A)
                raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            self.debug_stack_string += "\n"
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            msg = msg.format(t)
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        ##################################
        else:
            return pop(semantic_stack)

        ##################################

        return True
