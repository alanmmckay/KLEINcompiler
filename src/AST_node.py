import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#from src.errors import SemanticError


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
            #right hand side is popped first...
            rightHandSide = value
            leftHandSide = top(semantic_stack)
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
        if isinstance(top(semantic_stack), ActualsNode):
            actualsNode = top(semantic_stack)
            pop(semantic_stack)
        else:
            #create empty actualsNode
            actualsNode = ActualsNode([])
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
        if(isinstance(top(semantic_stack),FormalsNode)):
            parameters = top(semantic_stack)
            pop(semantic_stack)
        else:
            #create empty formalsNode
            parameters = FormalsNode([])
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
        return nodeType(functions)
    else:
        raise ValueError("halt!!")


class ASTnode(object):
    def __init__(self):
        #this information list will populate during each node construction
        self.information = []
        
    def parse_node(self,position=0):
        if position < len(self.information):#if position is in bounds of information
            evaluate = self.information[position]#take a value to evaluate
            
            print()
            
            if isinstance(evaluate, ASTnode):#if it is a node
                evaluate.parse_node(0)#parse through the node
            
            newEval = self.parse_node(position+1)#grab the next bit of information
            #feed newEval into a function which checks relevant type information
            
            #just printing information here to track what's happening
            if isinstance(evaluate, ASTnode):
                print(type(evaluate))
            else:
                print(type(self.information[position]))#display the information
                print(self.information[position])
                
            return self.information[position]
        
    
class Program(ASTnode):
    pass


class DefinitionsNode(ASTnode):
    def __init__(self, functionsList):
        ASTnode.__init__(self)
        self.functions = functionsList
        self.information = self.functions
        
            
    def __str__(self):
        self.returnString = "Program: \n"
        for function in reversed(self.functions):
            self.returnString += str(function) + "\n"
        return self.returnString


class FunctionNode(ASTnode):
    def __init__(self, name, parameters, returnType, body):
        ASTnode.__init__(self)
        self.bodyNode = body
        self.typeNode = returnType
        self.formals = parameters
        self.identifierNode = name
        
        push(self.bodyNode, self.information)
        push(self.typeNode, self.information)
        push(self.formals, self.information)
        push(self.identifierNode, self.information)

    def __str__(self):
        return "function " + str(self.identifierNode) + " " + str(self.formals) + " " + str(self.typeNode) + " \n" + str(self.bodyNode) + " "


class FormalsNode(ASTnode):
    def __init__(self, parameters):
        ASTnode.__init__(self)
        self.formals = []
        while(len(parameters) > 0):
            push(top(parameters),self.formals)#this is adding a set of tuples: (identifierNode, typeNode)
            pop(parameters)#perhaps change this!!
        self.information = self.formals
    
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
        ASTnode.__init__(self)
        self.expressions = expressions#list of expression and printstatement nodes
        self.information = self.expressions

    def __str__(self):
        returnString = str()
        for expression in self.expressions:
            returnString += str(expression) + "\n"
        returnString += "\n"
        return returnString


# ---  --- #

class ExpressionNode(ASTnode):
    def __init__(self, expression):
        ASTnode.__init__(self)
        self.expression = expression
        push(self.expression, self.information)
        
    def __str__(self):
        return " " + str(self.expression) + " "
    
# --- --- #

class ActualsNode(ASTnode):
    def __init__(self, actuals_list):
        ASTnode.__init__(self)
        self.actuals = []#list of expressions
        while(len(actuals_list) > 0):
            push(top(actuals_list),self.actuals)
            pop(actuals_list)
        self.information = self.actuals

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
        ASTnode.__init__(self)
        self.actualsNode = arguments
        self.identifierNode = functionName
        push(self.actualsNode, self.information)
        push(self.identifierNode, self.information)

    def __str__(self):
        self.returnString = str(self.identifierNode)
        self.returnString += " ("
        self.returnString += str(self.actualsNode)
        self.returnString += ")"
        return self.returnString


# --- --- #

class PrintStatementNode(ASTnode):
    def __init__(self, expressions_list):
        ASTnode.__init__(self)
        self.expressions = expressions_list#list of expression nodes
        self.information = self.expressions

    def __str__(self):
        self.returnString = "print("
        for expression in self.expressions:
            self.returnString += str(expression)
        self.returnString += ")"
        return self.returnString
 
# -- # An if statement consists of various expressions --- #
class IfNode(ASTnode):
    def __init__(self, ifExpression, thenExpression, elseExpression):
        ASTnode.__init__(self)
        self.expr2 = elseExpression
        self.expr1 = thenExpression
        self.condition = ifExpression
        push(self.expr2, self.information)
        push(self.expr1, self.information)
        push(self.condition, self.information)

    def __str__(self):
        self.returnString = "if " + str(self.condition) + "\n"
        self.returnString += "then " + str(self.expr1) + "\n"
        self.returnString += "else " + str(self.expr2) + "\n"
        return self.returnString
  
# --- Expressions have values... --- #

class ValueNode(ASTnode):
    def __init__(self, value):
        ASTnode.__init__(self)
        self.value = value
        push(self.value, self.information)
        
        
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
        self.value1 = leftOperand
        push(self.value1, self.information)

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


