from enum import Enum

class TokenType(Enum):
    NUMBER = 1
    KEYWORD = 2
    WORD = 3
    OPERATORS = 4
    DELIMETER = 5
    BOOLEAN = 6
    PRIMITIVE = 7
    EOF = 8


class Token:
    def __init__(self, token_type, token_value=None):
        self.token_type = token_type
        self.token_value = token_value

    def is_number(self):
        return self.token_type == TokenType.NUMBER

    def is_keyword(self):
        return self.token_type == TokenType.KEYWORD

    def is_boolean(self):
        return self.token_type == TokenType.BOOLEAN

    def is_operator(self):
        return self.token_type == TokenType.OPERATORS

    def is_delimeter(self):
        return self.token_type == TokenType.DELIMETER

    def is_primitive(self):
        return self.token_type == TokenType.PRIMITIVE

    def is_word(self):
        return self.token_type == TokenType.WORD

    def is_eof(self):
        return self.token_type == TokenType.EOF

    def value(self):
        return self.token_value

    def __repr__(self):
        if self.is_keyword():
            return 'keyword      ' + self.token_value

        elif self.is_number():
            return 'number       ' + str(self.token_value)

        elif self.is_word():
            return 'word         ' + self.token_value

        elif self.is_boolean():
            return 'boolean    ' + self.token_value

        elif self.is_primitive():
            return 'primitive    ' + self.token_value

        elif self.is_operator():
            return 'operator     ' + self.token_value

        elif self.is_delimeter():
            return 'delimeter    ' + self.token_value

        else:  # is_eof()
            return 'end_of_stream'
