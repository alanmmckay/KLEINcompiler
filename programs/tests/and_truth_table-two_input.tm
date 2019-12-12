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
12: LD 0,3(6) : identifier load
13: LD 0,4(6) : AndNode left operand
14: LD 1,3(6) : AndNode right operand
15: JEQ 0,4(7) : jump to next line x
16: JEQ 1,3(7) : jump to next line x
17: LDC 0,1(4) : AndNode evaluates to true
18: ST 0,5(6)
19: LDA 7,2(7) : jump to next evaulation
20: LDC 0,0(4) : line x; AndNode evaulates to false
21: ST 0,5(6)
22: LD 7,0(6) : main FunctionNode line return
