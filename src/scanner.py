import sys
from src.k_token import Token, TokenType
from src.errors import LexicalError


keywords = ["function", "boolean", "if", "then", "else", "not", "and", "or"]
boolean = ["true", "false"]
primitive = ["main", "print"]

class Scanner:
    'Read tokens from an input stream'

    def __init__(self, program_str):
        self.program_str = program_str
        self.pos = 0
        self.lookahead = None

    def peek(self):
        if not self.lookahead:
            self.lookahead = self.get_next_token()
        return self.lookahead

    def next_token(self):
        if self.lookahead:
            answer = self.lookahead
            self.lookahead = None
            return answer
        else:
            return self.get_next_token()

    # --------------------------------------------------------

    def get_next_token(self):
        self.skip_whitespace()

        if self.pos >= len(self.program_str):
            return Token(TokenType.EOF)

        if self.program_str[self.pos] == '0':
            self.pos += 1
            return Token(TokenType.NUMBER, "0")

        if self.program_str[self.pos] == '=':
            self.pos += 1
            return Token(TokenType.OPERATORS, "=")

        if self.program_str[self.pos] == '+':
            self.pos += 1
            return Token(TokenType.OPERATORS, "+")

        if self.program_str[self.pos] == '-':
            self.pos += 1
            return Token(TokenType.OPERATORS, "-")

        if self.program_str[self.pos] == '<':
            self.pos += 1
            return Token(TokenType.OPERATORS, "<")

        if self.program_str[self.pos] == '*':
            self.pos += 1
            return Token(TokenType.OPERATORS, "*")

        if self.program_str[self.pos] == '/':
            self.pos += 1
            return Token(TokenType.OPERATORS, "/")

        if self.program_str[self.pos] == '(':
            self.pos += 1
            if self.program_str[self.pos] == '*':
                self.pos += 1
                self.skip_comment();
                return
            else:
                return Token(TokenType.DELIMETER, "(")

        if self.program_str[self.pos] == ')':
            self.pos += 1
            return Token(TokenType.DELIMETER, ")")

        if self.program_str[self.pos] == ',':
            self.pos += 1
            return Token(TokenType.DELIMETER, ",")

        if self.program_str[self.pos] == ':':
            self.pos += 1
            return Token(TokenType.DELIMETER, ":")

        if self.program_str[self.pos].isalpha():
            word = self.get_word()
            if word in keywords:
                return Token(TokenType.KEYWORD, word)
            elif word in boolean:
                return Token(TokenType.BOOLEAN, word)
            elif word in primitive:
                return Token(TokenType.PRIMITIVE, word)
            else:
                return Token(TokenType.WORD, word)

        if self.program_str[self.pos] in '123456789':
            number = self.get_number()
            return Token(TokenType.NUMBER, number)

        # if no token matches, signal an error

        msg = 'invalid characters at position {}'.format(self.pos)
        raise LexicalError(msg)

    # --------------------------------------------------------

    def skip_whitespace(self):
        while self.pos < len(self.program_str) and \
                self.is_whitespace(self.program_str[self.pos]):
            self.pos += 1
        return

    def is_whitespace(self, ch):
        return ch in ' \n\t\r'

    def get_word(self):
        start = self.pos
        while self.pos < len(self.program_str) and \
                self.program_str[self.pos].isalpha() or self.program_str[self.pos] in "0123456789_":
            self.pos += 1
        return self.program_str[start: self.pos]

    def get_number(self):
        start = self.pos
        while self.pos < len(self.program_str) and \
                self.program_str[self.pos] in '0123456789':
            self.pos += 1

        if int(self.program_str[start: self.pos]) > 2147483647:
            print("too big")
            sys.exit()
        return int(self.program_str[start: self.pos])

    def skip_comment(self):
        while self.pos < len(self.program_str):
            if self.program_str[self.pos] == '*':
                self.pos += 1
                if self.program_str[self.pos] == ')':
                    self.pos += 1
                    return
            else:
                self.pos += 1
        if self.pos >= len(self.program_str):
            self.pos -= 1
        return
