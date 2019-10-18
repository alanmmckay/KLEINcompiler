import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.errors import SemanticError


def top(stack):
    return stack[-1]


def pop(stack):
    stack.pop()


def push_rule(lst, stack):
    for element in reversed(lst):
        stack.append(element)


def push(lst, stack):
    stack.append(lst)


class ASTnode(object):
    pass


class Program(ASTnode):
    pass


class DefinitionsNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass


class FunctionNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class FormalsNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass


class FormalNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class BodyNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class PrintStatementNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class LessThanNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class EqualToNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class OrNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class PlusNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class MinusNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class AndNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class MultiplyNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class DivisionNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class IfNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class NotNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class FunctionCallNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class NegationNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        pass


class ActualsNode(ASTnode):
    def __init__(self, semantic_stack):
        list_of_actuals = []
        while isinstance(top(semantic_stack), NonEmptyActualsNode):
            list_of_actuals.add(pop(semantic_stack))
        push(list_of_actuals, semantic_stack)
    def __str__(self):
        pass


class NonEmptyActualsNode(ASTnode):
    def __init__(self, semantic_stack):
        #this merely exists?
        pass

    def __str__(self):
        pass


class IdentifierNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        pass


class NumberLiteralNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)
        
    def __str__(self):
        pass


class BooleanLiteralNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        pass


class TypeNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        pass
