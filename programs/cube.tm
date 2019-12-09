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
10: LDA 7,35(7)
11: OUT 0,0,0
12: HALT 0,0,0
13: LD 0,4(6) : ArithmeticOperation left operand
14: LD 1,3(6) : ArithmeticOperation right operand
15: MUL 0,0,1
16: ST 0,5(6)
17: LD 7,0(6) : multiply FunctionNode line return
18: LD 5,3(6) ; load actual #0
19: ST 5,7(6)
20: LD 5,3(6) ; load actual #1
21: ST 5,8(6)
22: LDC 1,4(000)
23: ADD 1,7,1
24: ST 1,4(6)
25: ST 6,5(6)
26: LDA 6,4(6)
27: LDC 7,13(000) : multiply FUNCTION-CALL
28: LD 6,1(6)
29: ST 0,4(6)
30: LD 7,0(6) : identity FunctionNode line return
31: LD 5,3(6) ; load actual #0
32: ST 5,7(6)
33: LDC 1,4(000)
34: ADD 1,7,1
35: ST 1,4(6)
36: ST 6,5(6)
37: LDA 6,4(6)
38: LDC 7,18(000) : identity FUNCTION-CALL
39: LD 6,1(6)
40: ST 0,4(6)
41: LD 0,4(6) : ArithmeticOperation left operand
42: LD 1,3(6) : ArithmeticOperation right operand
43: MUL 0,0,1
44: ST 0,5(6)
45: LD 7,0(6) : cube FunctionNode line return
46: LD 5,3(6) ; load actual #0
47: ST 5,9(6)
48: LDC 1,4(000)
49: ADD 1,7,1
50: ST 1,6(6)
51: ST 6,7(6)
52: LDA 6,6(6)
53: LDC 7,31(000) : cube FUNCTION-CALL
54: LD 6,1(6)
55: ST 0,6(6)
56: LD 7,0(6) : main FunctionNode line return
