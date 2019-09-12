from src.k_token import Token, TokenType
from src.errors import LexicalError


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

        if self.program_str[self.pos] == '=':
            self.pos += 1
            return Token(TokenType.EQUALS)

        if self.program_str[self.pos] == '+':
            self.pos += 1
            return Token(TokenType.PLUS)

        if self.program_str[self.pos] == '-':
            self.pos += 1
            return Token(TokenType.MINUS)

        if self.program_str[self.pos] == '<':
            self.pos += 1
            return Token(TokenType.LESSTHAN)

        if self.program_str[self.pos] == '*':
            self.pos += 1
            return Token(TokenType.TIMES)

        if self.program_str[self.pos] == '/':
            self.pos += 1
            return Token(TokenType.DIVIDE)

        # if self.program_str[self.pos] == '(' and self.program_str[self.peek()] == '*':
        #     self.pos += 2
        #     return Token(TokenType.BEGINCOMM)

        if self.program_str[self.pos] == '(':
            self.pos += 1
            return Token(TokenType.LEFTPEREN)

        if self.program_str[self.pos] == ')':
            self.pos += 1
            return Token(TokenType.RIGHTPEREN)

        if self.program_str[self.pos] == ',':
            self.pos += 1
            return Token(TokenType.COMMA)

        if self.program_str[self.pos] == ':':
            self.pos += 1
            return Token(TokenType.COLON)

        # if self.program_str[self.pos:].startswith('(*'):
        #     self.pos += 2
        #     return Token(TokenType.BEGINCOMM)

        # if self.program_str[self.pos:].startswith('*)'):
        #     self.pos += 2
        #     return Token(TokenType.ENDCOMM)

        if self.program_str[self.pos:].startswith('if'):
            self.pos += 2
            return Token(TokenType.IF)

        if self.program_str[self.pos:].startswith('then'):
            self.pos += 4
            return Token(TokenType.THEN)

        if self.program_str[self.pos:].startswith('else'):
            self.pos += 4
            return Token(TokenType.ELSE)

        if self.program_str[self.pos:].startswith('not'):
            self.pos += 3
            return Token(TokenType.NOT)

        if self.program_str[self.pos:].startswith('and'):
            self.pos += 3
            return Token(TokenType.AND)

        if self.program_str[self.pos:].startswith('or'):
            self.pos += 2
            return Token(TokenType.OR)

        if self.program_str[self.pos:].startswith('main'):
            self.pos += 4
            return Token(TokenType.MAIN)

        if self.program_str[self.pos:].startswith('print'):
            self.pos += 5
            return Token(TokenType.PRINT)

        if self.program_str[self.pos].isalpha():
            word = self.get_word()
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
                self.program_str[self.pos].isalpha():
            self.pos += 1
        return self.program_str[start: self.pos]

    def get_number(self):
        start = self.pos
        while self.pos < len(self.program_str) and \
                self.program_str[self.pos] in '0123456789':
            self.pos += 1
        return int(self.program_str[start: self.pos])


# code copied for use in get_next_token() ------------------
#     if the scanner takes a file to read ------------------
'''
  with open(filename) as f:
    while True:
      c = f.read(1)
      if not c:
        print "End of file"
        break
      print "Read a character:", c
'''
