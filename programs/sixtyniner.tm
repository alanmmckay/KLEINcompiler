0: LD 1,1(0)
1: ST 1,4(6)
2: LD 1,2(0)
3: ST 1,5(6)
4: LDC 6,1(000)
5: LDC 1,2(000)
6: ADD 1,7,1
7: ST 1,0(6)
8: LDA 7,2(7)
9: OUT 0,0,0
10: HALT 0,0,0
11: OUT 0,0,0 : PrintStatementNode output
12: OUT 0,0,0 : PrintStatementNode output
13: LD 0,4(6) : AndNode left operand
14: LD 1,3(6) : AndNode right operand
15: JEQ 0,4(7) : jump to next line x
16: JEQ 1,3(7) : jump to next line x
17: LDC 0,1(000) : AndNode evaluates to true
18: ST 0,5(6)
19: LDA 7,2(7) : jump to next evaulation
20: LDC 0,0(000) : line x; AndNode evaulates to false
21: ST 0,5(6)
22: LD 0,5(6) : result of an if-statement condition
23: JEQ 0,3(7)
24: LDC 0,69(000) : NumberLiteralNode constant
25: ST 0,6(6) : NumberLiteralNode storage
26: LDA 7,2(7) : jump to next evaluation
27: LDC 0,96(000) : NumberLiteralNode constant; line x
28: ST 0,7(6) : NumberLiteralNode storage
29: ST 0,8(6)
30: LD 7,0(6) : main FunctionNode line return
