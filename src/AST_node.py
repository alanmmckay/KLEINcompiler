import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.errors import SemanticError
from src.stack_operations import top, pop, push, push_rule

function_record = []
# used to keep track of the function definition
# that is currently being processed

function_table = {}
#function_table[functionName] = {"functionNode":FunctionNode object, "stack_position": position of function in IMEM.}

#temp_vars stores available dmem addresses
temp_vars = [0]

# This function should return the offset from the stack pointer of the next open
# memory location for saving a temporary variable (and update the count)
def get_open_place( ):
    next_open = temp_vars.pop( )
    temp_vars.append( next_open + 1 )
    return next_open

def nodeBuilder(semantic_stack, nodeType):
    if nodeType == ExpressionNode:
        expression = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(expression)

    elif issubclass(nodeType, ValueNode):
        value = top(semantic_stack)
        pop(semantic_stack)
        if issubclass(nodeType, BinaryOperator):
            # right hand side is popped first...
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

    elif nodeType == IfNode:  # rename these vars...[?]
        elseStatement = top(semantic_stack)
        pop(semantic_stack)
        thenStatement = top(semantic_stack)
        pop(semantic_stack)
        ifCondition = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(ifCondition, thenStatement, elseStatement)

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
            # create empty actualsNode
            actualsNode = ActualsNode([])
        functionName = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(functionName, actualsNode)

    elif nodeType == FormalsNode:  # getting parameter and argument switched up here...?
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
        if (isinstance(top(semantic_stack), FormalsNode)):
            parameters = top(semantic_stack)
            pop(semantic_stack)
        else:
            # create empty formalsNode
            parameters = FormalsNode([])
        name = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(name, parameters, returnType, body)

    elif nodeType == BodyNode:
        expressions = []
        while isinstance(top(semantic_stack), ExpressionNode) or isinstance(top(semantic_stack),
                                                                            PrintStatementNode) or isinstance(
            top(semantic_stack), BodyNode):
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
    elif nodeType == ProgramNode:
        #hand the DefinitionsNode to the ProgramNode
        functionDefinitions = top(semantic_stack)
        pop(semantic_stack)
        return nodeType(functionDefinitions)
    else:
        raise ValueError("Invalid node type in nodeBuilder")


class ErrorNode(object):
    def __init__(self, msg):
        self.msg = msg

    def get_message(self):
        return self.msg


class ASTnode(object):
    def __init__(self):
        # this information list will populate during each node construction
        self.information = []
        # outputType designates the type of values to expect from the result of the node
        self.outputType = str()

    def process_node(self, position=0):
        # ad-hoc means to push the ErrorNode to the parser---
        if len(function_record) > 0 and isinstance(top(function_record), ErrorNode):
            return function_record
        # I'm unsure if this block is neccessary---#

        if position < len(self.information):  # if position is in bounds of information
            evaluate = self.information[position]  # take a value to evaluate

            if isinstance(evaluate, ASTnode):  # if it is a node
                if isinstance(evaluate, FunctionNode):
                    function_record.append(
                        evaluate.get_name())  # this list is used to keep track of which function is currently being processed

                nextNode = evaluate.process_node(0)  # make way to the leaf of a branch

                # ad-hoc means to push the ErrorNode to the parser---
                if len(function_record) > 0 and isinstance(top(function_record), ErrorNode):
                    return function_record
                # this block is used. Keep it until a more elegant solution is found---#

            # traverse each leaf of a respective branch
            nextInfo = self.process_node(position + 1)

            if isinstance(evaluate, ASTnode):
                # the aboverecursive descent will force typecheck to start at a leaf
                errorState = evaluate.typeCheck()
                if errorState != None:
                    push(ErrorNode(errorState), function_record)

            # ad-hocery! ---
            if isinstance(top(function_record), ErrorNode):
                return function_record
            #this block is used, simillar to previous block---#
            return self.information[position]

    def typeCheck(self):
        if 'main' not in function_table:
            return "A main function must be declared."

    def get_outputType(self):
        return self.outputType
