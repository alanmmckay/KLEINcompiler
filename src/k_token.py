from enum import Enum

class TokenType(Enum):
    NUMBER = 1
    KEYWORD = 2
    WORD = 3
    OPERATORS = 4
    SEPERATORS = 5
    EOF = 6


class Token:
    def __init__(self, token_type, token_value=None):
        self.token_type = token_type
        self.token_value = token_value

    def is_main(self):
        return self.token_type == TokenType.WORD

    def is_print(self):
        return self.token_type == TokenType.WORD

    def is_number(self):
        return self.token_type == TokenType.NUMBER

    def is_if(self):
        return self.token_type == TokenType.KEYWORD

    def is_then(self):
        return self.token_type == TokenType.KEYWORD

    def is_else(self):
        return self.token_type == TokenType.KEYWORD

    def is_not(self):
        return self.token_type == TokenType.KEYWORD

    def is_and(self):
        return self.token_type == TokenType.KEYWORD

    def is_or(self):
        return self.token_type == TokenType.KEYWORD

    def is_equals(self):
        return self.token_type == TokenType.OPERATORS

    def is_word(self):
        return self.token_type == TokenType.WORD

    def is_plus(self):
        return self.token_type == TokenType.OPERATORS

    def is_minus(self):
        return self.token_type == TokenType.OPERATORS

    def is_lessthan(self):
        return self.token_type == TokenType.OPERATORS

    def is_times(self):
        return self.token_type == TokenType.OPERATORS

    def is_divide(self):
        return self.token_type == TokenType.OPERATORS

    def is_leftperen(self):
        return self.token_type == TokenType.SEPERATORS

    def is_rightperen(self):
        return self.token_type == TokenType.SEPERATORS

    def is_begincomm(self):
        return self.token_type == TokenType.SEPERATORS

    def is_endcomm(self):
        return self.token_type == TokenType.SEPERATORS

    def is_comma(self):
        return self.token_type == TokenType.SEPERATORS

    def is_colon(self):
        return self.token_type == TokenType.SEPERATORS

    def is_eof(self):
        return self.token_type == TokenType.EOF

    def value(self):
        return self.token_value

    def __repr__(self):
        if self.is_main():
            return 'main'
        elif self.is_print():
            return 'print'
        elif self.is_if():
            return 'if'
        elif self.is_then():
            return 'then'
        elif self.is_else():
            return 'else'
        elif self.is_not():
            return 'not'
        elif self.is_and():
            return 'and'
        elif self.is_or():
            return 'or'
        elif self.is_number():
            return 'number = ' + str(self.token_value)
        elif self.is_equals():
            return 'equal sign'
        elif self.is_word():
            return 'word  = ' + self.token_value
        elif self.is_plus():
            return 'plus sign'
        elif self.is_minus():
            return 'minus sign'
        elif self.is_lessthan():
            return 'less than sign'
        elif self.is_times():
            return 'times sign'
        elif self.is_divide():
            return 'division sign'
        elif self.is_leftperen():
            return 'left peren'
        elif self.is_rightperen():
            return 'right peren'
        elif self.is_begincomm():
            return 'begin comment'
        elif self.is_endcomm():
            return 'end comment'
        elif self.is_comma():
            return 'comma'
        elif self.is_colon():
            return 'colon'
        else:  # is_eof()
            return 'end_of_stream'
