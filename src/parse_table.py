from enum import Enum
from src.k_token import Token, TokenType


class NonTerminal(Enum):
    Program = 0
    Definitions = 1
    Def = 2
    Formals = 3
    Nonempty_Formals = 4
    Nonempty_Formals_t = 5
    Formal = 6
    Body = 7
    Type = 8
    Expr = 9
    Expr_p = 10
    Simple_Expr = 11
    Simple_Expr_t = 12
    Term = 13
    Term_t = 14
    Factor = 15
    Factor_t = 16
    Actuals = 17
    Nonempty_Actuals = 18
    Nonempty_Actuals_t = 19
    Literal = 20
    Print_Statement = 21

class Terminal(Enum):
    Function = 1
    OpenParen = 2
    CloseParen = 3
    Colon = 4
    Comma = 5
    Integer = 6
    Boolean = 7
    LessThan = 8
    Equals = 9
    Or = 10
    Plus = 11
    Minus = 12
    And = 13
    Mult = 14
    Divide = 15
    If = 16
    Then = 17
    Else = 18
    Not = 19
    Print = 20 

class StaticTerminal():
    def __init__(self, token):
        self.value = token.token_value
        if(self.value == "function"):
            self.value = Terminal.Function
        elif(self.value == "("):
            self.value = Terminal.OpenParen
        elif(self.value == ")"):
            self.value = Terminal.CloseParen
        elif(self.value == ":"):
            self.value = Terminal.Colon
        elif(self.value == ","):
            self.value = Terminal.Comma
        elif(self.value == "integer"):
            self.value = Terminal.Integer
        elif(self.value == "boolean"):
            self.value = Terminal.Boolean
        elif(self.value == "<"):
            self.value = Terminal.LessThan
        elif(self.value == "="):
            self.value = Terminal.Equals
        elif(self.value == "or"):
            self.value = Terminal.Or
        elif(self.value == "+"):
            self.value = Terminal.Plus
        elif(self.value == "-"):
            self.value = Terminal.Minus
        elif(self.value == "and"):
            self.value = Terminal.And
        elif(self.value == "*"):
            self.value = Terminal.Mult
        elif(self.value == "/"):
            self.value = Terminal.Divide
        elif(self.value == "if"):
            self.value = Terminal.If
        elif(self.value == "then"):
            self.value = Terminal.Then
        elif(self.value == "else"):
            self.value = Terminal.Else
        elif(self.value == "not"):
            self.value = Terminal.Not
        elif(self.value == "print"):
            self.value = Terminal.Print
        else:
            print(self.value)
            raise ValueError("Error in StaticTerminal Class!")
        
