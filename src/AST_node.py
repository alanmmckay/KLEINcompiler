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
        return str()


class FunctionNode(ASTnode):
    def __init__(self, semantic_stack):
        self.identifier = top(semantic_stack)
        pop(semantic_stack)
        self.formals = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return "Function Node Values: " + str(self.identifier) + " " + str(self.formals)


class FormalsNode(ASTnode):
    def __init__(self, semantic_stack):
        self.formals = []
        while True:
            if isinstance(top(semantic_stack), TypeNode):
                self.formalType = top(semantic_stack)
                pop(semantic_stack)
                self.identifier = top(semantic_stack)
                pop(semantic_stack)
                push_rule((self.identifier, self.formalType), self.formals)
            else:
                break
        
            
    def __iter__(self):
        pass

    def __str__(self):
        self.returnString = "FromalsNode Values: \n"
        for i in self.formals:
            self.returnString += str(i) + " \n"
        return self.returnString


'''class FormalNode(ASTnode):
    def __init__(self, semantic_stack):
        pass

    def __str__(self):
        return str()'''


class BodyNode(ASTnode):
    def __init__(self, semantic_stack):
        self.printStatement = top(semantic_stack)
        self.expressions = []
        while isinstance(top(semantic_stack), Expression):
            push(top(semantic_stack, self.expressions))
            pop(semantic_stack)

    def __str__(self):
        return str()


class PrintStatementNode(ASTnode):
    def __init__(self, semantic_stack):
        self.expressions = []
        while isinstance(top(semantic_stack), Expression):
            push(top(semantic_stack), self.expressions)
            pop(semantic_stack)

    def __str__(self):
        return str()

class IfNode(ASTnode):
    def __init__(self, semantic_stack):
        self.Condition = top(semantic_stack)
        pop(semantic_stack)
        self.expr1 = top(semantic_stack)
        pop(semantic_stack)
        self.expr2 = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str()
    

# --- UnaryOperator: subclass of ASTnode --- #

class Expression(ASTnode):
    def __init__(self):
        pass
    
    def __str__(self):
        return str()
    

class UnaryOperator(Expression):
    def __init__(self, semantic_stack):
        self.operatorType = "UnaryOperator"
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return self.operatorType + " " + str(self.value) +" \n"


class NotNode(UnaryOperator):
    def __init__(self, semantic_stack):
        UnaryOperator(self, semantic_stack)
        self.operatorType = "not"


class NegationNode(ASTnode):
    def __init__(self, semantic_stack):
        UnaryOperator(self, semantic_stack)
        self.operatorType = "negate"
    

# --- BinaryOperator: subclass of UnaryOperator --- #

class BinaryOperator(UnaryOperator):
    def __init__(self, semantic_stack):
        UnaryOperator.__init__(self, semantic_stack)
        self.value1 = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.value1) + " " + self.operatorType + " " + str(self.value) + " \n"

class LessThanNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "<"


class EqualToNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "="


class OrNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "or"


class PlusNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "+"


class MinusNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "-"


class AndNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "and"


class MultiplyNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "*"


class DivisionNode(BinaryOperator):
    def __init__(self, semantic_stack):
        BinaryOperator.__init__(self, semantic_stack)
        self.operatorType = "/"


# --- A FunctionCall needs to know an identifier name and the parameters --- #
class FunctionCallNode(ASTnode):
    def __init__(self, semantic_stack):
        self.functionName = top(semantic_stack)
        pop(semantic_stack)
        self.actuals = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        self.returnString = "FunctionCallNode Values: \n"
        self.returnString += self.functionName+"\n"
        self.returnString += self.actuals
        return returnString


class ActualsNode(ASTnode):
    def __init__(self, semantic_stack):
        self.actuals = []
        while isinstance(top(semantic_stack), ASTnode):
            push(pop(semantic_stack), self.actuals)
        
    def __str__(self):
        self.returnString = "ActualsNode Vales: \n"
        for i in actuals:
            self.returnString += "i \n"
        return self.returnString


'''class NonEmptyActualsNode(ASTnode):
    def __init__(self, semantic_stack):
        #this merely exists?
        pass

    def __str__(self):
        pass'''


class IdentifierNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.value)


class NumberLiteralNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)
        
    def __str__(self):
        return str(self.value)

class BooleanLiteralNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.value)


class TypeNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.value)