#end ASTNode superclass


class ProgramNode(ASTnode):
    #consideration: put all class definitions WITHIN this node.
    #use this node to store the function table and function record
    def __init__(self, functionDefinitions):
        ASTnode.__init__(self)
        self.definitionsNode = functionDefinitions
        push(self.definitionsNode,self.information)


    def __str__(self):
        #Definitions.__str__() prints out the function list...
        self.returnString = "Program: \n"
        self.returnString += self.definitionsNode.__str__()
        return self.returnString

    def typeCheck(self):
        pass

    def code_gen(self, line):
        program = []

        #This block rebuilds the argument list in DMEM to factor the existence
        #of a return address and return value within a regular function
            #Basically: an adhoc implementation to allow TM parameters    
        r6_address = len(function_table['main']['functionNode'].get_formals())
        main_arguments = []
        index = 1
        while index < r6_address + 1:
            main_arguments = main_arguments + ['LD 1,'+str(index)+'(0)', 'ST 1,'+str(index+3)+'(6)']
            index+=1
            
        #perhaps replace index - 1 with r6_address
        program += self.definitionsNode.code_gen(7 + ((index - 1)*2))

        front_matter = main_arguments + ['LDC 6,1(4)',#set position of top
                        'LDC 1,2(4)',
                        'ADD 1,7,1',
                        'ST 1,0(6)',#store return address
                        'LDA 7,' + str(function_table['main']['stack_position'] + 2) + '(7)',
                        'OUT 0,0,0',
                        'HALT 0,0,0']

        program = front_matter + program

        # Second pass to find function calls and insert the address of the
        # function (since we might now know this address when the function is
        # called)
        for index, instruction in enumerate(program):
            if 'FUNCTION-CALL' in instruction:
                # Remove the placeholder instruction from the program...
                program.pop( index )

                # ... and replace with a 'load-constant' to put the address of
                #     the called function into the PC (register 7)
                function_address = function_table[instruction.split()[1]]['function_address']
                program.insert( index, 'LDC 7,' + str(function_address) + '(4) : '+instruction.split()[1]+' FUNCTION-CALL')
                
        return program
#end ProgramNode


class DefinitionsNode(ASTnode):
    def __init__(self, functionsList):
        ASTnode.__init__(self)
        self.functions = functionsList
        self.information = self.functions
        self.functionSwitch = None

        # build function a function table to ensure function calls are valid
        for function in self.functions:
            functionName = function.get_name()
            if functionName not in function_table:
                function_table[functionName] = {}
                function_table[functionName]["functionNode"] = function
            else:
                self.functionSwitch = functionName
                continue

    def __str__(self):
        self.returnString = str()
        for function in reversed(self.functions):
            self.returnString += str(function) + "\n"
        return self.returnString

    def typeCheck(self):
        if self.functionSwitch != None:
            msg = 'Duplicate Function Declaration: {}'
            msg = msg.format(self.functionSwitch)
            return msg

    def code_gen(self, line):
        program = []
        for function in self.functions:
            function_table[function.get_name()]["stack_position"] = len(program)
            function_table[function.get_name()]['function_address'] = len(program) + line
            program += function.code_gen(line + len(program))
        # Our first instruction is to set the PC to the address of the 'main' function
        return program
#end DefinitionsNode


