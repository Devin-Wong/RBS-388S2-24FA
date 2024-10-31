# 7 Set and Tuple

Jin Wang, 

MSIS, Rutgers

---

[1. Sets](#1.%20Sets)
[2. Set Methods and Operations](#2.%20Set%20Methods%20and%20Operations)
[3. Modifying a Set](#3.%20Modifying%20a%20Set)
[4. Tuple](#4.%20Tuple)
[5. Tuple assignment](#5.%20Tuple%20assignment)
[6. Variable-length argument tuples](#6.%20Variable-length%20argument%20tuples)
[7. Lists and tuples](#7.%20Lists%20and%20tuples)
[8. Practice questions](#8.%20Practice%20questions)


---
## 1. Sets
---
### Defining sets

Sets are another collection/container, like lists, which contain multiple values. 
- The **key differences** are
	- **Sets don't hold order**
	- **Sets don't allow duplicate elements**

---
**Set size**
- List lists, `len()` returns set size.

---
**`in` Operation**

---

### List and set

- Set and list are interchangeable. 
---

## 2. Set Methods and Operations

---

### `add()` method


### `union()` method and `|` operator


### `intersetion()` method and `&` operator


### `difference()` method and `-` operator

---
## 3. Modifying a Set

**`remove()` method**
**`discard()` method**


---

## 4. Tuple
---

### Defining tuples

```python
>>> t = 'a', 'b', 'c', 'd'
>>> t
('a', 'b', 'c', 'd')
```


---
### Slice operator
The slice operator selects a range of elements.
```python
>>> t = ('a', 'b', 'c', 'd')
>>> t[0]
'a'
>>> t[1:3]
('b', 'c')
```

---
### Tuples are immutable
- Tuples are immutable, and you cannot modify the elements.
```python
>>> t = ('a', 'b', 'c', 'd')
>>> t[0] = 'A'
TypeError: 'tuple' object does not support item assignment
```

---
## 5. Tuple assignment

---
## 6. Variable-length argument tuples


---
## 7. Lists and tuples

### `zip()` function

### `enumerate()` function

---
## 8. Practice questions

---
1. We've provided you with a list of lottery players, and also with 4 random lottery numbers. The random lottery numbers are generated like this:
```python
import random
lottery_numbers = set(random.sample(list(range(22)), 4))
```
And the list of players we've given you are:
```python
players = [
("Rolf", {1, 3, 5, 7, 11, 20}),
("Charlie", {2, 7, 9, 5, 12, 15}),
("Anna", {7, 8, 1, 3, 13, 16}),
("Jen", {4, 7, 3, 5, 12, 21})
]
```

Try to find out the number of winnings for each person. For example, if the lottery number is  `6, 8, 9, 13, 16, 19`, you need to print:

```python
Rolf won 0.
Charlie won 1.
Anna has won 3.
Jen has won 0.
```
---

2. Try to create a function, which can take variable-length arguments and return the square root of the arguments.
---
3. Summary data. Create a function, named `summarize_data`, which takes a list of numbers and returns a tuple containing the minimum, mean, and the maximum values. For example, given `[1, 2, 5]`, it would return `1, 2.6666, 5`
	- You may use some built-in functions, like `sum`, `min`, and `max` .
---

4. **(Optional)** Letter frequency. Create a function, named `letter_frequency`, which takes a string and prints the letters in the string (case-insensitive, or just use upper case) and corresponding frequency. For example, 
	- Given 'Rutgers, RBS', the function would print `[('G', 1), ('U', 1), ('B', 1), ('T', 1), ('R', 3), (',', 1), ('E', 1), ('S', 2)]`

---
 **End**
 