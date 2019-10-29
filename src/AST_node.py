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


#--- Possible functional node factory implementation ---#

def nodeBuilder(semantic_stack, nodeType):
    if nodeType == ExpressionNode:
        expression = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(expression)
    elif issubclass(nodeType, ValueNode):
        value = top(semantic_stack)
        pop(semantic_stack)
        if issubclass(nodeType, BinaryOperator):
            leftHandSide = value
            rightHandSide = top(semantic_stack)
            pop(semantic_stack)
            return nodeType(leftHandSide, rightHandSide)
        else:
            return nodeType(value)
    elif nodeType == PrintStatementNode:
        expressions = []
        while isinstance(top(semantic_stack), ExpressionNode):
            push(top(semantic_stack), expressions)
            pop(semantic_stack)
        return nodeType(expressions)
    elif nodeType == IfNode:#rename these vars...[?]
        elseStatement = top(semantic_stack)
        pop(semantic_stack)
        thenStatement = top(semantic_stack)
        pop(semantic_stack)
        ifCondition = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(ifCondition,thenStatement,elseStatement)
    elif nodeType == ActualsNode:
        actuals = []
        while isinstance(top(semantic_stack), ExpressionNode):
            push(top(semantic_stack), actuals)
            pop(semantic_stack)
        return nodeType(actuals)
    elif nodeType == FunctionCallNode:
        actualsNode = top(semantic_stack)
        pop(semantic_stack)
        functionName = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(functionName, actualsNode)
    elif nodeType == FormalsNode:#getting parameter and argument switched up here...?
        parameters = []
        while True:
            if isinstance(top(semantic_stack), TypeNode):
                parameterType = top(semantic_stack)
                pop(semantic_stack)
                identifier = top(semantic_stack)
                pop(semantic_stack)
                push((identifier, parameterType), parameters)
            else:
                break
        return nodeType(parameters)
    elif nodeType == FunctionNode:
        body = top(semantic_stack)
        pop(semantic_stack)
        returnType = top(semantic_stack)
        pop(semantic_stack)
        parameters = top(semantic_stack)
        pop(semantic_stack)
        name = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(name, parameters, returnType, body)
    elif nodeType == BodyNode:
        expressions = []
        while isinstance(top(semantic_stack), ExpressionNode) or isinstance(top(semantic_stack), PrintStatementNode):
           push(top(semantic_stack), expressions)
           pop(semantic_stack)
        return nodeType(expressions)
    elif nodeType == DefinitionsNode:
        functions = []
        while True:
            if len(semantic_stack) > 0 and isinstance(top(semantic_stack), FunctionNode):
                push(top(semantic_stack), functions)
                pop(semantic_stack)
            else:
                break
        return functions
    else:
        raise ValueError("halt!!")


class ASTnode(object):
    pass


class Program(ASTnode):
    pass


class DefinitionsNode(ASTnode):
    def __init__(self, functionsList):
        self.functions = functionsList
            
    def __str__(self):
        self.returnString = "Program: \n"
        for function in reversed(self.functions):
            self.returnString += str(function) + "\n"
        return self.returnString


class FunctionNode(ASTnode):
    def __init__(self, name, parameters, returnType, body):
        self.bodyNode = body
        self.typeNode = returnType
        self.formals = parameters
        self.identifierNode = name

    def __str__(self):
        return "functionNode: " + str(self.identifierNode) + " " + str(self.formals) + " " + str(self.typeNode) + " \n" + str(self.bodyNode) + " end funciton node"


class FormalsNode(ASTnode):
    def __init__(self, parameters):
        self.formals = parameters
        
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
    def __init__(self, expressions):
        self.expressions = expressions

    def __str__(self):
        returnString = str()
        for expression in self.expressions:
            returnString += str(expression) + "\n"
        returnString += "\n"
        return returnString


# ---  --- #

class ExpressionNode(ASTnode):
    def __init__(self, expression):
        self.expression = expression
        
    def __str__(self):
        return "begin expression node: " + str(self.expression) + "end expression"
    
# --- --- #

class ActualsNode(ASTnode):
    def __init__(self, actuals_list):
        self.actuals = actuals_list
        
    def __str__(self):
        self.returnString = str()
        for i in self.actuals:
            self.returnString += str(i)
            if i != self.actuals[-1]:#!!! this could be a problem...
                self.returnString += ", "
        return self.returnString


# --- A FunctionCall needs to know an identifier name and the parameters --- #
class FunctionCallNode(ASTnode):
    def __init__(self, functionName, arguments):
        self.actualsNode = arguments
        self.identifierNode = functionName

    def __str__(self):
        self.returnString = str(self.identifierNode)
        self.returnString += " ("
        self.returnString += str(self.actualsNode)
        self.returnString += ")"
        return self.returnString


# --- --- #

class PrintStatementNode(ASTnode):
    def __init__(self, expressions_list):
        self.expressions = expressions_list

    def __str__(self):
        self.returnString = "print("
        for expression in self.expressions:
            self.returnString += str(expression)
        self.returnString += ")"
        return self.returnString
 
# -- # An if statement consists of various expressions --- #
class IfNode(ASTnode):
    def __init__(self, ifExpression, thenExpression, elseExpression):
        self.expr2 = elseExpression
        self.expr1 = thenExpression
        self.condition = ifExpression

    def __str__(self):
        self.returnString = "if " + str(self.condition) + "\n"
        self.returnString += "then " + str(self.expr1) + "\n"
        self.returnString += "else " + str(self.expr2) + "\n"
        return self.returnString
  
# --- Expressions have values... --- #

class ValueNode(ASTnode):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        self.returnString = str(self.value)
        return self.returnString
    
    
class IdentifierNode(ValueNode):
    def __init__(self, name):
        ValueNode.__init__(self, name)


class NumberLiteralNode(ValueNode):
    def __init__(self, number):
        ValueNode.__init__(self, number)


class BooleanLiteralNode(ValueNode):
    def __init__(self, boolValue):
        ValueNode.__init__(self, boolValue)



class TypeNode(ValueNode):
    def __init__(self, typeValue):
        ValueNode.__init__(self, typeValue)
        

# --- Values can have an operation --- #

class Operator(ValueNode):
    def __init__(self, operand):
        ValueNode.__init__(self, operand)
        self.operatorType = str()
        

# --- An operator can be a unary --- #

class UnaryOperator(Operator):
    def __init__(self, operand):
        Operator.__init__(self, operand)
        self.operatorType = "UnaryOperator"

    def __str__(self):
        self.returnString = " " + self.operatorType + " "
        self.returnString += str(self.value) + " "
        return self.returnString

# -- # Unary Operators:
class NotNode(UnaryOperator):
    def __init__(self, operand):
        UnaryOperator.__init__(self, operand)
        self.operatorType = "not"


class NegationNode(UnaryOperator):
    def __init__(self, operand):
        UnaryOperator.__init__(self, operand)
        self.operatorType = "negate"
    

# --- A Binary Operator has two values --- #

class BinaryOperator(UnaryOperator):
    def __init__(self, leftOperand, rightOperand):
        self.operatorType = "BinaryOperator"
        UnaryOperator.__init__(self, rightOperand)
        self.value1 = rightOperand

    def __str__(self):
        self.returnString = str(self.value1) + " "
        self.returnString += self.operatorType + " "
        self.returnString += str(self.value) + " "
        return self.returnString

# -- # Binary Operators: 
class LessThanNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "<"


class EqualToNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "="


class OrNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "or"


class PlusNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "+"


class MinusNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "-"


class AndNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "and"


class MultiplyNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "*"


class DivisionNode(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.operatorType = "/"

