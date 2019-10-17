from enum import Enum
from src.k_token import Token, TokenType
from src import AST_node


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
    Function = 100
    OpenParen = 200
    CloseParen = 300
    Colon = 400
    Comma = 500
    Integer = 600
    Boolean = 700
    LessThan = 800
    Equals = 900
    Or = 1000
    Plus = 1100
    Minus = 1200
    And = 1300
    Mult = 1400
    Divide = 1500
    If = 1600
    Then = 1700
    Else = 1800
    Not = 1900
    Print = 2000


class StaticTerminal():
    def __init__(self, token):
        self.value = token.token_value
        if (self.value == "function"):
            self.value = Terminal.Function
        elif (self.value == "("):
            self.value = Terminal.OpenParen
        elif (self.value == ")"):
            self.value = Terminal.CloseParen
        elif (self.value == ":"):
            self.value = Terminal.Colon
        elif (self.value == ","):
            self.value = Terminal.Comma
        elif (self.value == "integer"):
            self.value = Terminal.Integer
        elif (self.value == "boolean"):
            self.value = Terminal.Boolean
        elif (self.value == "<"):
            self.value = Terminal.LessThan
        elif (self.value == "="):
            self.value = Terminal.Equals
        elif (self.value == "or"):
            self.value = Terminal.Or
        elif (self.value == "+"):
            self.value = Terminal.Plus
        elif (self.value == "-"):
            self.value = Terminal.Minus
        elif (self.value == "and"):
            self.value = Terminal.And
        elif (self.value == "*"):
            self.value = Terminal.Mult
        elif (self.value == "/"):
            self.value = Terminal.Divide
        elif (self.value == "if"):
            self.value = Terminal.If
        elif (self.value == "then"):
            self.value = Terminal.Then
        elif (self.value == "else"):
            self.value = Terminal.Else
        elif (self.value == "not"):
            self.value = Terminal.Not
        elif (self.value == "print"):
            self.value = Terminal.Print
        else:
            msg = "Error in StaticTerminal class.\n"
            msg += "Token: {}\n".format(token)
            raise ValueError(msg)


