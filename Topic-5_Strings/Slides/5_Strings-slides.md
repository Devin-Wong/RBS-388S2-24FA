# 5 Strings

Jin Wang, 

MSIS, Rutgers

---


- [5 Strings](#5-strings)
- [1. A string is a sequence](#1-a-string-is-a-sequence)
	- [len function](#len-function)
	- [String slices](#string-slices)
- [2.  Strings are immutable](#2--strings-are-immutable)
	- [3. String methods](#3-string-methods)
	- [.strip()](#strip)
	- [.title()](#title)
	- [.upper()](#upper)
	- [.split()](#split)
- [4. Traversal with a `for` loop](#4-traversal-with-a-for-loop)
- [5. Application 1: Searching](#5-application-1-searching)
- [6. Application 2: Looping and counting](#6-application-2-looping-and-counting)
- [7. Practice questions](#7-practice-questions)



---
# 1. A string is a sequence
---
**String in Topic 1**

- Values in Quotation marks
- Small problem with quotation marks
- String concatenation
- String Repetition

---

**Bracket operator**
```python
>>> s = "Hello"
>>> letter = s[1]
>>> letter
```

Which is the value of `letter`

---

## len function

```python
>>> s = "Hello"
>>> len(s)
5
```

---

## String slices


```python
>>> s = "Hello, Jin!"
>>> s[0:5]
```

---
# 2.  Strings are immutable

---
## 3. String methods
---
## .strip()

- strip all whitespaces on the left and right of a string. 
---

## .title()
- Capitalize the first letter of each word
---
## .upper()

- Capitalize all letters
---
## .split()
- split a string into a list
---

# 4. Traversal with a `for` loop

---
# 5. Application 1: Searching
- find out whether there is a particular character in a string
---

# 6. Application 2: Looping and counting

- count the number of times a letter appears in a string.


---
# 7. Practice questions

---
1. Use two `input` function twice, one for inputing first name and another one for last name.  Use `.strip()` and `.title()` methods to correct user's input. Then print "Last name, First name". For example, input: " jin" as first name, "wang" as last name, the output would be "Wang, Jin".

---
2. Given an address, e.g., "100 Rockafeller Road, Piscataway, NJ 08854". Try to split the string, and get the information, street, city, state, zipcode.

---
3. Create a function, which takes a list of names and print "Hello, " together with each name. For example, taking a list, `['Mark', 'Peter', 'John']` , the function would print
	```python
	Hello, Mark
	Hello, Peter
	Hello, John
	```
--- 
4. Create a function, named `find_repetition`, to find out whether there are repetitive letters in a word. For example, For the word "Rutgers", the function returns `True` since the letter 'r' is repeated. (So it means we need to ignore the cases, 'R' is considered as a repetition of 'r'.) For the word "RBS", the function returns `False`.