parse_table = {
               (NonTerminal.Program, Terminal.Function): [NonTerminal.Definitions],
               (NonTerminal.Definitions, Terminal.Function): [NonTerminal.Def, NonTerminal.Definitions],
               (NonTerminal.Definitions, TokenType.EOF): [],
               (NonTerminal.Def, Terminal.Function): [TokenType.KEYWORD, TokenType.WORD, TokenType.DELIMETER,
                                                      NonTerminal.Formals, TokenType.DELIMETER, TokenType.DELIMETER,
                                                      NonTerminal.Type, NonTerminal.Body],
               (NonTerminal.Formals, TokenType.WORD): [NonTerminal.Nonempty_Formals],
               (NonTerminal.Formals, Terminal.CloseParen): [],
               (NonTerminal.Nonempty_Formals, TokenType.WORD): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
               (NonTerminal.Nonempty_Formals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Formals],
               (NonTerminal.Nonempty_Formals_t, Terminal.CloseParen): [],
               (NonTerminal.Formal, TokenType.WORD): [TokenType.WORD, TokenType.DELIMETER, NonTerminal.Type],
               (NonTerminal.Body, Terminal.OpenParen): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.Minus): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.If): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.Not): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.NUMBER): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.BOOLEAN): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.WORD): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.Print): [NonTerminal.Print_Statement, NonTerminal.Body],
               (NonTerminal.Type, Terminal.Integer): [TokenType.KEYWORD],
               (NonTerminal.Type, Terminal.Boolean): [TokenType.KEYWORD],
               (NonTerminal.Expr, Terminal.OpenParen): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.NUMBER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.BOOLEAN): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.Minus): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.If): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.Not): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.WORD): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr_p, Terminal.Function): [],
               (NonTerminal.Expr_p, Terminal.CloseParen): [],
               (NonTerminal.Expr_p, Terminal.Comma): [],
               (NonTerminal.Expr_p, Terminal.LessThan): [TokenType.OPERATORS, NonTerminal.Expr],
               (NonTerminal.Expr_p, Terminal.Equals): [TokenType.OPERATORS, NonTerminal.Expr],
               (NonTerminal.Expr_p, Terminal.And): [],
               (NonTerminal.Expr_p, Terminal.Mult): [],
               (NonTerminal.Expr_p, Terminal.Divide): [],
               (NonTerminal.Expr_p, Terminal.Then): [],
               (NonTerminal.Expr_p, Terminal.Else): [],
               (NonTerminal.Simple_Expr, Terminal.OpenParen): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.NUMBER): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.BOOLEAN): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.Minus): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.If): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.Not): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.WORD): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr_t, Terminal.LessThan): [],
               (NonTerminal.Simple_Expr_t, Terminal.Equals): [],
               (NonTerminal.Simple_Expr_t, Terminal.Or): [TokenType.KEYWORD, NonTerminal.Simple_Expr],
               (NonTerminal.Simple_Expr_t, Terminal.Plus): [TokenType.OPERATORS, NonTerminal.Simple_Expr],
               (NonTerminal.Simple_Expr_t, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Simple_Expr],
               (NonTerminal.Term, Terminal.OpenParen): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.NUMBER): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.BOOLEAN): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.Minus): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.If): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.Not): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.WORD): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term_t, Terminal.Or): [],
               (NonTerminal.Term_t, Terminal.Plus): [],
               (NonTerminal.Term_t, Terminal.Minus): [],
               (NonTerminal.Term_t, Terminal.And): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Term_t, Terminal.Mult): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Term_t, Terminal.Divide): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Factor, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER],
               (NonTerminal.Factor, TokenType.NUMBER): [NonTerminal.Literal],
               (NonTerminal.Factor, TokenType.BOOLEAN): [NonTerminal.Literal],
               (NonTerminal.Factor, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Factor],
               (NonTerminal.Factor, Terminal.If): [TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD],
               (NonTerminal.Factor, Terminal.Not): [TokenType.KEYWORD, NonTerminal.Factor],
               (NonTerminal.Factor, TokenType.WORD): [TokenType.WORD, NonTerminal.Factor_t],
               (NonTerminal.Factor_t, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Actuals, TokenType.DELIMETER],
               (NonTerminal.Factor_t, Terminal.And): [],
               (NonTerminal.Factor_t, Terminal.Mult): [],
               (NonTerminal.Factor_t, Terminal.Divide): [],
               (NonTerminal.Actuals, TokenType.NUMBER): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, TokenType.BOOLEAN): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.Minus): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.If): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.Not): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, TokenType.WORD): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Nonempty_Actuals, TokenType.NUMBER): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, TokenType.BOOLEAN): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.Minus): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.If): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.Not): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, TokenType.WORD): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals_t, Terminal.OpenParen): [],
               (NonTerminal.Nonempty_Actuals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Actuals],
               (NonTerminal.Nonempty_Actuals_t, Terminal.OpenParen): [],
               (NonTerminal.Literal, TokenType.NUMBER): [TokenType.NUMBER],
               (NonTerminal.Literal, TokenType.BOOLEAN): [TokenType.BOOLEAN],
               (NonTerminal.Print_Statement, Terminal.Print): [TokenType.KEYWORD, TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER]
}
               
               
               
               
                                                       