class FunctionNode(ASTnode):
    def __init__(self, name, parameters, returnType, body):
        ASTnode.__init__(self)
        self.bodyNode = body
        self.typeNode = returnType
        self.formals = parameters
        self.identifierNode = FunctionIdentifierNode(name)
        self.outputType = self.typeNode.get_outputType()

        push(self.bodyNode, self.information)
        push(self.typeNode, self.information)
        push(self.formals, self.information)
        push(self.identifierNode, self.information)

    def get_name(self):
        return self.identifierNode.__str__()

    def get_formals(self):
        return self.formals.get_formals()

    def __str__(self):
        return "function " + str(self.identifierNode) + " " + str(self.formals) + " " + str(
            self.typeNode) + " \n" + str(self.bodyNode) + " "

    def check_formals(self):
        current_function = function_record[-1]
        formal_list = []
        for formal in self.formals.get_formals():
            if formal[0].get_value() in formal_list:
                msg = "Duplicate parameter {} in function {}."
                msg = msg.format(formal[0].get_value(), current_function)
                return msg
            push(formal[0].get_value(),formal_list)
            

    def typeCheck(self):
        if self.outputType != self.bodyNode.get_outputType():
            msg = "Failed typecheck on FunctionNode: {}\n"
            msg += "Make sure function's body has the same output "
            msg += "as the function's declared type:\n"
            msg += "Function {}'s declared type: {}\n"
            msg += "Body output type: {}\n"
            bodyOutputType = self.bodyNode.outputType
            if self.bodyNode.outputType == "":
                self.bodyNode.outputType = "None"
            msg = msg.format(self.identifierNode.get_value(), self.identifierNode.get_value(), self.outputType, self.bodyNode.outputType)
            return msg
        msg = self.check_formals()
        return msg

    def code_gen(self, line):#need to clean up comments here...
        current_function = str(self.identifierNode)
        self.start_address = line
        program = []
        #print( 'Function', current_function, 'is at', line)

        # frame_size represents the size of the stack frame, which might vary for each function
        # (1 space for return address, 1 for stack pointer, and one for each argument)
        frame_size = 3 + len(self.formals.get_formals())

        # Create a new starting point for temporary variables
        temp_vars.append(frame_size)

        program += self.bodyNode.code_gen(program, line)

        program.append('LD 7,0(6) : '+current_function+' FunctionNode line return')

        # Function has been generated, remove the temp var counter from the list
        temp_vars.pop( )

        # Insert an instruction which says return to the address of the caller
        return program
#end FunctionNode

class FormalsNode(ASTnode):
    def __init__(self, parameters):
        ASTnode.__init__(self)
        self.formals = []
        #inserting a set of tuples: (identifierNode, typeNode)
        while len(parameters) > 0:
            push(top(parameters), self.formals)
            pop(parameters)  # perhaps change this!!
        self.information = self.formals

    def __str__(self):
        self.returnString = " ("
        for pair in self.formals:
            self.returnString += str(pair[0]) + " : " + str(pair[1])
            if pair != self.formals[-1]:# !!! this could be a problem!
                self.returnString += ", "
        self.returnString += ")"
        return self.returnString

    def get_formals(self):
        return self.formals
#end FormalsNode


class BodyNode(ASTnode):
    def __init__(self, expressions):
        ASTnode.__init__(self)
        self.expressions = expressions
        self.information = self.expressions

    def __str__(self):
        returnString = str()
        for expression in self.expressions:
            returnString += str(expression) + "\n"
        returnString += "\n"
        return returnString

    def typeCheck(self):
        self.outputType = str()
        expressionSwitch = 0
        for node in self.expressions:
            if isinstance(node, ExpressionNode) or isinstance(node, BodyNode):
                if expressionSwitch == 0:
                    self.outputType = node.get_outputType()
                    expressionSwitch = 1
                elif expressionSwitch == 1:
                    if node.get_outputType() != self.outputType:
                        msg = "Failed typecheck on BodyNode"
                        msg.format()
                        return msg

    def code_gen(self, program, line):
        program = []
        for expression in reversed(self.expressions):
            program += expression.code_gen(program, line)
            line += 1
        return program
#end BodyNode


class ExpressionNode(ASTnode):
    def __init__(self, expression):
        ASTnode.__init__(self)
        self.expression = expression
        push(self.expression, self.information)

    def __str__(self):
        return " " + str(self.expression) + " "

    def typeCheck(self):
        self.outputType = self.expression.get_outputType()

    def code_gen(self, program, line):
        program = self.expression.code_gen(program, line)
        self.place = self.expression.place
        return program