parse_table = {
    (NonTerminal.Program, Terminal.Function): [NonTerminal.Definitions, AST_node.Definitions],
    (NonTerminal.Definitions, Terminal.Function): [NonTerminal.Def, NonTerminal.Definitions],
    (NonTerminal.Definitions, TokenType.EOF): [],
    (NonTerminal.Def, Terminal.Function): [TokenType.KEYWORD, TokenType.WORD, AST_node.Identifier, TokenType.DELIMETER,
                                           NonTerminal.Formals, TokenType.DELIMETER, TokenType.DELIMETER,
                                           NonTerminal.Type, NonTerminal.Body, AST_node.Function],
    (NonTerminal.Formals, TokenType.WORD): [NonTerminal.Nonempty_Formals, AST_node.Formals],
    (NonTerminal.Formals, Terminal.CloseParen): [],
    (NonTerminal.Nonempty_Formals, TokenType.WORD): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
    (NonTerminal.Nonempty_Formals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Formals],
    (NonTerminal.Nonempty_Formals_t, Terminal.CloseParen): [],
    (NonTerminal.Formal, TokenType.WORD): [TokenType.WORD, AST_node.Identifier, TokenType.DELIMETER, NonTerminal.Type,
                                           AST_node.Formal],
    (NonTerminal.Body, Terminal.OpenParen): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Minus): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.If): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Not): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.NUMBER): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.BOOLEAN): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.WORD): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Print): [NonTerminal.Print_Statement, NonTerminal.Body, AST_node.Body],
    (NonTerminal.Type, Terminal.Integer): [TokenType.KEYWORD, AST_node.Type],
    (NonTerminal.Type, Terminal.Boolean): [TokenType.KEYWORD, AST_node.Type],
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
    (NonTerminal.Expr_p, Terminal.LessThan): [TokenType.OPERATORS, NonTerminal.Expr, AST_node.LessThan],
    (NonTerminal.Expr_p, Terminal.Equals): [TokenType.OPERATORS, NonTerminal.Expr, AST_node.EqualTo],
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
    (NonTerminal.Simple_Expr_t, Terminal.Or): [TokenType.KEYWORD, NonTerminal.Simple_Expr, AST_node.OrExpr],
    (NonTerminal.Simple_Expr_t, Terminal.Plus): [TokenType.OPERATORS, NonTerminal.Simple_Expr, AST_node.PlusExpr],
    (NonTerminal.Simple_Expr_t, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Simple_Expr, AST_node.MinusExpr],
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
    (NonTerminal.Term_t, Terminal.And): [TokenType.KEYWORD, NonTerminal.Term, AST_node.AndExpr],
    (NonTerminal.Term_t, Terminal.Mult): [TokenType.OPERATORS, NonTerminal.Term, AST_node.TimesExpr],
    (NonTerminal.Term_t, Terminal.Divide): [TokenType.OPERATORS, NonTerminal.Term, AST_node.DivideExpr],
    (NonTerminal.Factor, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER],
    (NonTerminal.Factor, TokenType.NUMBER): [NonTerminal.Literal],
    (NonTerminal.Factor, TokenType.BOOLEAN): [NonTerminal.Literal],
    (NonTerminal.Factor, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Factor, AST_node.Negate],
    (NonTerminal.Factor, Terminal.If): [TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD, NonTerminal.Expr,
                                        TokenType.KEYWORD, NonTerminal.Expr, AST_node.IfStatement],
    (NonTerminal.Factor, Terminal.Not): [TokenType.KEYWORD, NonTerminal.Factor, AST_node.NotExpr],
    (NonTerminal.Factor, TokenType.WORD): [TokenType.WORD, AST_node.Identifier, NonTerminal.Factor_t],
    (NonTerminal.Factor_t, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Actuals, TokenType.DELIMETER, AST_node.FunctionCall],
    (NonTerminal.Factor_t, Terminal.And): [],
    (NonTerminal.Factor_t, Terminal.Mult): [],
    (NonTerminal.Factor_t, Terminal.Divide): [],
    (NonTerminal.Actuals, TokenType.NUMBER): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Actuals, TokenType.BOOLEAN): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Actuals, Terminal.Minus): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Actuals, Terminal.If): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Actuals, Terminal.Not): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Actuals, TokenType.WORD): [NonTerminal.Nonempty_Actuals, AST_node.Actuals],
    (NonTerminal.Nonempty_Actuals, TokenType.NUMBER): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, TokenType.BOOLEAN): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.Minus): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.If): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.Not): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, TokenType.WORD): [NonTerminal.Expr, AST_node.Nea, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals_t, Terminal.CloseParen): [],
    (NonTerminal.Nonempty_Actuals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Actuals],
    (NonTerminal.Literal, TokenType.NUMBER): [TokenType.NUMBER, AST_node.NumberLiteral],
    (NonTerminal.Literal, TokenType.BOOLEAN): [TokenType.BOOLEAN, AST_node.BooleanLiteral],
    (NonTerminal.Print_Statement, Terminal.Print): [TokenType.KEYWORD, TokenType.DELIMETER, NonTerminal.Expr,
                                                    TokenType.DELIMETER, AST_node.PrintStatement],
    (NonTerminal.Program, TokenType.EOF): [],
    (NonTerminal.Nonempty_Formals, Terminal.CloseParen): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
    (NonTerminal.Expr_p, Terminal.Or): [],
    (NonTerminal.Expr_p, Terminal.Plus): [],
    (NonTerminal.Expr_p, Terminal.Minus): [],
    # (NonTerminal.Expr_p, Terminal.And): [],
    (NonTerminal.Expr_p, TokenType.EOF): [],
    (NonTerminal.Simple_Expr_t, Terminal.And): [],
    (NonTerminal.Simple_Expr_t, Terminal.Mult): [],
    (NonTerminal.Simple_Expr_t, Terminal.Divide): [],
    # (NonTerminal.Simple_Expr_t , Terminal.Or): [],
    # (NonTerminal.Simple_Expr_t , Terminal.Plus): [],
    # (NonTerminal.Simple_Expr_t , Terminal.Minus): [],
    (NonTerminal.Simple_Expr_t, Terminal.And): [],
    (NonTerminal.Simple_Expr_t, Terminal.Function): [],
    (NonTerminal.Simple_Expr_t, Terminal.Then): [],
    (NonTerminal.Simple_Expr_t, Terminal.Else): [],
    (NonTerminal.Simple_Expr_t, Terminal.CloseParen): [],
    (NonTerminal.Simple_Expr_t, Terminal.Comma): [],
    (NonTerminal.Simple_Expr_t, TokenType.EOF): [],
    (NonTerminal.Term_t, Terminal.Function): [],
    (NonTerminal.Term_t, Terminal.CloseParen): [],
    (NonTerminal.Term_t, Terminal.Comma): [],
    (NonTerminal.Term_t, Terminal.LessThan): [],
    (NonTerminal.Term_t, Terminal.Equals): [],
    (NonTerminal.Term_t, Terminal.Then): [],
    (NonTerminal.Term_t, Terminal.Else): [],
    (NonTerminal.Term_t, TokenType.EOF): [],
    (NonTerminal.Factor_t, Terminal.Or): [],
    (NonTerminal.Factor_t, Terminal.Plus): [],
    (NonTerminal.Factor_t, Terminal.Minus): [],
    (NonTerminal.Factor_t, Terminal.LessThan): [],
    (NonTerminal.Factor_t, Terminal.Equals): [],
    (NonTerminal.Factor_t, Terminal.Function): [],
    (NonTerminal.Factor_t, Terminal.Then): [],
    (NonTerminal.Factor_t, Terminal.Else): [],
    (NonTerminal.Factor_t, Terminal.CloseParen): [],
    (NonTerminal.Factor_t, Terminal.Comma): [],
    (NonTerminal.Factor_t, TokenType.EOF): [],
    (NonTerminal.Actuals, Terminal.OpenParen): [NonTerminal.Nonempty_Actuals],
    (NonTerminal.Nonempty_Actuals, Terminal.OpenParen): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Body, TokenType.EOF): []
}
# should there be a (NonTerminal.Program, TokenType.EOF) index?
