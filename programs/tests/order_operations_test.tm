0: LDC 6,1(000)
1: LDC 1,2(000)
2: ADD 1,7,1
3: ST 1,0(6)
4: LDA 7,2(7)
5: OUT 0,0,0
6: HALT 0,0,0
7: LDC 0,12(000) : NumberLiteralNode constant
8: ST 0,3(6) : NumberLiteralNode storage
9: LDC 0,3(000) : NumberLiteralNode constant
10: ST 0,4(6) : NumberLiteralNode storage
11: LD 0,3(6) : ArithmeticOperation left operand
12: LD 1,4(6) : ArithmeticOperation right operand
13: SUB 0,0,1
14: ST 0,5(6)
15: LDC 0,3(000) : NumberLiteralNode constant
16: ST 0,6(6) : NumberLiteralNode storage
17: LDC 0,9(000) : NumberLiteralNode constant
18: ST 0,7(6) : NumberLiteralNode storage
19: LD 0,6(6) : ArithmeticOperation left operand
20: LD 1,7(6) : ArithmeticOperation right operand
21: MUL 0,0,1
22: ST 0,8(6)
23: LD 0,5(6) : ArithmeticOperation left operand
24: LD 1,8(6) : ArithmeticOperation right operand
25: DIV 0,0,1
26: ST 0,9(6)
27: LD 7,0(6) : main FunctionNode line return