#end ExpressionNode


class ActualsNode(ASTnode):
    def __init__(self, actuals_list):
        ASTnode.__init__(self)
        self.actuals = []  # list of expressions
        while (len(actuals_list) > 0):
            push(top(actuals_list), self.actuals)
            pop(actuals_list)
        self.information = self.actuals

    def __str__(self):
        self.returnString = str()
        for i in self.actuals:
            self.returnString += str(i)
            if i != self.actuals[-1]:  # !!! this could be a problem...
                self.returnString += ", "
        return self.returnString
#end ActualsNode


class FunctionCallNode(ASTnode):
    def __init__(self, functionName, arguments):
        ASTnode.__init__(self)
        self.actualsNode = arguments
        self.identifierNode = FunctionIdentifierNode(functionName)
        push(self.actualsNode, self.information)
        push(self.identifierNode, self.information)

    def __str__(self):
        self.returnString = str(self.identifierNode)
        self.returnString += " ("
        self.returnString += str(self.actualsNode)
        self.returnString += ")"
        return self.returnString

    def typeCheck(self):
        current_function = function_record[-1]
        if self.identifierNode.get_value() in function_table:
            self.outputType = function_table[self.identifierNode.get_value()]["functionNode"].get_outputType()
        else:
            msg = "Function call {} is undefined.\n"
            msg += "This function call occurs in {}.\n"
            msg = msg.format(self.identifierNode.get_value(),current_function)
            return msg

    def code_gen(self, a, b):
        program = []

        # First generate code for the expressions in the actual, saving the
        # values as temporary spots in the stack frame
        for actual in self.actualsNode.actuals:
            program += actual.code_gen(a,b)

        # Get the next open memory space in the stack (we will use this to find
        # the starting point for the next activation record)
        self.place = get_open_place()

        # Take each of the values we calculated from the actual parameters and
        # copy them into the stack frame of the function we are going to call
        for index, actual in enumerate(self.actualsNode.actuals):
            program.append( 'LD 5,' + str(actual.place) + '(6) ; load actual #' + str(index) )
            program.append( 'ST 5,' + str(self.place + 3 + index) + '(6)' )

        # (Compute and) Copy the return address into the new stack frame
        program.append( 'LDC 1,4(4)' )
        program.append( 'ADD 1,7,1' )
        program.append( 'ST 1,' + str(self.place) + '(6)' )

        # Save the (current) stack pointer into the next place in the activation record
        program.append( 'ST 6,' + str(self.place + 1) + '(6)')

        # Sets the (new) stack pointer to the start of the next activation record
        program.append( 'LDA 6,' + str(self.place) + '(6)' )

        # Add a placeholder instruction which says to load the address of the
        # desired function (in IMEM) into the program counter
        program.append( 'FUNCTION-CALL ' + self.identifierNode.get_value() )# str(function_table[self.identifierNode.get_value()]['functionNode'].start_address ))

        # At this point, the function will execute and store the value it
        # evaluates to in register 0, and then set the program counter back
        # to "here" so I can keep executing the following instructions:

        # Restore the stack pointer to its "old" value
        program.append( 'LD 6,1(6)')

        # Store the returned value to the stack frame
        program.append( 'ST 0,' + str(self.place) + '(6)' )

        return program

        #!!!! may have a logical error where the compiler accepts formals of the same name for a function declaration

#end FunctionCallNode


class PrintStatementNode(ASTnode):
    def __init__(self, expressions_list):
        ASTnode.__init__(self)
        self.expressions = expressions_list  # list of expression nodes
        self.information = self.expressions

    def __str__(self):
        self.returnString = "print("
        for expression in self.expressions:
            self.returnString += str(expression)
        self.returnString += ")"
        return self.returnString

    def code_gen(self, program, line):
        program = []
        for expr in self.expressions:
            program += expr.code_gen(program, line)
            program.append('OUT 0,0,0 : PrintStatementNode output')
        return program
