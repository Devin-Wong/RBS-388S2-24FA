# 2 Functions


Jin Wang, 

MSIS, Rutgers


---
- [2 Functions](#2-functions)
  - [1. Function structure](#1-function-structure)
    - [1.1 Function](#11-function)
    - [1.2 Arguments (in `print()`)](#12-arguments-in-print)
  - [2.  Comments and Pseudocode](#2--comments-and-pseudocode)
  - [3. Create our own function by `def`](#3-create-our-own-function-by-def)
    - [First function without arguments](#first-function-without-arguments)
    - [Function with Arguments](#function-with-arguments)
    - [Function with default value](#function-with-default-value)
  - [4.  Return values](#4--return-values)
  - [5. Variables and parameters are local](#5-variables-and-parameters-are-local)
  - [6. Stack diagrams and debugging](#6-stack-diagrams-and-debugging)
  - [7. Organizing our code by using `main()`](#7-organizing-our-code-by-using-main)
  - [8. Practice questions](#8-practice-questions)
  - [Summing up](#summing-up)

---

## 1. Function structure

---

**The first function: `print()`**

---

### 1.1 Function

---
### 1.2 Arguments (in `print()`)

**Arguments**

- `print()` arguments: the python documentation at https://docs.python.org/3/library/functions.html#print. 

**Default arguments**

---

## 2.  Comments and Pseudocode

**Comments**

**Pseudocode**

**Multi-line comment**

---

## 3. Create our own function by `def`

---

### First function without arguments

---

### Function with Arguments 

---
### Function with default value

---
## 4.  Return values


---
## 5. Variables and parameters are local

---

## 6. Stack diagrams and debugging
---


**Call a function in another function**

---

**Stack diagram**

![width:100px](funcion_1.png)


---


**Debugging**

---

## 7. Organizing our code by using `main()` 

---
## 8. Practice questions
---

1. Write a program to create a function `show_employee()` using the following conditions.
	- It should accept the employee’s name and salary, and print both.
	- If the salary is missing in the function call, then assign default value 9000 to salary.
	
    Given
	
    ```python
    showEmployee("Ben", 12000)
    showEmployee("Jack")
    ```
    Expected output:

    ```python
    Name: Ben, salary: 12000
    Name: Jack, salary: 9000
    ```
---

2. What is the output of the following program?
	```python
	def outer_fun(a, b): 
		square = a ** 2 
		
		# inner function 
		def addition(a, b): 
			return a + b 
		
		add = addition(a, b) 
		
		return add + 5 

	result = outer_fun(5, 10) 
	print(result)
	```

---
3. Calculate the area of a circle. The mathematical formula is $\pi r^2$, where $r$ denotes the radius, and $\pi$ is the mathematical constant, 3.14.

   1. create a function named `square`, which returns the squared value given a number.

   2. create a function named `area`, which returns the area of a circle given a radius. In this function, you need to call the `square` function defined above.
	
   3. Create a main function to orgnize the program. In the main function, print a sentence like 
      	- "The area of a circle with radius 1 is 3.14." if you put $r=1$, or 
      	- "The area of a circle with radius 2 is 12.56." if you put $r=2$.


---

## Summing up
- `print()` function 
- Arguments in `print()`
- Comments and pseudocode
- Create function using `def`
- Arguments, default value
- Local variables
- `main()` function

---

End
