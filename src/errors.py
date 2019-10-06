import sys
#sys.tracebacklimit=0

# errors thrown by the scanner
class LexicalError(ValueError):
    pass


# errors thrown by the parser
class ParseError(ValueError):
    pass


# errors thrown by the type checker
class SemanticError(ValueError):
    pass
