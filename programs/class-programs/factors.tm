0: LD 1,1(0)
1: ST 1,4(6)
2: LDC 6,1(000)
3: LDC 1,2(000)
4: ADD 1,7,1
5: ST 1,0(6)
6: LDA 7,171(7)
7: OUT 0,0,0
8: HALT 0,0,0
9: LD 0,4(6) : identifier load
10: LD 0,3(6) : identifier load
11: LD 0,4(6) : LessThanNode left operand
12: LD 1,3(6) : LessThanNode right operand
13: SUB 2,1,0
14: JLT 2,3(7) : jump to next line x
15: LDC 0,0(000) : LessThanNode evaluates to false
16: ST 0,5(6)
17: LDA 7,2(7) : jump to next evaluation
18: LDC 0,1(5) : line x; LessThanNode evaluates to true
19: ST 0,5(6)
20: LD 0,5(6) : result of an if-statement condition
21: JEQ 0,2(7)
22: LD 0,3(6) : identifier load
23: LDA 7,19(7) : jump to next evaluation
24: LD 0,4(6) : identifier load; line x
25: LD 0,3(6) : identifier load
26: LD 0,4(6) : ArithmeticOperation left operand
27: LD 1,3(6) : ArithmeticOperation right operand
28: SUB 0,0,1
29: ST 0,6(6)
30: LD 0,4(6) : identifier load
31: LD 5,6(6) ; load actual #0
32: ST 5,10(6)
33: LD 5,4(6) ; load actual #1
34: ST 5,11(6)
35: LDC 1,4(000)
36: ADD 1,7,1
37: ST 1,7(6)
38: ST 6,8(6)
39: LDA 6,7(6)
40: LDC 7,9(000) : remainder FUNCTION-CALL
41: LD 6,1(6)
42: ST 0,7(6)
43: ST 0,8(6)
44: LD 7,0(6) : remainder FunctionNode line return
45: LDC 0,0(000) : NumberLiteralNode constant
46: ST 0,5(6) : NumberLiteralNode storage
47: LD 0,4(6) : identifier load
48: LD 0,3(6) : identifier load
49: LD 5,4(6) ; load actual #0
50: ST 5,9(6)
51: LD 5,3(6) ; load actual #1
52: ST 5,10(6)
53: LDC 1,4(000)
54: ADD 1,7,1
55: ST 1,6(6)
56: ST 6,7(6)
57: LDA 6,6(6)
58: LDC 7,9(000) : remainder FUNCTION-CALL
59: LD 6,1(6)
60: ST 0,6(6)
61: LD 0,5(6) : EqualNode left operand
62: LD 1,6(6) : EqualNode right operand
63: SUB 2,0,1
64: JNE 2, 3(7) : jump to next line x
65: LDC 0,1(000) : EqualNode evaluates to true
66: ST 0,7(6)
67: LDA 7,2(7) : jump to next evaluation
68: LDC 0,0(000) : line x; EqualNode evaluates to false
69: ST 0,7(6)
70: LD 7,0(6) : divides FunctionNode line return
71: LD 0,4(6) : identifier load
72: OUT 0,0,0 : PrintStatementNode output
73: LD 0,3(6) : identifier load
74: LDC 0,1(000) : NumberLiteralNode constant
75: ST 0,5(6) : NumberLiteralNode storage
76: LD 0,4(6) : identifier load
77: LD 0,5(6) : ArithmeticOperation left operand
78: LD 1,4(6) : ArithmeticOperation right operand
79: ADD 0,0,1
80: ST 0,6(6)
81: LD 5,3(6) ; load actual #0
82: ST 5,10(6)
83: LD 5,6(6) ; load actual #1
84: ST 5,11(6)
85: LDC 1,4(000)
86: ADD 1,7,1
87: ST 1,7(6)
88: ST 6,8(6)
89: LDA 6,7(6)
90: LDC 7,147(000) : loopToN FUNCTION-CALL
91: LD 6,1(6)
92: ST 0,7(6)
93: LD 7,0(6) : printAndLoop FunctionNode line return
94: LD 0,4(6) : identifier load
95: LD 0,3(6) : identifier load
96: LD 5,4(6) ; load actual #0
97: ST 5,8(6)
98: LD 5,3(6) ; load actual #1
99: ST 5,9(6)
100: LDC 1,4(000)
101: ADD 1,7,1
102: ST 1,5(6)
103: ST 6,6(6)
104: LDA 6,5(6)
105: LDC 7,45(000) : divides FUNCTION-CALL
106: LD 6,1(6)
107: ST 0,5(6)
108: LD 0,5(6) : result of an if-statement condition
109: JEQ 0,15(7)
110: LD 0,3(6) : identifier load
111: LD 0,4(6) : identifier load
112: LD 5,3(6) ; load actual #0
113: ST 5,9(6)
114: LD 5,4(6) ; load actual #1
115: ST 5,10(6)
116: LDC 1,4(000)
117: ADD 1,7,1
118: ST 1,6(6)
119: ST 6,7(6)
120: LDA 6,6(6)
121: LDC 7,71(000) : printAndLoop FUNCTION-CALL
122: LD 6,1(6)
123: ST 0,6(6)
124: LDA 7,20(7) : jump to next evaluation
125: LD 0,3(6) : identifier load; line x
126: LDC 0,1(000) : NumberLiteralNode constant
127: ST 0,7(6) : NumberLiteralNode storage
128: LD 0,4(6) : identifier load
129: LD 0,7(6) : ArithmeticOperation left operand
130: LD 1,4(6) : ArithmeticOperation right operand
131: ADD 0,0,1
132: ST 0,8(6)
133: LD 5,3(6) ; load actual #0
134: ST 5,12(6)
135: LD 5,8(6) ; load actual #1
136: ST 5,13(6)
137: LDC 1,4(000)
138: ADD 1,7,1
139: ST 1,9(6)
140: ST 6,10(6)
141: LDA 6,9(6)
142: LDC 7,147(000) : loopToN FUNCTION-CALL
143: LD 6,1(6)
144: ST 0,9(6)
145: ST 0,10(6)
146: LD 7,0(6) : testAndLoop FunctionNode line return
147: LD 0,4(6) : identifier load
148: LD 0,3(6) : identifier load
149: LD 0,4(6) : EqualNode left operand
150: LD 1,3(6) : EqualNode right operand
151: SUB 2,0,1
152: JNE 2, 3(7) : jump to next line x
153: LDC 0,1(000) : EqualNode evaluates to true
154: ST 0,5(6)
155: LDA 7,2(7) : jump to next evaluation
156: LDC 0,0(000) : line x; EqualNode evaluates to false
157: ST 0,5(6)
158: LD 0,5(6) : result of an if-statement condition
159: JEQ 0,2(7)
160: LD 0,3(6) : identifier load
161: LDA 7,14(7) : jump to next evaluation
162: LD 0,3(6) : identifier load; line x
163: LD 0,4(6) : identifier load
164: LD 5,3(6) ; load actual #0
165: ST 5,9(6)
166: LD 5,4(6) ; load actual #1
167: ST 5,10(6)
168: LDC 1,4(000)
169: ADD 1,7,1
170: ST 1,6(6)
171: ST 6,7(6)
172: LDA 6,6(6)
173: LDC 7,94(000) : testAndLoop FUNCTION-CALL
174: LD 6,1(6)
175: ST 0,6(6)
176: ST 0,7(6)
177: LD 7,0(6) : loopToN FunctionNode line return
178: LD 0,3(6) : identifier load
179: LDC 0,1(000) : NumberLiteralNode constant
180: ST 0,4(6) : NumberLiteralNode storage
181: LD 5,3(6) ; load actual #0
182: ST 5,8(6)
183: LD 5,4(6) ; load actual #1
184: ST 5,9(6)
185: LDC 1,4(000)
186: ADD 1,7,1
187: ST 1,5(6)
188: ST 6,6(6)
189: LDA 6,5(6)
190: LDC 7,147(000) : loopToN FUNCTION-CALL
191: LD 6,1(6)
192: ST 0,5(6)
193: LD 7,0(6) : main FunctionNode line return
