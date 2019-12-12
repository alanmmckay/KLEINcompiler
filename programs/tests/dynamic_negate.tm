0: LD 1,1(0)
1: ST 1,4(6)
2: LD 1,2(0)
3: ST 1,5(6)
4: LDC 6,1(4)
5: LDC 1,2(4)
6: ADD 1,7,1
7: ST 1,0(6)
8: LDA 7,2(7)
9: OUT 0,0,0
10: HALT 0,0,0
11: LD 0,4(6) : identifier load
12: LDC 0,0(4) : NumberLiteralNode constant
13: ST 0,5(6) : NumberLiteralNode storage
14: LD 0,4(6) : LessThanNode left operand
15: LD 1,5(6) : LessThanNode right operand
16: SUB 2,1,0
17: JLT 2,3(7) : jump to next line x
18: LDC 0,0(4) : LessThanNode evaluates to false
19: ST 0,6(6)
20: LDA 7,2(7) : jump to next evaluation
21: LDC 0,1(4) : line x; LessThanNode evaluates to true
22: ST 0,6(6)
23: LD 0,6(6) : result of an if-statement condition
24: JEQ 0,25(7)
25: LD 0,3(6) : identifier load
26: LD 0,3(6)
27: OUT 4,0,0
28: SUB 0,4,0
29: ST 0,7(6)
30: LD 0,4(6) : identifier load
31: LDC 0,1(4) : NumberLiteralNode constant
32: ST 0,8(6) : NumberLiteralNode storage
33: LD 0,4(6) : ArithmeticOperation left operand
34: LD 1,8(6) : ArithmeticOperation right operand
35: SUB 0,0,1
36: ST 0,9(6)
37: LD 5,7(6) ; load actual #0
38: ST 5,13(6)
39: LD 5,9(6) ; load actual #1
40: ST 5,14(6)
41: LDC 1,4(4)
42: ADD 1,7,1
43: ST 1,10(6)
44: ST 6,11(6)
45: LDA 6,10(6)
46: LDC 7,11(4) : main FUNCTION-CALL
47: LD 6,1(6)
48: ST 0,10(6)
49: LDA 7,1(7) : jump to next evaluation
50: LD 0,3(6) : identifier load; line x
51: ST 0,11(6)
52: LD 7,0(6) : main FunctionNode line return
