from src.k_token import Token, TokenType
from src.errors import LexicalError

keywords = ["function", "boolean", "if", "then", "else", "not", "and", "or", "integer", "print"]
boolean = ["true", "false"]
# primitive = ["main", "print"]


class Scanner:
    """Read tokens from an input stream"""

    def __init__(self, program_str):
        self.program_str = program_str
        self.pos = 0
        self.lookahead = None
        self.line = 1

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

        # This would be the state to handle end of file.
        if self.pos >= len(self.program_str):
            return Token(TokenType.EOF)

        # This is a state to handle lone zeros
        # Needs to be fixed so if anything int or alpha follows throws error
        if self.program_str[self.pos] == '0':
            self.pos += 1
            return Token(TokenType.NUMBER, "0")

        # This chunk handles our operator state
        # -----------------------------------------------------
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
        # -------------------------------------------------

        # This section handles our delimeter state as well as comments
        # --------------------------------------------------
        if self.program_str[self.pos] == '(':
            self.pos += 1
            if self.program_str[self.pos] == '*':
                self.pos += 1
                self.skip_comment()
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
        # -------------------------------------------------

        # this section handles our Keyword, Boolean, Primitive and Word states.
        # -------------------------------------------------
        if self.program_str[self.pos].isalpha():
            word = self.get_word()
            if word in keywords:
                return Token(TokenType.KEYWORD, word)
            elif word in boolean:
                return Token(TokenType.BOOLEAN, word)
            # elif word in primitive:
            #     return Token(TokenType.PRIMITIVE, word)
            else:
                return Token(TokenType.WORD, word)
            # --------------------------------------------

        # This would be the section where we handle our integer state
        # -------------------------------------------------------
        if self.program_str[self.pos] in '123456789':
            number = self.get_number()
            return Token(TokenType.NUMBER, number)
        # -------------------------------------------------------

        # if no token matches, signal an error
        msg = 'invalid character: {} on line {}'.format(self.program_str[self.pos], self.line)
        LexicalError(msg, self.program_str, self.pos)
        #raise LexicalError(msg, self.pos, program_str)

    # --------------------------------------------------------

    def skip_whitespace(self):
        while self.pos < len(self.program_str) and \
                self.is_whitespace(self.program_str[self.pos]):
            self.pos += 1
        return

    def is_whitespace(self, ch):
        if ch == '\n':
            self.line += 1
        return ch in ' \n\t\r'

    def get_word(self):
        start = self.pos
        while self.pos < len(self.program_str) and \
                self.program_str[self.pos].isalpha() or self.program_str[self.pos] in "0123456789_":
            self.pos += 1
            if (self.pos - start) > 256:
                msg = 'IDENTIFIER exceeds 256 character limit on line {} \n IDENTIFIER: {}'
                msg = msg.format(self.line, self.program_str[start: self.pos])
                raise LexicalError(msg, self.program_str, self.pos)
        return self.program_str[start: self.pos]

    def get_number(self):
        start = self.pos
        while self.pos < len(self.program_str) and \
                self.program_str[self.pos] in '0123456789':
            self.pos += 1
        if int(self.program_str[start: self.pos]) > 2147483647:
            msg = "INTEGER out of bounds on line {} \n INTEGER: {} \n must be within range +/- 2147483647"
            msg = msg.format(self.line, self.program_str[start: self.pos])
            raise LexicalError(msg, self.program_str, self.pos)
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