#end PrintStatementNode

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

    def typeCheck(self):
        current_function = function_record[-1]
        if self.condition.get_outputType() == "boolean": #use outputType accessor here?
            if self.expr1.get_outputType() == self.expr2.get_outputType():
                self.outputType = self.expr1.get_outputType()
            else:
                msg = "If statement in function {} has inconsistent output type:\n"
                msg += "Then clause output type: {}\n"
                msg += "Else clause output type: {}\n"
                msg = msg.format(current_function, self.expr1.get_outputType(), self.expr2.get_outputType())
                return msg
        else:
            msg = "If statement requires a boolean conditional."
            msg = msg.format()
            return msg

    def code_gen(self, program, line):
        #An if statement is comprised of a conditional, then clause, and an else clause.
        condition_code = self.condition.code_gen(program,line)
        then_code = self.expr1.code_gen(program,line)
        else_code = self.expr2.code_gen(program,line)
        #add these to program where appropriate...

        self.place = get_open_place()

        #evaluate the condition:
        program = condition_code

        #decide what to do based on conditional result
            #if the result is 1, execute else_code
        else_start = str(len(then_code)+1)
        program = program + ['LD 0,' + str(self.condition.place) + '(6) : result of an if-statement condition',
                             'JEQ 0,'+else_start+'(7)']#if r0 is not zero, then jump to line x;
                             #line x might need to be dynamically generated...
                             #perhaps count the amount of lines that exist in then_code and else_code

        #execute the then clause
        program = program + then_code

        #jump to end of if statement
        else_end = str(len(else_code))
        program = program + ['LDA 7,'+else_end+'(7) : jump to next evaluation']

        lineXPosition = len(program)

        #execute the else clause
        program = program + else_code

        lineX = program[lineXPosition]
        newLineX = lineX + "; line x"

        program[lineXPosition] = newLineX

        #store the result of if statement
        program = program + ['ST 0,' + str(self.place) + '(6)']

        return program
    #end IfNode.code_gen()
#end IfNode


# --- Expressions have values... --- #
class ValueNode(ASTnode):
    def __init__(self, value):
        ASTnode.__init__(self)
        self.value = value
        push(self.value, self.information)

    def __str__(self):
        self.returnString = str(self.value)
        return self.returnString

    def get_value(self):
        return self.value
#end ValueNode


class IdentifierNode(ValueNode):
    def __init__(self, name):
        ValueNode.__init__(self, name)

    def typeCheck(self):
        existBool = 0
        current_function = function_record[-1]
        formals = function_table[current_function]["functionNode"].get_formals()
        for index, formal in enumerate(formals):
            if self.value == formal[0].get_value():
                existBool = 1
                self.outputType = formal[1].get_value()
                self.formal_position = index
        if existBool != 1:
            msg = "Identifier {} referred in {} has no declaration in function definition."
            msg = msg.format(self.value, current_function)
            return msg

    def code_gen(self,a,b):
        self.place = 3 + self.formal_position
        #identifiers will always be in an expressionnode...
        #this is a short term fix for outputting an actual through a print statement.
        #very ineffecient
        return ['LD 0,'+str(self.place)+'(6) : identifier load']
        return []
#end IdentifierNode


class FunctionIdentifierNode(IdentifierNode):
    def __init__(self, node):
        IdentifierNode.__init__(self, node.value)  # introduce some sort of accessor

    def typeCheck(self):
        pass
#end FunctionIdentifierNode


class NumberLiteralNode(ValueNode):
    def __init__(self, number):
        ValueNode.__init__(self, number)
        self.outputType = "integer"

    def code_gen(self, program, line):
        # Get a relative (to stack pointer) address to save this constant to
        self.place = get_open_place( )
        # Load the constant value into register 0, and then save this
        # register to the temporary variable location 'place'
        program = ['LDC 0,' + str(self.value) + '(4) : NumberLiteralNode constant',
                   'ST 0,' + str(self.place) + '(6) : NumberLiteralNode storage']
        return program
