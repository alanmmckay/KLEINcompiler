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


'''def buildNode(semantic_stack, nodeType):
    
    if issubclass(nodeType, ValueNode):
        if nodeType == BinaryOperator:
            #create node sending the value parameters based on the semantic stack
        else:
            #create node sending a single value as a parameter based on the semantic stack
    if nodeType == IfNode:#three values
        #create node sending the three parameters based on the semantic stack
    if nodeType == PrintStatementNode:#at least one value[?]
        #create node sending a list of parameters[?] from the semantic stack
    if nodeType == ActualsNode:#at least one value
        #create node sending a list of actuals
    if nodeType == FunctionCallNode:#two values
        #create node sending an identifier node and an actuals node
    if nodeType == BodyNode:
        #create a node that is either a print statement or a set of expressions
    if nodeType == FormalsNode:#two values
        #create node sending a set of tuples which define a identifier : type pair
    if nodeType == FunctionNode:
        #create node sneding a formals node and an identifier node
    if nodeType == DefinitionsNode
        #create node sending...'''

class ASTnode(object):
    pass


class Program(ASTnode):
    pass


class DefinitionsNode(ASTnode):
    def __init__(self, semantic_stack):
        self.functions = []
        while True:
            if len(semantic_stack) > 0 and isinstance(top(semantic_stack), FunctionNode):
                push(top(semantic_stack), self.functions)
                #print(top(semantic_stack))
                pop(semantic_stack)
            else:
                break
            
    def __str__(self):
        self.returnString = "Program: \n"
        for function in reversed(self.functions):
            self.returnString += str(function) + "\n"
        return self.returnString


class FunctionNode(ASTnode):
    def __init__(self, semantic_stack):
        self.functionBody = top(semantic_stack)
        pop(semantic_stack)
        self.functionType = top(semantic_stack)
        pop(semantic_stack)
        self.functionFormals = top(semantic_stack)
        pop(semantic_stack)
        self.functionName = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.functionName) + " " + str(self.functionFormals) + " " + str(self.functionType) + " \n" + str(self.functionBody)


class FormalsNode(ASTnode):
    def __init__(self, semantic_stack):
        self.formals = []
        while True:
            if isinstance(top(semantic_stack), TypeNode):
                self.formalType = top(semantic_stack)
                pop(semantic_stack)
                self.identifier = top(semantic_stack)
                pop(semantic_stack)
                push((self.identifier, self.formalType), self.formals)
            else:
                break
        
    def __iter__(self):
        pass

    def __str__(self):
        self.returnString = " ("
        for pair in self.formals:
            self.returnString += str(pair[0]) + " : " + str(pair[1])
            if pair != self.formals[-1]:#!!! this could be a problem!
                self.returnString += ", "
        self.returnString += ")"
        return self.returnString


class BodyNode(ASTnode):
    def __init__(self, semantic_stack):
        self.expressions = []
        while isinstance(top(semantic_stack), ExpressionNode) or isinstance(top(semantic_stack), PrintStatementNode):
            push(top(semantic_stack), self.expressions)
            pop(semantic_stack)

    def __str__(self):
        returnString = str()
        for expression in self.expressions:
            returnString += str(expression) + "\n"
        returnString += "\n"
        return returnString


# ---  --- #

'''class Expression(ASTnode):
    def __init__(self):
        pass
    
    def __str__(self):
        return str()
'''

class ExpressionNode(ASTnode):
    def __init__(self, semantic_stack):
        self.expression = top(semantic_stack)
        pop(semantic_stack)
        
    def __str__(self):
        return str(self.expression)
    
# --- --- #

class ActualsNode(ASTnode):
    def __init__(self, semantic_stack):
        self.actuals = []
        while isinstance(top(semantic_stack), ExpressionNode):
            push(top(semantic_stack), self.actuals)
            pop(semantic_stack)
        
    def __str__(self):
        self.returnString = str()
        for i in self.actuals:
            self.returnString += str(i)
            if i != self.actuals[-1]:#!!! this could be a problem...
                self.returnString += ", "
        return self.returnString


# --- A FunctionCall needs to know an identifier name and the parameters --- #
class FunctionCallNode(ASTnode):
    def __init__(self, semantic_stack):
        self.actualsNode = top(semantic_stack)
        pop(semantic_stack)
        self.functionName = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        self.returnString = str(self.functionName)
        self.returnString += " ("
        self.returnString += str(self.actualsNode)
        self.returnString += ")"
        return self.returnString


# --- --- #

class PrintStatementNode(ASTnode):
    def __init__(self, semantic_stack):
        self.expressions = []
        while isinstance(top(semantic_stack), ExpressionNode):
            push(top(semantic_stack), self.expressions)
            pop(semantic_stack)

    def __str__(self):
        self.returnString = "print("
        for expression in self.expressions:
            self.returnString += str(expression)
        self.returnString += ")"
        return self.returnString
 
# -- # An if statement consists of various expressions --- #
class IfNode(ASTnode):
    def __init__(self, semantic_stack):
        self.expr2 = top(semantic_stack)
        pop(semantic_stack)
        self.expr1 = top(semantic_stack)
        pop(semantic_stack)
        self.condition = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        self.returnString = "if " + str(self.condition) + "\n"
        self.returnString += "then " + str(self.expr1) + "\n"
        self.returnString += "else " + str(self.expr2) + "\n"
        return self.returnString
  
# --- Expressions have values... --- #

class ValueNode(ASTnode):
    def __init__(self, semantic_stack):
        self.value = top(semantic_stack)
        pop(semantic_stack)
        
    def __str__(self):
        return str(self.value)
    
    
class IdentifierNode(ValueNode):
    def __init__(self, semantic_stack):
        ValueNode.__init__(self, semantic_stack)


class NumberLiteralNode(ValueNode):
    def __init__(self, semantic_stack):
        ValueNode.__init__(self, semantic_stack)


class BooleanLiteralNode(ValueNode):
    def __init__(self, semantic_stack):
        ValueNode.__init__(self, semantic_stack)



class TypeNode(ValueNode):
    def __init__(self, semantic_stack):
        ValueNode.__init__(self, semantic_stack)
        

# --- Values can have an operation --- #

class Operator(ValueNode):
    def __init__(self, semantic_stack):
        ValueNode.__init__(self, semantic_stack)
        self.operatorType = str()
        

# --- An operator can be a unary --- #

class UnaryOperator(Operator):
    def __init__(self, semantic_stack):
        Operator.__init__(self, semantic_stack)
        self.operatorType = "UnaryOperator"

    def __str__(self):
        return self.operatorType + " " + str(self.value) + " "

# -- # Unary Operators:
class NotNode(UnaryOperator):
    def __init__(self, semantic_stack):
        UnaryOperator.__init__(self, semantic_stack)
        self.operatorType = "not"


class NegationNode(UnaryOperator):
    def __init__(self, semantic_stack):
        UnaryOperator.__init__(self, semantic_stack)
        self.operatorType = "negate"
    

# --- A Binary Operator has two values --- #

class BinaryOperator(UnaryOperator):
    def __init__(self, semantic_stack):
        self.operatorType = "BinaryOperator"
        UnaryOperator.__init__(self, semantic_stack)
        self.value1 = top(semantic_stack)
        pop(semantic_stack)

    def __str__(self):
        return str(self.value1) + " " + self.operatorType + " " + str(self.value) + " "

# -- # Binary Operators: 
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

