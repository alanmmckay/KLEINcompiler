from enum import Enum
from src.k_token import Token, TokenType
from src.AST_node import *


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
    Function = 0
    OpenParen = 1
    CloseParen = 2
    Colon = 3
    Comma = 4
    Integer = 5
    Boolean = 6
    LessThan = 7
    Equals = 8
    Or = 9
    Plus = 10
    Minus = 11
    And = 12
    Mult = 13
    Divide = 14
    If = 15
    Then = 16
    Else = 17
    Not = 18
    Print = 19


class SemanticAction(Enum):
    MakeDefinitions = 0
    MakeIdentifier = 1
    MakeFunction = 2
    MakeFormals = 3
    MakeFormal = 4
    MakeBody = 5
    MakeType = 6
    MakeLessThan = 7
    MakeEqualTo = 8
    MakePlus = 9
    MakeMinus = 10
    MakeAnd = 11
    MakeMultiply = 12
    MakeDivision = 13
    MakeNegation = 14
    MakeIf = 15
    MakeNot = 16
    MakeFunctionCall = 17
    MakeActuals = 18
    MakeNonEmptyActuals = 19
    MakeNumberLiteral = 20
    MakeBooleanLiteral = 21
    MakePrintStatement = 22
    MakeOr = 23
    MakeExpression = 24
    

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
        
object_factory = {
    SemanticAction.MakeDefinitions: DefinitionsNode,
    SemanticAction.MakeIdentifier: IdentifierNode,
    SemanticAction.MakeFunction: FunctionNode,
    SemanticAction.MakeFormals: FormalsNode,
    #SemanticAction.MakeFormal: FormalNode,
    SemanticAction.MakeBody: BodyNode,
    SemanticAction.MakeType: TypeNode,
    SemanticAction.MakeLessThan: LessThanNode,
    SemanticAction.MakeEqualTo: EqualToNode,
    SemanticAction.MakePlus: PlusNode,
    SemanticAction.MakeMinus: MinusNode,
    SemanticAction.MakeAnd: AndNode,
    SemanticAction.MakeMultiply: MultiplyNode,
    SemanticAction.MakeDivision: DivisionNode,
    SemanticAction.MakeNegation: NegationNode,
    SemanticAction.MakeIf: IfNode,
    SemanticAction.MakeNot: NotNode,
    SemanticAction.MakeFunctionCall: FunctionCallNode,
    SemanticAction.MakeActuals: ActualsNode,
    #SemanticAction.MakeNonEmptyActuals: NonEmptyActualsNode,
    SemanticAction.MakeNumberLiteral: NumberLiteralNode,
    SemanticAction.MakeBooleanLiteral: BooleanLiteralNode,
    SemanticAction.MakePrintStatement: PrintStatementNode,
    SemanticAction.MakeOr: OrNode,
    SemanticAction.MakeExpression : ExpressionNode
}    
            

