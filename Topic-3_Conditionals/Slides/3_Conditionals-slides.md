# 3 Conditionals


Jin Wang, MSIS, Rutgers


---
- [3 Conditionals](#3-conditionals)
	- [1. Boolean expressions](#1-boolean-expressions)
	- [2. Logical operators](#2-logical-operators)
	- [3. Conditional statement: `if` statement](#3-conditional-statement-if-statement)
	- [4. Alternative execution: Control Flow, `else`, and `elif`](#4-alternative-execution-control-flow-else-and-elif)
	- [5. `and`， `or` in `if` statement](#5-and-or-in-if-statement)
	- [6.  Pythonic `if`](#6--pythonic-if)
	- [7. Application: recursion](#7-application-recursion)
	- [Practice questions](#practice-questions)
	- [Summing up](#summing-up)



---
## 1. Boolean expressions

---

**Boolean expressions**
```python
>>> 5 == 5
True
>>> 5 ==6
False
```


---
**Relational operators**
- Python has a set of "**Operators**" that can be used to ask mathematical questions.

| Symbol  | meaning                  |
| ------- | ------------------------ |
| > and < | larger and smaller       |
| >=      | greater than or equal to |
| <=      | less than or equal to    |
| ==      | equals                   |
| !=      | not equal to             |


---
## 2. Logical operators

---

**`and` operator**
- Format \<boolean expression A\> and \<boolean expression B\> 
-  It is `True` if *both* boolean expressions are `True`.

---

**`or` operator**
- Format: `<boolean expression A> or <boolean expression B>`. 
- It is `True`  if *either or both* of the boolean expressions is `True`. 

---
**`not` operator**
- `not` operator negates a boolean expression. `not <boolean expression>` is `True` only is the boolean expression is `False`. 

---

**number as boolean value**
- Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict.
- Any nonzero number is interpreted as `True`
```python
>>> 2 and True
True

>>> 0 and True
False
```

---

## 3. Conditional statement: `if` statement

- `if` statements have the same structure as function definitions: a header followed by an *indented body*.
- **Number of statements in the indented bodies**

---

## 4. Alternative execution: Control Flow, `else`, and `elif`

---
From `if`s to `if-else` 

---
From `if`s to `if-elif` and `if-elif-else` 


---

## 5. `and`， `or` in `if` statement

---
## 6.  Pythonic `if`


---
## 7. Application: recursion


---
## Practice questions

---

1.  Create a function named `is_even`, which returns `True` if inputting a even number; return `False`.

---
2. In a right triangle, the lengths of the sides are $a$, $b$ and the hypotenuse is $c$. Pythagoras theorem says that $a^2 + b^2 = c^2$. Write a function named _check_pythagoras_ that takes parameters, $a$, $b$ and $c$, and checks to see if Pythagoras theorem holds. If it holds, the program should print "Pythagoras theorem is satisfied.". Otherwise, the program print, "No, Pythagoras theorem isn't satisfied."

---
3. Use `if-elif-else` statements to finish this question. Professors give letter grade based on the score a student gets in an exam. Write `Python` code which can print a letter grade given a score value.
	
	| Score  | Letter grade |
	| ------ | ------------ |
	| 90-100 | A            |
	| 80-89  | B            |
	| 70-79  | C            |
	| 60-69  | D            |
	| <60    | F            |

---
## Summing up
- Conditionals
- Logical operators: `or`, `and`, `not`
- `if` statements
- Control flow, `elif`, `else`
- Pythonic coding

---

End
