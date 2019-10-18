from src.scanner import Scanner
from src.errors import ParseError
from src.parse_table import *
from src.k_token import Token, TokenType
from src.AST_node import ASTnode

def top(stack):
    return stack[-1]


def pop(stack):
    stack.pop()


def push_rule(lst, stack):
    for element in reversed(lst):
        stack.append(element)


def push(lst, stack):
    stack.append(lst)


class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.debug_stack_string = ""

    def parse(self):
        parse_stack = []
        semantic_stack = []

        push_rule([NonTerminal.Program, TokenType.EOF], parse_stack)
        while parse_stack:
            A = top(parse_stack)
            self.debug_stack_string += "Current Stack: " + str(parse_stack) + "\n"
            self.debug_stack_string += "Top of Stack: " + str(A) + "\n"
            if isinstance(A, TokenType):
                t = self.scanner.next_token()
                self.debug_stack_string += "Token Type: " + str(t.token_type) + "\n"
                self.debug_stack_string += "Token Value: " + str(t.token_value) + "\n"
                if A == t.token_type:
                    pop(parse_stack)
                    
                    #####################################
                    
                    #putting information worth keeping onto the stack
                    #this information will be housed within the relevant nodes
                    #Does this factor boolean literals and types?
                    if t.is_number() or t.is_word():
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
                objectClass = object_factory.get(A)
                
                print(objectClass)
                print(semantic_stack)
                print()
                
                #create a node using that class
                node = objectClass(semantic_stack)
                
                #put that node into the semantic stack
                push(node, semantic_stack)
                
                #pop the semantic rule off the parse stack
                pop(parse_stack)
                

                # need some sort of action in here, talks about it in session
                # 14 class notes
                
            ###############################################

            else:
                msg = 'invalid item on parse_stack: {}'
                msg = msg.format(A)
                raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)
            self.debug_stack_string += "\n"
        if not t.is_eof():
            msg = 'unexpected token at end: {}'
            msg = msg.format(t)
            raise ParseError(msg, self.scanner.get_program_string(), self.debug_stack_string)

        #################################################
        
        elif len(semantic_stack) != 1:
            #print("hello")
            msg = 'unexpected number of AST nodes: {}'
            # raise ParseError()

        else:
            # print statement here for a check
            print(semantic_stack)
            return top(semantic_stack)
        
        ################################################

        # return True
