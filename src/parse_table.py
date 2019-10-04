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


parse_table = {(NonTerminal.Program, TokenType.KEYWORD): [NonTerminal.Definitions],
               (NonTerminal.Definitions, TokenType.KEYWORD): [NonTerminal.Def, NonTerminal.Definitions],
               (NonTerminal.Definitions, TokenType.EOF): [],
               (NonTerminal.Def, TokenType.KEYWORD): [TokenType.KEYWORD, TokenType.WORD, TokenType.DELIMETER,
                                                      NonTerminal.Formals, TokenType.DELIMETER, TokenType.DELIMETER,
                                                      NonTerminal.Type, NonTerminal.Body],
               (NonTerminal.Formals, TokenType.WORD): [NonTerminal.Nonempty_Formals],
               (NonTerminal.Formals, TokenType.DELIMETER): [TokenType.DELIMETER],#---#
               (NonTerminal.Nonempty_Formals, TokenType.WORD): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
               (NonTerminal.Nonempty_Formals_t, TokenType.DELIMETER): [TokenType.DELIMETER, NonTerminal.Nonempty_Formals],
               (NonTerminal.Nonempty_Formals_t, TokenType.DELIMETER): [TokenType.DELIMETER],#---#
               (NonTerminal.Formal, TokenType.WORD): [TokenType.WORD, TokenType.DELIMETER, NonTerminal.Type],
               (NonTerminal.Body, TokenType.DELIMETER): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.NUMBER): [NonTerminal.Expr],#
               (NonTerminal.Body, TokenType.BOOLEAN): [NonTerminal.Expr],#
               (NonTerminal.Body, TokenType.OPERATOR): [NonTerminal.Expr],#
               (NonTerminal.Body, TokenType.KEYWORD): [NonTerminal.Expr],#
               (NonTerminal.Body, TokenType.PRIMITIVE): [NonTerminal.Print_Statement, NonTerminal.Body],
               (NonTerminal.Type, TokenType.KEYWORD): [TokenType.KEYWORD],
               (NonTerminal.Expr, TokenType.DELIMITER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.NUMBER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.BOOLEAN): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.DELIMITER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.KEYWORD): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr_p, TokenType.KEYWORD): [TokenType.KEYWORD],
               (NonTerminal.Expr_p, TokenType.DELIMETER): [TokenType.DELIMITER],
               (NonTerminal.Expr_p, TokenType.OPERATORS): [TokenType.OPERATORS, NonTerminal.Expr],
               
                                                       