#end NumberLiteralNode


class BooleanLiteralNode(ValueNode):
    def __init__(self, boolValue):
        ValueNode.__init__(self, boolValue)
        self.outputType = "boolean"

    def code_gen(self, program, line):
        opCode_dict = {"true": "1", "false": "0"}
        self.place = get_open_place( )
        program = ['LDC 0,' + opCode_dict[self.value] + '(4) : BooleanLiteralNode value',
                   'ST 0,' + str(self.place) + '(6) : BooleanLiteralNode storage']
        return program
#end BooleanLiteralNode


class TypeNode(ValueNode):
    def __init__(self, typeValue):
        ValueNode.__init__(self, typeValue)
        self.outputType = typeValue  # !! possible introduction of another property type
#end TypeNode


#The remaining nodes are all subclasses of this Operator node
class Operator(ValueNode):
    def __init__(self, operand):
        ValueNode.__init__(self, operand)
        self.operatorType = str()
#end Operator superclass

class UnaryOperator(Operator):
    def __init__(self, operand):
        Operator.__init__(self, operand)
        self.operatorType = "UnaryOperator"

    def __str__(self):
        self.returnString = " " + self.operatorType + " "
        self.returnString += str(self.value) + " "
        return self.returnString

    def build_error(self):
        current_function = function_record[-1]
        msg = "{} expression within function {} expecting {}, received {}({})."
        msg = msg.format(self.operatorType, current_function, self.outputType, self.value, self.value.outputType)
        return msg
#end UnaryOperator superclass


# -- # Unary Operators:
class NotNode(UnaryOperator):
    def __init__(self, operand):
        UnaryOperator.__init__(self, operand)
        self.operatorType = "not"
        self.outputType = "boolean"

    def typeCheck(self):
        if self.value.outputType != "boolean":
            return self.build_error()

    def code_gen(self, program, line):
        program = self.value.code_gen(program, line)
        self.place = get_open_place()
        
        program = program + ['LD 0,'+str(self.value.place)+'(6)',
                             #if reg 0 is 1: store 1; else: store 0
                             'JEQ 0,3(7)',#jump if equal to zero
                             'LDC 0,0(4)',#not equal to zero thus change to zero
                             'ST 0,' + str(self.place) + '(6)',
                             'LDA 7,1(7)',
                             'LDC 0,1(4)',
                             'ST 0,' + str(self.place) + '(6)'
                             ]
        return program
#end NotNode


class NegationNode(UnaryOperator):
    def __init__(self, operand):
        UnaryOperator.__init__(self, operand)
        self.operatorType = "negate"
        self.outputType = "integer"

    def typeCheck(self):
        if self.value.outputType != "integer":
            return self.build_error()

    def code_gen(self, program, line):
        program = self.value.code_gen(program, line)#descend to a boolean literal
        self.place = get_open_place()
        
        program = program + ['LD 0,'+str(self.value.place)+'(6)',
                             'SUB 0,4,0',
                             'ST 0,'+str(self.place)+'(6)'
                             ]
        return program
#end NegationNode


class BinaryOperator(UnaryOperator):
    def __init__(self, leftOperand, rightOperand):
        self.operatorType = "BinaryOperator"
        UnaryOperator.__init__(self, rightOperand)
        self.value1 = leftOperand
        push(self.value1, self.information)
        self.get_value = self.get_values

    def __str__(self):
        self.returnString = str(self.value1) + " "
        self.returnString += self.operatorType + " "
        self.returnString += str(self.value) + " "
        return self.returnString

    def get_values(self):
        return (self.value1, self.value)

    def build_error(self):
        current_function = function_record[-1]
        msg = "{} expression within function {} expecting {}s, received {}({}) and {}({})."
        msg = msg.format(self.operatorType, current_function, self.outputType, self.value1, self.value1.outputType, self.value, self.value.outputType)
        return msg