parse_table = {
    (NonTerminal.Program, Terminal.Function): [NonTerminal.Definitions, SemanticAction.MakeDefinitions],
    (NonTerminal.Definitions, Terminal.Function): [NonTerminal.Def, NonTerminal.Definitions],
    (NonTerminal.Definitions, TokenType.EOF): [],
    (NonTerminal.Def, Terminal.Function): [TokenType.KEYWORD, TokenType.WORD, SemanticAction.MakeIdentifier, TokenType.DELIMETER, NonTerminal.Formals, TokenType.DELIMETER, TokenType.DELIMETER, NonTerminal.Type, NonTerminal.Body, SemanticAction.MakeFunction],
    (NonTerminal.Formals, TokenType.WORD): [NonTerminal.Nonempty_Formals, SemanticAction.MakeFormals],
    (NonTerminal.Formals, Terminal.CloseParen): [],
    (NonTerminal.Nonempty_Formals, TokenType.WORD): [NonTerminal.Formal, NonTerminal.Nonempty_Formals_t],
    (NonTerminal.Nonempty_Formals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Formals],
    (NonTerminal.Nonempty_Formals_t, Terminal.CloseParen): [],
    (NonTerminal.Formal, TokenType.WORD): [TokenType.WORD, SemanticAction.MakeIdentifier, TokenType.DELIMETER, NonTerminal.Type],
    (NonTerminal.Body, Terminal.OpenParen): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Minus): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.If): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Not): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.NUMBER): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.BOOLEAN): [NonTerminal.Expr],
    (NonTerminal.Body, TokenType.WORD): [NonTerminal.Expr],
    (NonTerminal.Body, Terminal.Print): [NonTerminal.Print_Statement, NonTerminal.Body, SemanticAction.MakeBody],
    (NonTerminal.Type, Terminal.Integer): [TokenType.KEYWORD, SemanticAction.MakeType],
    (NonTerminal.Type, Terminal.Boolean): [TokenType.KEYWORD, SemanticAction.MakeType],
    (NonTerminal.Expr, Terminal.OpenParen): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, TokenType.NUMBER): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, TokenType.BOOLEAN): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, Terminal.Minus): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, Terminal.If): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, Terminal.Not): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr, TokenType.WORD): [NonTerminal.Simple_Expr, NonTerminal.Expr_p, SemanticAction.MakeExpression],
    (NonTerminal.Expr_p, Terminal.Function): [],
    (NonTerminal.Expr_p, Terminal.CloseParen): [],
    (NonTerminal.Expr_p, Terminal.Comma): [],
    (NonTerminal.Expr_p, Terminal.LessThan): [TokenType.OPERATORS, NonTerminal.Expr, SemanticAction.MakeLessThan],
    (NonTerminal.Expr_p, Terminal.Equals): [TokenType.OPERATORS, NonTerminal.Expr, SemanticAction.MakeEqualTo],
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
    (NonTerminal.Simple_Expr_t, Terminal.Or): [TokenType.KEYWORD, NonTerminal.Simple_Expr, SemanticAction.MakeOr],
    (NonTerminal.Simple_Expr_t, Terminal.Plus): [TokenType.OPERATORS, NonTerminal.Simple_Expr, SemanticAction.MakePlus],
    (NonTerminal.Simple_Expr_t, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Simple_Expr, SemanticAction.MakeMinus],
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
    (NonTerminal.Term_t, Terminal.And): [TokenType.KEYWORD, NonTerminal.Term, SemanticAction.MakeAnd],
    (NonTerminal.Term_t, Terminal.Mult): [TokenType.OPERATORS, NonTerminal.Term, SemanticAction.MakeMultiply],
    (NonTerminal.Term_t, Terminal.Divide): [TokenType.OPERATORS, NonTerminal.Term, SemanticAction.MakeDivision],
    (NonTerminal.Factor, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Expr, TokenType.DELIMETER],
    (NonTerminal.Factor, TokenType.NUMBER): [NonTerminal.Literal],
    (NonTerminal.Factor, TokenType.BOOLEAN): [NonTerminal.Literal],
    (NonTerminal.Factor, Terminal.Minus): [TokenType.OPERATORS, NonTerminal.Factor, SemanticAction.MakeNegation],
    (NonTerminal.Factor, Terminal.If): [TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD, NonTerminal.Expr, TokenType.KEYWORD, NonTerminal.Expr, SemanticAction.MakeIf],
    (NonTerminal.Factor, Terminal.Not): [TokenType.KEYWORD, NonTerminal.Factor, SemanticAction.MakeNot],
    (NonTerminal.Factor, TokenType.WORD): [TokenType.WORD, SemanticAction.MakeIdentifier, NonTerminal.Factor_t],
    (NonTerminal.Factor_t, Terminal.OpenParen): [TokenType.DELIMETER, NonTerminal.Actuals, TokenType.DELIMETER, SemanticAction.MakeFunctionCall],
    (NonTerminal.Factor_t, Terminal.And): [],
    (NonTerminal.Factor_t, Terminal.Mult): [],
    (NonTerminal.Factor_t, Terminal.Divide): [],
    (NonTerminal.Actuals, TokenType.NUMBER): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Actuals, TokenType.BOOLEAN): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Actuals, Terminal.Minus): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Actuals, Terminal.If): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Actuals, Terminal.Not): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Actuals, TokenType.WORD): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Nonempty_Actuals, TokenType.NUMBER): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, TokenType.BOOLEAN): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.Minus): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.If): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, Terminal.Not): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals, TokenType.WORD): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Nonempty_Actuals_t, Terminal.CloseParen): [],
    (NonTerminal.Nonempty_Actuals_t, Terminal.Comma): [TokenType.DELIMETER, NonTerminal.Nonempty_Actuals],
    (NonTerminal.Literal, TokenType.NUMBER): [TokenType.NUMBER, SemanticAction.MakeNumberLiteral],
    (NonTerminal.Literal, TokenType.BOOLEAN): [TokenType.BOOLEAN, SemanticAction.MakeBooleanLiteral],
    (NonTerminal.Print_Statement, Terminal.Print): [TokenType.KEYWORD, TokenType.DELIMETER, NonTerminal.Expr,
                                                    TokenType.DELIMETER, SemanticAction.MakePrintStatement],
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
    (NonTerminal.Actuals, Terminal.OpenParen): [NonTerminal.Nonempty_Actuals, SemanticAction.MakeActuals],
    (NonTerminal.Nonempty_Actuals, Terminal.OpenParen): [NonTerminal.Expr, NonTerminal.Nonempty_Actuals_t],
    (NonTerminal.Body, TokenType.EOF): []
}
# should there be a (NonTerminal.Program, TokenType.EOF) index?
