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
    function = 1
    openParen = 2
    closeParen = 3
    colon = 4
    comma = 5
    integer = 6
    boolean = 7
    lessThan = 8
    equals = 9
    orr = 10
    plus = 11
    minus = 12
    andd = 13
    mult = 14
    divide = 15
    iif = 16
    then = 17
    eelse = 18
    nnot = 19
    pprint = 20
    
parse_table = {
               (NonTerminal.Program, Terminal.function): [NonTerminal.Definitions],
               (NonTerminal.Definitions, Terminal.function): [NonTerminal.Def, NonTerminal.Definitions],
               (NonTerminal.Definitions, TokenType.EOF): [],
               (NonTerminal.Def, TokenType.function): [TokenType.KEYWORD, TokenType.WORD, TokenType.DELIMETER,
                                                      NonTerminal.Formals, TokenType.DELIMETER, TokenType.DELIMETER,
                                                      NonTerminal.Type, NonTerminal.Body],
               (NonTerminal.Formals, TokenType.WORD): [NonTerminal.Nonempty_Formals],
               (NonTerminal.Formals, Terminal.closeParen): [],
               (NonTerminal.Nonempty_Formals, TokenType.WORD): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
               (NonTerminal.Nonempty_Formals_t, Terminal.comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Formals],
               (NonTerminal.Nonempty_Formals_t, Terminal.closeParen): [],
               (NonTerminal.Formal, TokenType.WORD): [TokenType.WORD, TokenType.DELIMETER, NonTerminal.Type],
               (NonTerminal.Body, Terminal.openParen): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.minus): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.iif): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.nnot): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.NUMBER): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.BOOLEAN): [NonTerminal.Expr],
               (NonTerminal.Body, TokenType.WORD): [NonTerminal.Expr],
               (NonTerminal.Body, Terminal.pprint): [NonTerminal.Print_Statement, NonTerminal.Body],
               (NonTerminal.Type, Terminal.integer): [TokenType.KEYWORD],
               (NonTerminal.Type, Terminal.boolean): [TokenType.KEYWORD],
               (NonTerminal.Expr, Terminal.openParen): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.NUMBER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.BOOLEAN): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.minus): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.iif): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, Terminal.nnot): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr, TokenType.WORD): [NonTerminal.Simple_Expr, NonTerminal.Expr_p],
               (NonTerminal.Expr_p, Terminal.function): [],
               (NonTerminal.Expr_p, Terminal.closeParen): [],
               (NonTerminal.Expr_p, Terminal.comma): [],
               (NonTerminal.Expr_p, Terminal.lessThan): [TokenType.OPERATORS, NonTerminal.Expr],
               (NonTerminal.Expr_p, Terminal.equals): [TokenType.OPERATORS, NonTerminal.Expr],
               (NonTerminal.Expr_p, Terminal.andd): [],
               (NonTerminal.Expr_p, Terminal.mult): [],
               (NonTerminal.Expr_p, Terminal.divide): [],
               (NonTerminal.Expr_p, Terminal.then): [],
               (NonTerminal.Expr_p, Terminal.eelse): [],
               (NonTerminal.Simple_Expr, Terminal.openParen): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.NUMBER): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.BOOLEAN): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.minus): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.iif): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, Terminal.nnot): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr, TokenType.WORD): [NonTerminal.Term, NonTerminal.Simple_Expr_t],
               (NonTerminal.Simple_Expr_t, Terminal.lessThan): [],
               (NonTerminal.Simple_Expr_t, Terminal.equals): [],
               (NonTerminal.Simple_Expr_t, Terminal.orr): [TokenType.KEYWORD, NonTerminal.Simple_Expr],
               (NonTerminal.Simple_Expr_t, Terminal.plus): [TokenType.OPERATORS, NonTerminal.Simple_Expr],
               (NonTerminal.Simple_Expr_t, Terminal.minus): [TokenType.OPERATORS, NonTerminal.Simple_Expr],
               (NonTerminal.Term, Terminal.openParen): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.NUMBER): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.BOOLEAN): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.minus): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.iif): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, Terminal.nnot): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term, TokenType.WORD): [NonTerminal.Factor, NonTerminal.Term_t],
               (NonTerminal.Term_t, Terminal.orr): [],
               (NonTerminal.Term_t, Terminal.plus): [],
               (NonTerminal.Term_t, Terminal.minus): [],
               (NonTerminal.Term_t, Terminal.andd): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Term_t, Terminal.mult): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Term_t, Terminal.divide): [TokenType.OPERATORS, NonTerminal.Term],
               (NonTerminal.Factor, Terminal.openParen): [TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER],
               (NonTerminal.Factor, TokenType.NUMBER): [NonTerminal.Literal],
               (NonTerminal.Factor, TokenType.BOOLEAN): [NonTerminal.Literal],
               (NonTerminal.Factor, Terminal.minus): [TokenType.OPERATORS, NonTerminal.Factor],
               (NonTerminal.Factor, Terminal.iif): [TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD],
               (NonTerminal.Factor, Terminal.nnot): [TokenType.KEYWORD, NonTerminal.Factor],
               (NonTerminal.Factor, TokenType.WORD): [TokenType.WORD, NonTerminal.Factor_t],
               (NonTerminal.Factor_t, Terminal.openParen): [TokenType.DELIMETER, NonTerminal.Actuals, TokenType.DELIMETER],
               (NonTerminal.Factor_t, Terminal.andd): [],
               (NonTerminal.Factor_t, Terminal.mult): [],
               (NonTerminal.Factor_t, Terminal.divide): [],
               (NonTerminal.Actuals, TokenType.NUMBER): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, TokenType.BOOLEAN): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.minus): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.iif): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, Terminal.nnot): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Actuals, TokenType.WORD): [NonTerminal.Nonempty_Actuals],
               (NonTerminal.Nonempty_Actuals, TokenType.NUMBER): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, TokenType.BOOLEAN): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.minus): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.iif): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, Terminal.nnot): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals, TokenType.WORD): [NonTerminal.Expr, Nonempty_Actuals_t],
               (NonTerminal.Nonempty_Actuals_t, Terminal.openParen): [],
               (NonTerminal.Nonempty_Actuals_t, Terminal.comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Actuals],
               (NonTerminal.Nonempty_Actuals_t, Terminal.openParen): [],
               (NonTerminal.Literal, TokenType.NUMBER): [TokenType.NUMBER],
               (NonTerminal.Literal, TokenType.BOOLEAN): [TokenType.BOOLEAN],
               (NonTerminal.Print_Statement, Terminal.pprint): [TokenType.KEYWORD, TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER]
}
               
               
               
               
                                                       
