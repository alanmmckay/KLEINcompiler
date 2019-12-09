0: LD 1,1(0)
1: ST 1,4(6)
2: LD 1,2(0)
3: ST 1,5(6)
4: LD 1,3(0)
5: ST 1,6(6)
6: LDC 6,1(000)
7: LDC 1,2(000)
8: ADD 1,7,1
9: ST 1,0(6)
10: LDA 7,2(7)
11: OUT 0,0,0
12: HALT 0,0,0
13: LD 0,3(6) : identifier load
14: OUT 0,0,0 : PrintStatementNode output
15: LD 0,5(6) : identifier load
16: LD 0,4(6) : NegationNode value, derived from number literal node
17: LD 0,3(6) : identifier load
18: LD 0,4(6) : ArithmeticOperation left operand
19: LD 1,3(6) : ArithmeticOperation right operand
20: ADD 0,0,1
21: ST 0,6(6)
22: LD 0,5(6) : ArithmeticOperation left operand
23: LD 1,6(6) : ArithmeticOperation right operand
24: MUL 0,0,1
25: ST 0,7(6)
26: LD 7,0(6) : main FunctionNode line return
