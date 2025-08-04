// *************** Operator Precedence and Associativity in javascript ***************

// *********** a is a operand, b is an operand *************
// *******************   + - * / 

// JavaScript Operator Precedence List (High → Low)
// Precedence	Operator(s)	Type	Associativity
// 21	()	Grouping	N/A
// 20	. [] () ?.	Member / Call	Left to Right
// 19	new (without arguments)	Object Creation	Right to Left
// 18	++ -- (Postfix)	Postfix Increment/Decrement	Left to Right
// 17	++ -- + - ~ ! typeof void delete	Unary	Right to Left
// 16	**	Exponentiation	Right to Left
// 15	* / %	Multiplication / Division / Modulus	Left to Right
// 14	+ -	Addition / Subtraction	Left to Right
// 13	<< >> >>>	Bitwise Shift	Left to Right
// 12	< <= > >= in instanceof	Relational	Left to Right
// 11	== != === !==	Equality	Left to Right
// 10	&	Bitwise AND	Left to Right
// 9	^	Bitwise XOR	Left to Right
// 8	`	`	Bitwise OR
// 7	&&	Logical AND	Left to Right
// 6	`		`
// 5	??	Nullish Coalescing	Left to Right
// 4	?:	Conditional (Ternary)	Right to Left
// 3	= += -= *= /= etc.	Assignment	Right to Left
// 2	yield yield*	Yield	Right to Left
// 1	,	Comma	Left to Right
// use Precedence part (Common):
// Operator	Meaning	Precedence	Associativity
// *, /, %	Multiplication / Division / Modulus	15	Left to Right
// +, -	Addition / Subtraction	14	Left to Right
// ==, !=, ===, !==	Equality	11	Left to Right
// &&	Logical AND	7	Left to Right
// `		`	Logical OR
// ?:	Ternary	4	Right to Left
// = += etc	Assignment	3	Right to Left