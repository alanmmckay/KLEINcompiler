0: LDC 6,1(000)
1: LDC 1,2(000)
2: ADD 1,7,1
3: ST 1,0(6)
4: LDA 7,2(7)
5: OUT 0,0,0
6: HALT 0,0,0
7: LDC 0,1(000) : NumberLiteralNode constant
8: ST 0,3(6) : NumberLiteralNode storage
9: OUT 0,0,0 : PrintStatementNode output
10: LDC 0,1(000) : NumberLiteralNode constant
11: ST 0,4(6) : NumberLiteralNode storage
12: LD 7,0(6) : main FunctionNode line return
