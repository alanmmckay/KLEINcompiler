from src.scanner import Scanner
from src.errors import ParseError
from src.parse_table import *
from src.k_token import Token, TokenType
from src.AST_node import *
from src.stack_operations import *


class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.debug_stack_string = str()
        self.debug_semantic_string = str()

    def parse(self):
        parse_stack = []
        semantic_stack = []

        push_rule([NonTerminal.Program, TokenType.EOF], parse_stack)
        while parse_stack:
            A = top(parse_stack)
            self.debug_stack_string += "Current Stack: " + str(parse_stack) + "\n"
            self.debug_stack_string += "Top of Stack: " + str(A) + "\n"
            if isinstance(A, TokenType):
                #print()
                #print(semantic_stack)
                t = self.scanner.next_token()
                #print(str(t.token_value) + " " + str(t.token_type))
                self.debug_stack_string += "Token Type: " + str(t.token_type) + "\n"
                self.debug_stack_string += "Token Value: " + str(t.token_value) + "\n"
                if A == t.token_type:
                    pop(parse_stack)
                    
                    #####################################
                    
                    #putting information worth keeping onto the stack
                    #this information will be housed within the relevant nodes
                    #Does this factor boolean literals and types?
                    if t.is_number() or t.is_word() or t.token_value == 'integer' or t.token_value == 'boolean' or t.token_value == 'true' or t.token_value == 'false':
                        push(t.value(), semantic_stack)
                        
                    #####################################
                    
                else:
                    msg = 'token mismatch: {} and {}'
                    msg = msg.format(A, t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            elif isinstance(A, NonTerminal):
                t = self.scanner.peek()
                self.debug_stack_string += "Token Type: " + str(t.token_type) + "\n"
                if ((t.token_type == TokenType.OPERATORS) or (t.token_type == TokenType.DELIMETER) or (
                        t.token_type == TokenType.KEYWORD)):
                    terminal = StaticTerminal(t)
                    terminal = terminal.value
                else:
                    terminal = t.token_type
                self.debug_stack_string += "Terminal Value: " + str(terminal) + "\n"
                self.debug_stack_string += "Indexing into table: " + str(A) + ", " + str(terminal) + "\n"
                rule = parse_table.get((A, terminal))
                if rule is not None:
                    pop(parse_stack)
                    push_rule(rule, parse_stack)
                else:
                    msg = 'cannot expand {} on {}'
                    msg = msg.format(A, t)
                    raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

            ################################################
            
            elif isinstance(A, SemanticAction):
                
                #decide which type of node needs to be made
                objectClass = class_factory.get(A)
                #print(objectClass)
                #create a node using that class
                node = nodeBuilder(semantic_stack,objectClass)
                #print(node)
                #put that node into the semantic stack
                push(node, semantic_stack)
                
                #pop the semantic rule off the parse stack
                pop(parse_stack)
                #print()
                self.debug_semantic_string += "---New Node: \n" 
                self.debug_semantic_string += str(type(top(semantic_stack))) + "\n"
                self.debug_semantic_string += str(node) + "\n\n"
                
            ###############################################

            else:
                msg = 'invalid item on parse_stack: {}'
                msg = msg.format(A)
                raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            self.debug_stack_string += "semantic stack: \n"
            '''for i in semantic_stack:
             self.debug_stack_string += str(i) + "\n"'''
            self.debug_stack_string += "\n"
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            msg = msg.format(t)
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        #################################################
        
        elif len(semantic_stack) != 1:
            msg = 'unexpected number of AST nodes: {}'
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        else:
            # print statement here for a check
            # print(self.debug_semantic_string)
            #print(semantic_stack)
            result = top(semantic_stack).process_node()
            if isinstance(result, list):
                msg = top(result).get_message()
                raise SemanticError(msg, self.scanner.get_program_string(),self.debug_semantic_string)
            return top(semantic_stack)
        
        ################################################

        # return True
