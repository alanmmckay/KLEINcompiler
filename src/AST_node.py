import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.errors import SemanticError


class ASTnode(object):
    def __init__(self, last, semanticStack):
        pass


class Program(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Definitions(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass


class Function(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Formals(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass


class Formal(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Body(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class PrintStatement(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class OrExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class MinusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class AndExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class TimesExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class DivideExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class IfStatement(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class NotExpr(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class FunctionCall(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Negate(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Actuals(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Nea(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class NumberLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class BooleanLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass


class Type(ASTnode):
    def __init__(self, last, semanticStack):
        pass

    def __str__(self):
        pass
