
# 4 Loop

Jin Wang, 

MSIS, Rutgers


---

Table of Contents

[1. Updating variables.](#1.%20Updating%20variables.)
[2. Repetitions and Loops](#2.%20Repetitions%20and%20Loops)
[3. `while` loops](#3.%20%60while%60%20loops)
[4. List basics](#4.%20List%20basics)
[5. `for` loops](#5.%20%60for%60%20loops)
[6. `continue`, `break`](#6.%20%60continue%60,%20%60break%60)
[7. Practice Questions](#7.%20Practice%20Questions)



---
## 1. Updating variables.

---

**Reassignment**
```python
x = 1
x = 2
print(x)
```

---

**Updating variables**

```python
x = 1
y = x
x = 2
print(y)
```

---
**increment**

```python
i+=1
```

**decrement**
```python
i-=1
```
---
## 2. Repetitions and Loops

```python
print("Hello")
print("Hello")
print("Hello")
```

---

## 3. `while` loops


```python
while <condition>:
	<block>
```


---

## 4. List basics

---
**List**

```python
names = ["Jin", "Mark", "Neil"]
numbers = [3, 8, 8]

print(names)
print(numbers)
```

---
**Getting access to the elements**
```python
names = ["Jin", "Mark", "Neil"]
numbers = [3, 8, 8]

print(names[0])
print(names[1])
print(names[2])

print(numbers[0])
print(numbers[1])
print(numbers[2])
```

---
**Updating the elements**
```python
numbers = [3, 8, 8]
numbers[2] = 5

print(numbers)
```

---
**`range()` function**

```python
numbers_range = range(3)
numbers_list = list(numbers_range)

print(numbers_list)
```
---
**len() function to obtain length**

```python
numbers = [3, 8, 8]
l = len(numbers)
print(l)
```

---
## 5. `for` loops



```python
for i in range(3):
	print("Hello")
```


---


## 6. `continue`, `break`


---

## 7. Practice Questions


1. Create a function named `get_maximum` taking a list of numbers, which can return the maximum number in the list.

---
2. Calculate the sum of  1 to $n$.
	1. Create a function named `get_number` which returns a positive number. In the function you use `input` function to let user input a positive integer. If user inputs a negative number, reprompt the user with "Please input a positive number: " .
	2. Create a function named `get_sum` taking a number $n$ and returning the sum of 1 to  $n$.
	3. Create a `main` function which calls the two functions above to calculate the sum of 1 to $n$.
---
1. Create a function taking a list, which can print out the 2nd value, 4th value, 6th value, ... . For example, given a list `x = ['a', 'b', 'c', 'd']`, the output should print 'b' and 'd'. (try to use `continue` in the loop)
---
1. Given a list of numbers, try to print the numbers starting with the first one and stop when the sum of the numbers collected is larger than 100.