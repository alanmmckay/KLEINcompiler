0: LD 1,1(0)
1: ST 1,4(6)
2: LDC 6,1(4)
3: LDC 1,2(4)
4: ADD 1,7,1
5: ST 1,0(6)
6: LDA 7,584(7)
7: OUT 0,0,0
8: HALT 0,0,0
9: LD 0,4(6) : identifier load
10: LD 0,3(6) : identifier load
11: LD 0,4(6) : LessThanNode left operand
12: LD 1,3(6) : LessThanNode right operand
13: SUB 2,1,0
14: JLT 2,3(7) : jump to next line x
15: LDC 0,0(4) : LessThanNode evaluates to false
16: ST 0,5(6)
17: LDA 7,2(7) : jump to next evaluation
18: LDC 0,1(4) : line x; LessThanNode evaluates to true
19: ST 0,5(6)
20: LD 0,5(6) : result of an if-statement condition
21: JEQ 0,2(7)
22: LD 0,3(6) : identifier load
23: LDA 7,19(7) : jump to next evaluation
24: LD 0,3(6) : identifier load; line x
25: LD 0,4(6) : identifier load
26: LD 0,3(6) : ArithmeticOperation left operand
27: LD 1,4(6) : ArithmeticOperation right operand
28: SUB 0,0,1
29: ST 0,6(6)
30: LD 0,4(6) : identifier load
31: LD 5,6(6) ; load actual #0
32: ST 5,10(6)
33: LD 5,4(6) ; load actual #1
34: ST 5,11(6)
35: LDC 1,4(4)
36: ADD 1,7,1
37: ST 1,7(6)
38: ST 6,8(6)
39: LDA 6,7(6)
40: LDC 7,9(4) : mod FUNCTION-CALL
41: LD 6,1(6)
42: ST 0,7(6)
43: ST 0,8(6)
44: LD 7,0(6) : mod FunctionNode line return
45: LDC 0,0(4) : NumberLiteralNode constant
46: ST 0,5(6) : NumberLiteralNode storage
47: LD 0,4(6) : identifier load
48: LD 0,3(6) : identifier load
49: LD 5,4(6) ; load actual #0
50: ST 5,9(6)
51: LD 5,3(6) ; load actual #1
52: ST 5,10(6)
53: LDC 1,4(4)
54: ADD 1,7,1
55: ST 1,6(6)
56: ST 6,7(6)
57: LDA 6,6(6)
58: LDC 7,9(4) : mod FUNCTION-CALL
59: LD 6,1(6)
60: ST 0,6(6)
61: LD 0,5(6) : EqualNode left operand
62: LD 1,6(6) : EqualNode right operand
63: SUB 2,0,1
64: JNE 2, 3(7) : jump to next line x
65: LDC 0,1(4) : EqualNode evaluates to true
66: ST 0,7(6)
67: LDA 7,2(7) : jump to next evaluation
68: LDC 0,0(4) : line x; EqualNode evaluates to false
69: ST 0,7(6)
70: LD 7,0(6) : divides FunctionNode line return
71: LD 0,4(6) : identifier load
72: LD 0,3(6) : identifier load
73: LD 0,4(6) : LessThanNode left operand
74: LD 1,3(6) : LessThanNode right operand
75: SUB 2,1,0
76: JLT 2,3(7) : jump to next line x
77: LDC 0,0(4) : LessThanNode evaluates to false
78: ST 0,5(6)
79: LDA 7,2(7) : jump to next evaluation
80: LDC 0,1(4) : line x; LessThanNode evaluates to true
81: ST 0,5(6)
82: LD 0,5(6) : result of an if-statement condition
83: JEQ 0,44(7)
84: LD 0,3(6) : identifier load
85: LDC 0,1(4) : NumberLiteralNode constant
86: ST 0,6(6) : NumberLiteralNode storage
87: LD 0,3(6) : ArithmeticOperation left operand
88: LD 1,6(6) : ArithmeticOperation right operand
89: ADD 0,0,1
90: ST 0,7(6)
91: LD 0,4(6) : identifier load
92: LD 5,7(6) ; load actual #0
93: ST 5,11(6)
94: LD 5,4(6) ; load actual #1
95: ST 5,12(6)
96: LDC 1,4(4)
97: ADD 1,7,1
98: ST 1,8(6)
99: ST 6,9(6)
100: LDA 6,8(6)
101: LDC 7,71(4) : hasDivisorFrom FUNCTION-CALL
102: LD 6,1(6)
103: ST 0,8(6)
104: LD 0,3(6) : identifier load
105: LD 0,4(6) : identifier load
106: LD 5,3(6) ; load actual #0
107: ST 5,12(6)
108: LD 5,4(6) ; load actual #1
109: ST 5,13(6)
110: LDC 1,4(4)
111: ADD 1,7,1
112: ST 1,9(6)
113: ST 6,10(6)
114: LDA 6,9(6)
115: LDC 7,45(4) : divides FUNCTION-CALL
116: LD 6,1(6)
117: ST 0,9(6)
118: LD 0,8(6) : OrNode left operand
119: LD 1,9(6) : OrNode right operand
120: JNE 0,4(7) : jump to next line x
121: JNE 1,3(7) : jump to next line x
122: LDC 0,0(4) : OrNode evaulates to false
123: ST 0,10(6)
124: LDA 7,2(7) : jump to next evaluation
125: LDC 0,1(4) : line x; OrNode evaulates to true
126: ST 0,10(6)
127: LDA 7,2(7) : jump to next evaluation
128: LDC 0,0(4) : BooleanLiteralNode value; line x
129: ST 0,11(6) : BooleanLiteralNode storage
130: ST 0,12(6)
131: LD 7,0(6) : hasDivisorFrom FunctionNode line return
132: LDC 0,2(4) : NumberLiteralNode constant
133: ST 0,4(6) : NumberLiteralNode storage
134: LD 0,3(6) : identifier load
135: LD 5,4(6) ; load actual #0
136: ST 5,8(6)
137: LD 5,3(6) ; load actual #1
138: ST 5,9(6)
139: LDC 1,4(4)
140: ADD 1,7,1
141: ST 1,5(6)
142: ST 6,6(6)
143: LDA 6,5(6)
144: LDC 7,71(4) : hasDivisorFrom FUNCTION-CALL
145: LD 6,1(6)
146: ST 0,5(6)
147: LD 0,5(6)
148: JEQ 0,3(7)
149: LDC 0,0(4)
150: ST 0,6(6)
151: LDA 7,1(7)
152: LDC 0,1(4)
153: ST 0,6(6)
154: LD 7,0(6) : isPrime FunctionNode line return
155: LDC 0,0(4) : NumberLiteralNode constant
156: ST 0,5(6) : NumberLiteralNode storage
157: LD 0,3(6) : identifier load
158: LDC 0,10(4) : NumberLiteralNode constant
159: ST 0,6(6) : NumberLiteralNode storage
160: LD 0,3(6) : ArithmeticOperation left operand
161: LD 1,6(6) : ArithmeticOperation right operand
162: DIV 0,0,1
163: ST 0,7(6)
164: LD 0,5(6) : EqualNode left operand
165: LD 1,7(6) : EqualNode right operand
166: SUB 2,0,1
167: JNE 2, 3(7) : jump to next line x
168: LDC 0,1(4) : EqualNode evaluates to true
169: ST 0,8(6)
170: LDA 7,2(7) : jump to next evaluation
171: LDC 0,0(4) : line x; EqualNode evaluates to false
172: ST 0,8(6)
173: LD 0,8(6) : result of an if-statement condition
174: JEQ 0,2(7)
175: LD 0,4(6) : identifier load
176: LDA 7,26(7) : jump to next evaluation
177: LD 0,3(6) : identifier load; line x
178: LDC 0,10(4) : NumberLiteralNode constant
179: ST 0,9(6) : NumberLiteralNode storage
180: LD 0,3(6) : ArithmeticOperation left operand
181: LD 1,9(6) : ArithmeticOperation right operand
182: DIV 0,0,1
183: ST 0,10(6)
184: LD 0,4(6) : identifier load
185: LDC 0,1(4) : NumberLiteralNode constant
186: ST 0,11(6) : NumberLiteralNode storage
187: LD 0,4(6) : ArithmeticOperation left operand
188: LD 1,11(6) : ArithmeticOperation right operand
189: ADD 0,0,1
190: ST 0,12(6)
191: LD 5,10(6) ; load actual #0
192: ST 5,16(6)
193: LD 5,12(6) ; load actual #1
194: ST 5,17(6)
195: LDC 1,4(4)
196: ADD 1,7,1
197: ST 1,13(6)
198: ST 6,14(6)
199: LDA 6,13(6)
200: LDC 7,155(4) : log10Helper FUNCTION-CALL
201: LD 6,1(6)
202: ST 0,13(6)
203: ST 0,14(6)
204: LD 7,0(6) : log10Helper FunctionNode line return
205: LD 0,3(6) : identifier load
206: LDC 0,0(4) : NumberLiteralNode constant
207: ST 0,4(6) : NumberLiteralNode storage
208: LD 5,3(6) ; load actual #0
209: ST 5,8(6)
210: LD 5,4(6) ; load actual #1
211: ST 5,9(6)
212: LDC 1,4(4)
213: ADD 1,7,1
214: ST 1,5(6)
215: ST 6,6(6)
216: LDA 6,5(6)
217: LDC 7,155(4) : log10Helper FUNCTION-CALL
218: LD 6,1(6)
219: ST 0,5(6)
220: LD 7,0(6) : log10 FunctionNode line return
221: LDC 0,0(4) : NumberLiteralNode constant
222: ST 0,6(6) : NumberLiteralNode storage
223: LD 0,4(6) : identifier load
224: LD 0,6(6) : EqualNode left operand
225: LD 1,4(6) : EqualNode right operand
226: SUB 2,0,1
227: JNE 2, 3(7) : jump to next line x
228: LDC 0,1(4) : EqualNode evaluates to true
229: ST 0,7(6)
230: LDA 7,2(7) : jump to next evaluation
231: LDC 0,0(4) : line x; EqualNode evaluates to false
232: ST 0,7(6)
233: LD 0,7(6) : result of an if-statement condition
234: JEQ 0,3(7)
235: LDC 0,1(4) : NumberLiteralNode constant
236: ST 0,8(6) : NumberLiteralNode storage
237: LDA 7,45(7) : jump to next evaluation
238: LDC 0,1(4) : NumberLiteralNode constant; line x
239: ST 0,9(6) : NumberLiteralNode storage
240: LD 0,4(6) : identifier load
241: LD 0,9(6) : EqualNode left operand
242: LD 1,4(6) : EqualNode right operand
243: SUB 2,0,1
244: JNE 2, 3(7) : jump to next line x
245: LDC 0,1(4) : EqualNode evaluates to true
246: ST 0,10(6)
247: LDA 7,2(7) : jump to next evaluation
248: LDC 0,0(4) : line x; EqualNode evaluates to false
249: ST 0,10(6)
250: LD 0,10(6) : result of an if-statement condition
251: JEQ 0,2(7)
252: LD 0,5(6) : identifier load
253: LDA 7,28(7) : jump to next evaluation
254: LD 0,3(6) : identifier load; line x
255: LD 0,4(6) : identifier load
256: LDC 0,1(4) : NumberLiteralNode constant
257: ST 0,11(6) : NumberLiteralNode storage
258: LD 0,4(6) : ArithmeticOperation left operand
259: LD 1,11(6) : ArithmeticOperation right operand
260: SUB 0,0,1
261: ST 0,12(6)
262: LD 0,3(6) : identifier load
263: LD 0,5(6) : identifier load
264: LD 0,3(6) : ArithmeticOperation left operand
265: LD 1,5(6) : ArithmeticOperation right operand
266: MUL 0,0,1
267: ST 0,13(6)
268: LD 5,3(6) ; load actual #0
269: ST 5,17(6)
270: LD 5,12(6) ; load actual #1
271: ST 5,18(6)
272: LD 5,13(6) ; load actual #2
273: ST 5,19(6)
274: LDC 1,4(4)
275: ADD 1,7,1
276: ST 1,14(6)
277: ST 6,15(6)
278: LDA 6,14(6)
279: LDC 7,221(4) : powHelper FUNCTION-CALL
280: LD 6,1(6)
281: ST 0,14(6)
282: ST 0,15(6)
283: ST 0,16(6)
284: LD 7,0(6) : powHelper FunctionNode line return
285: LD 0,3(6) : identifier load
286: LD 0,4(6) : identifier load
287: LD 0,3(6) : identifier load
288: LD 5,3(6) ; load actual #0
289: ST 5,8(6)
290: LD 5,4(6) ; load actual #1
291: ST 5,9(6)
292: LD 5,3(6) ; load actual #2
293: ST 5,10(6)
294: LDC 1,4(4)
295: ADD 1,7,1
296: ST 1,5(6)
297: ST 6,6(6)
298: LDA 6,5(6)
299: LDC 7,221(4) : powHelper FUNCTION-CALL
300: LD 6,1(6)
301: ST 0,5(6)
302: LD 7,0(6) : pow FunctionNode line return
303: LD 0,3(6) : identifier load
304: LDC 0,10(4) : NumberLiteralNode constant
305: ST 0,4(6) : NumberLiteralNode storage
306: LD 0,3(6) : ArithmeticOperation left operand
307: LD 1,4(6) : ArithmeticOperation right operand
308: DIV 0,0,1
309: ST 0,5(6)
310: LD 0,3(6) : identifier load
311: LDC 0,10(4) : NumberLiteralNode constant
312: ST 0,6(6) : NumberLiteralNode storage
313: LD 5,3(6) ; load actual #0
314: ST 5,10(6)
315: LD 5,6(6) ; load actual #1
316: ST 5,11(6)
317: LDC 1,4(4)
318: ADD 1,7,1
319: ST 1,7(6)
320: ST 6,8(6)
321: LDA 6,7(6)
322: LDC 7,9(4) : mod FUNCTION-CALL
323: LD 6,1(6)
324: ST 0,7(6)
325: LDC 0,10(4) : NumberLiteralNode constant
326: ST 0,8(6) : NumberLiteralNode storage
327: LD 0,3(6) : identifier load
328: LD 5,3(6) ; load actual #0
329: ST 5,12(6)
330: LDC 1,4(4)
331: ADD 1,7,1
332: ST 1,9(6)
333: ST 6,10(6)
334: LDA 6,9(6)
335: LDC 7,205(4) : log10 FUNCTION-CALL
336: LD 6,1(6)
337: ST 0,9(6)
338: LD 5,8(6) ; load actual #0
339: ST 5,13(6)
340: LD 5,9(6) ; load actual #1
341: ST 5,14(6)
342: LDC 1,4(4)
343: ADD 1,7,1
344: ST 1,10(6)
345: ST 6,11(6)
346: LDA 6,10(6)
347: LDC 7,285(4) : pow FUNCTION-CALL
348: LD 6,1(6)
349: ST 0,10(6)
350: LD 0,7(6) : ArithmeticOperation left operand
351: LD 1,10(6) : ArithmeticOperation right operand
352: MUL 0,0,1
353: ST 0,11(6)
354: LD 0,5(6) : ArithmeticOperation left operand
355: LD 1,11(6) : ArithmeticOperation right operand
356: ADD 0,0,1
357: ST 0,12(6)
358: LD 7,0(6) : rotate FunctionNode line return
359: LD 0,3(6) : identifier load
360: OUT 0,0,0 : PrintStatementNode output
361: LDC 0,1(4) : BooleanLiteralNode value
362: ST 0,4(6) : BooleanLiteralNode storage
363: LD 7,0(6) : report FunctionNode line return
364: LDC 0,0(4) : NumberLiteralNode constant
365: ST 0,5(6) : NumberLiteralNode storage
366: LD 0,4(6) : identifier load
367: LD 0,5(6) : EqualNode left operand
368: LD 1,4(6) : EqualNode right operand
369: SUB 2,0,1
370: JNE 2, 3(7) : jump to next line x
371: LDC 0,1(4) : EqualNode evaluates to true
372: ST 0,6(6)
373: LDA 7,2(7) : jump to next evaluation
374: LDC 0,0(4) : line x; EqualNode evaluates to false
375: ST 0,6(6)
376: LD 0,6(6) : result of an if-statement condition
377: JEQ 0,3(7)
378: LDC 0,1(4) : BooleanLiteralNode value
379: ST 0,7(6) : BooleanLiteralNode storage
380: LDA 7,50(7) : jump to next evaluation
381: LD 0,3(6) : identifier load; line x
382: LD 5,3(6) ; load actual #0
383: ST 5,11(6)
384: LDC 1,4(4)
385: ADD 1,7,1
386: ST 1,8(6)
387: ST 6,9(6)
388: LDA 6,8(6)
389: LDC 7,303(4) : rotate FUNCTION-CALL
390: LD 6,1(6)
391: ST 0,8(6)
392: LD 0,4(6) : identifier load
393: LDC 0,1(4) : NumberLiteralNode constant
394: ST 0,9(6) : NumberLiteralNode storage
395: LD 0,4(6) : ArithmeticOperation left operand
396: LD 1,9(6) : ArithmeticOperation right operand
397: SUB 0,0,1
398: ST 0,10(6)
399: LD 5,8(6) ; load actual #0
400: ST 5,14(6)
401: LD 5,10(6) ; load actual #1
402: ST 5,15(6)
403: LDC 1,4(4)
404: ADD 1,7,1
405: ST 1,11(6)
406: ST 6,12(6)
407: LDA 6,11(6)
408: LDC 7,364(4) : isCircularPrimeHelper FUNCTION-CALL
409: LD 6,1(6)
410: ST 0,11(6)
411: LD 0,3(6) : identifier load
412: LD 5,3(6) ; load actual #0
413: ST 5,15(6)
414: LDC 1,4(4)
415: ADD 1,7,1
416: ST 1,12(6)
417: ST 6,13(6)
418: LDA 6,12(6)
419: LDC 7,132(4) : isPrime FUNCTION-CALL
420: LD 6,1(6)
421: ST 0,12(6)
422: LD 0,11(6) : AndNode left operand
423: LD 1,12(6) : AndNode right operand
424: JEQ 0,4(7) : jump to next line x
425: JEQ 1,3(7) : jump to next line x
426: LDC 0,1(4) : AndNode evaluates to true
427: ST 0,13(6)
428: LDA 7,2(7) : jump to next evaulation
429: LDC 0,0(4) : line x; AndNode evaulates to false
430: ST 0,13(6)
431: ST 0,14(6)
432: LD 7,0(6) : isCircularPrimeHelper FunctionNode line return
433: LD 0,3(6) : identifier load
434: LD 0,3(6) : identifier load
435: LD 5,3(6) ; load actual #0
436: ST 5,7(6)
437: LDC 1,4(4)
438: ADD 1,7,1
439: ST 1,4(6)
440: ST 6,5(6)
441: LDA 6,4(6)
442: LDC 7,205(4) : log10 FUNCTION-CALL
443: LD 6,1(6)
444: ST 0,4(6)
445: LDC 0,1(4) : NumberLiteralNode constant
446: ST 0,5(6) : NumberLiteralNode storage
447: LD 0,4(6) : ArithmeticOperation left operand
448: LD 1,5(6) : ArithmeticOperation right operand
449: ADD 0,0,1
450: ST 0,6(6)
451: LD 5,3(6) ; load actual #0
452: ST 5,10(6)
453: LD 5,6(6) ; load actual #1
454: ST 5,11(6)
455: LDC 1,4(4)
456: ADD 1,7,1
457: ST 1,7(6)
458: ST 6,8(6)
459: LDA 6,7(6)
460: LDC 7,364(4) : isCircularPrimeHelper FUNCTION-CALL
461: LD 6,1(6)
462: ST 0,7(6)
463: LD 0,7(6) : result of an if-statement condition
464: JEQ 0,12(7)
465: LD 0,3(6) : identifier load
466: LD 5,3(6) ; load actual #0
467: ST 5,11(6)
468: LDC 1,4(4)
469: ADD 1,7,1
470: ST 1,8(6)
471: ST 6,9(6)
472: LDA 6,8(6)
473: LDC 7,359(4) : report FUNCTION-CALL
474: LD 6,1(6)
475: ST 0,8(6)
476: LDA 7,2(7) : jump to next evaluation
477: LDC 0,0(4) : BooleanLiteralNode value; line x
478: ST 0,9(6) : BooleanLiteralNode storage
479: ST 0,10(6)
480: LD 7,0(6) : isCircularPrime FunctionNode line return
481: LD 0,3(6) : identifier load
482: LD 0,4(6) : identifier load
483: LD 0,3(6) : LessThanNode left operand
484: LD 1,4(6) : LessThanNode right operand
485: SUB 2,1,0
486: JLT 2,3(7) : jump to next line x
487: LDC 0,0(4) : LessThanNode evaluates to false
488: ST 0,6(6)
489: LDA 7,2(7) : jump to next evaluation
490: LDC 0,1(4) : line x; LessThanNode evaluates to true
491: ST 0,6(6)
492: LD 0,6(6) : result of an if-statement condition
493: JEQ 0,68(7)
494: LD 0,4(6) : identifier load
495: LD 5,4(6) ; load actual #0
496: ST 5,10(6)
497: LDC 1,4(4)
498: ADD 1,7,1
499: ST 1,7(6)
500: ST 6,8(6)
501: LDA 6,7(6)
502: LDC 7,433(4) : isCircularPrime FUNCTION-CALL
503: LD 6,1(6)
504: ST 0,7(6)
505: LD 0,7(6) : result of an if-statement condition
506: JEQ 0,30(7)
507: LD 0,3(6) : identifier load
508: LD 0,4(6) : identifier load
509: LDC 0,1(4) : NumberLiteralNode constant
510: ST 0,8(6) : NumberLiteralNode storage
511: LD 0,4(6) : ArithmeticOperation left operand
512: LD 1,8(6) : ArithmeticOperation right operand
513: ADD 0,0,1
514: ST 0,9(6)
515: LD 0,5(6) : identifier load
516: LDC 0,1(4) : NumberLiteralNode constant
517: ST 0,10(6) : NumberLiteralNode storage
518: LD 0,5(6) : ArithmeticOperation left operand
519: LD 1,10(6) : ArithmeticOperation right operand
520: ADD 0,0,1
521: ST 0,11(6)
522: LD 5,3(6) ; load actual #0
523: ST 5,15(6)
524: LD 5,9(6) ; load actual #1
525: ST 5,16(6)
526: LD 5,11(6) ; load actual #2
527: ST 5,17(6)
528: LDC 1,4(4)
529: ADD 1,7,1
530: ST 1,12(6)
531: ST 6,13(6)
532: LDA 6,12(6)
533: LDC 7,481(4) : circularPrimesToHelper FUNCTION-CALL
534: LD 6,1(6)
535: ST 0,12(6)
536: LDA 7,23(7) : jump to next evaluation
537: LD 0,3(6) : identifier load; line x
538: LD 0,4(6) : identifier load
539: LDC 0,1(4) : NumberLiteralNode constant
540: ST 0,13(6) : NumberLiteralNode storage
541: LD 0,4(6) : ArithmeticOperation left operand
542: LD 1,13(6) : ArithmeticOperation right operand
543: ADD 0,0,1
544: ST 0,14(6)
545: LD 0,5(6) : identifier load
546: LD 5,3(6) ; load actual #0
547: ST 5,18(6)
548: LD 5,14(6) ; load actual #1
549: ST 5,19(6)
550: LD 5,5(6) ; load actual #2
551: ST 5,20(6)
552: LDC 1,4(4)
553: ADD 1,7,1
554: ST 1,15(6)
555: ST 6,16(6)
556: LDA 6,15(6)
557: LDC 7,481(4) : circularPrimesToHelper FUNCTION-CALL
558: LD 6,1(6)
559: ST 0,15(6)
560: ST 0,16(6)
561: LDA 7,1(7) : jump to next evaluation
562: LD 0,5(6) : identifier load; line x
563: ST 0,17(6)
564: LD 7,0(6) : circularPrimesToHelper FunctionNode line return
565: LD 0,3(6) : identifier load
566: LDC 0,1(4) : NumberLiteralNode constant
567: ST 0,4(6) : NumberLiteralNode storage
568: LD 0,3(6) : ArithmeticOperation left operand
569: LD 1,4(6) : ArithmeticOperation right operand
570: ADD 0,0,1
571: ST 0,5(6)
572: LDC 0,2(4) : NumberLiteralNode constant
573: ST 0,6(6) : NumberLiteralNode storage
574: LDC 0,0(4) : NumberLiteralNode constant
575: ST 0,7(6) : NumberLiteralNode storage
576: LD 5,5(6) ; load actual #0
577: ST 5,11(6)
578: LD 5,6(6) ; load actual #1
579: ST 5,12(6)
580: LD 5,7(6) ; load actual #2
581: ST 5,13(6)
582: LDC 1,4(4)
583: ADD 1,7,1
584: ST 1,8(6)
585: ST 6,9(6)
586: LDA 6,8(6)
587: LDC 7,481(4) : circularPrimesToHelper FUNCTION-CALL
588: LD 6,1(6)
589: ST 0,8(6)
590: LD 7,0(6) : circularPrimesTo FunctionNode line return
591: LD 0,3(6) : identifier load
592: LD 5,3(6) ; load actual #0
593: ST 5,7(6)
594: LDC 1,4(4)
595: ADD 1,7,1
596: ST 1,4(6)
597: ST 6,5(6)
598: LDA 6,4(6)
599: LDC 7,565(4) : circularPrimesTo FUNCTION-CALL
600: LD 6,1(6)
601: ST 0,4(6)
602: LD 7,0(6) : main FunctionNode line return