#end BinaryOperator superclass


class BooleanConnective(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        # NotNode is excluded from this class
        self.outputType = "boolean"

    def typeCheck(self):
        if self.value.outputType != "boolean" or self.value1.outputType != "boolean":
            return self.build_error()
#end BooleanConnective superclass


class BooleanComparison(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        self.outputType = "boolean"

    def typeCheck(self):
        if self.value.outputType != "integer" or self.value1.outputType != "integer":
            return self.build_error()
#end BooleanComparison superclass


class ArithmeticOperation(BinaryOperator):
    def __init__(self, leftOperand, rightOperand):
        BinaryOperator.__init__(self, leftOperand, rightOperand)
        # NegateNode is excluded from this class
        self.outputType = "integer"

    def typeCheck(self):  # code duplication
        if self.value.outputType != "integer" or self.value1.outputType != "integer":
            return self.build_error()

    def code_gen(self, program, line):
        opCode_dict = {'+' : 'ADD', '-' : 'SUB', '*' : 'MUL', '/' : 'DIV'}
        left, right = super().get_values()
        
        # Generate the code for the left and right-hand sides of the addition
        # (also updating the 'place' values for both)
        program = left.code_gen(program, line) + right.code_gen(program, line)
        # Get the next open place for me to save the result of the addition
        self.place = get_open_place()
        # Load the values for the left and right sides into registers 0 and 1,
        # compute the sum, and save to self.place
        program = program + ['LD 0,' + str(left.place) + '(6) : ArithmeticOperation left operand',
                             'LD 1,' + str(right.place) + '(6) : ArithmeticOperation right operand',
                             opCode_dict[self.operatorType] +' 0,0,1', # Add registers 0 and 1, saving the result in register 0
                             'ST 0,' + str(self.place) + '(6)']
        return program
#end ArithmeticOperation superclass


class LessThanNode(BooleanComparison):
    def __init__(self, leftOperand, rightOperand):
        BooleanComparison.__init__(self, leftOperand, rightOperand)
        self.operatorType = "<"
        self.outputType = "boolean"

    def code_gen(self, program, line):
        right, left = super().get_values()
        program = left.code_gen(program,line) + right.code_gen(program, line)
        self.place = get_open_place()
        program = program + ['LD 0,' + str(left.place) + '(6) : LessThanNode left operand',
                             'LD 1,' + str(right.place) + '(6) : LessThanNode right operand',
                             #subtract r0 by r1. If the restult is less than zero, then r0 less than r1
                             'SUB 2,1,0',
                             'JLT 2,3(7) : jump to next line x',#if r0 is less than r1, then jump to line x,
                             'LDC 0,0(4) : LessThanNode evaluates to false',#load 0 into register 0; this test is false
                             'ST 0,' + str(self.place) + '(6)',
                             'LDA 7,2(7) : jump to next evaluation',#jump past else statement
                             'LDC 0,1(4) : line x; LessThanNode evaluates to true',#line x: load 1 into register 0; this test is true
                             'ST 0,' + str(self.place) + '(6)']
        return program
#end LessThanNode


class EqualToNode(BooleanComparison):
    def __init__(self, leftOperand, rightOperand):
        BooleanComparison.__init__(self, leftOperand, rightOperand)
        self.operatorType = "="
        self.outputType = "boolean"

    def code_gen(self, program, line):
        right, left = super().get_values()
        program = left.code_gen(program,line) + right.code_gen(program, line)
        self.place = get_open_place()
        program = program + ['LD 0,' + str(left.place) + '(6) : EqualNode left operand',
                             'LD 1,' + str(right.place) + '(6) : EqualNode right operand',
                             #subtract r0 by r1. If the result is not zero, then they are not equal
                             'SUB 2,0,1',
                             'JNE 2, 3(7) : jump to next line x',#if not equal to zero, go to line x
                             'LDC 0,1(4) : EqualNode evaluates to true', #load 1 into register 0; this test is true
                             'ST 0,' + str(self.place) + '(6)',
                             'LDA 7,2(7) : jump to next evaluation',#jump past else statement
                             'LDC 0,0(4) : line x; EqualNode evaluates to false', #line x: load 0 into register 0; this test is false
                             'ST 0,' + str(self.place) + '(6)']
        return program
#end EqualToNode


class OrNode(BooleanConnective):
    def __init__(self, leftOperand, rightOperand):
        BooleanConnective.__init__(self, leftOperand, rightOperand)
        self.operatorType = "or"
        self.outputType = "boolean"

    def code_gen(self, program, line):
        right, left = super().get_values()
        program = left.code_gen(program, line) + right.code_gen(program, line)
        self.place = get_open_place()
        program = program + ['LD 0,' + str(left.place) + '(6) : OrNode left operand',
                             'LD 1,' + str(right.place) + '(6) : OrNode right operand',
                             'JNE 0,4(7) : jump to next line x',#if left side is not zero, go to line x
                             'JNE 1,3(7) : jump to next line x',#if right side is not zero, go to line x
                             'LDC 0,0(4) : OrNode evaulates to false',#load 0 into register 0; this test is false
                             'ST 0,' + str(self.place) + '(6)',
                             'LDA 7,2(7) : jump to next evaluation',#jump past else statement
                             'LDC 0,1(4) : line x; OrNode evaulates to true',#line x: load 1 into register 0; this test is true
                             'ST 0,' + str(self.place) + '(6)']
        return program
#end OrNode


class PlusNode(ArithmeticOperation):
    def __init__(self, leftOperand, rightOperand):
        ArithmeticOperation.__init__(self, leftOperand, rightOperand)
        self.operatorType = "+"
        self.outputType = "integer"
#end PlusNode


class MinusNode(ArithmeticOperation):
    def __init__(self, leftOperand, rightOperand):
        ArithmeticOperation.__init__(self, leftOperand, rightOperand)
        self.operatorType = "-"
        self.outputType = "integer"
#end MinusNode


class AndNode(BooleanConnective):
    def __init__(self, leftOperand, rightOperand):
        BooleanConnective.__init__(self, leftOperand, rightOperand)
        self.operatorType = "and"
        self.outputType = "boolean"

    def code_gen(self,program,line):
        right, left = super().get_values()
        program = left.code_gen(program,line) + right.code_gen(program,line)
        self.place = get_open_place()
        program = program + ['LD 0,' + str(left.place) + '(6) : AndNode left operand',
                             'LD 1,' + str(right.place) + '(6) : AndNode right operand',
                             'JEQ 0,4(7) : jump to next line x',#if left is equal to 0, go to line x
                             'JEQ 1,3(7) : jump to next line x',#if right is equal to 0, go to line x
                             'LDC 0,1(4) : AndNode evaluates to true',#load 1 into register 0; this test is true
                             'ST 0,' + str(self.place) + '(6)',
                             'LDA 7,2(7) : jump to next evaulation',#jump past else statement
                             'LDC 0,0(4) : line x; AndNode evaulates to false',#line x: load 0 into register 0; this test is false
                             'ST 0,' + str(self.place) + '(6)']
        return program
#end AndNode


class MultiplyNode(ArithmeticOperation):
    def __init__(self, leftOperand, rightOperand):
        ArithmeticOperation.__init__(self, leftOperand, rightOperand)
        self.operatorType = "*"
        self.outputType = "integer"
#end MultiplyNode


class DivisionNode(ArithmeticOperation):
    def __init__(self, leftOperand, rightOperand):
        ArithmeticOperation.__init__(self, leftOperand, rightOperand)
        self.operatorType = "/"
        self.outputType = "integer"
#end DivisionNode
 
