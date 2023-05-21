# 0x00. Python - Hello, World
- This is the first project on Python in my ALX Software engineering journey
- However,task 10 in this project was a technical interview preparation on C programming language
## What to expect from this project
|        Table of contents           | 
| -----------------------------------| 
|   What i learnt in this project    |
|        My header file              |
|   Project tasks(task 0 - task 13)  |


## What i learnt in this project
- In this project i learn about the basics of the python programming language
    - The Zen of python
    - How to use the Python interpreter
    - How to print text and variables using print
    - How to use strings in python
    - indexing and slicing in Python
    - Writing codes using the official python coding style and how to check your code with pycodestyle

## My header file
- All the prototypes of my functions for task 10 were included in my header file "lists.h

## Project tasks
### 0. Run Python file
A Shell script that runs a Python script.

The Python file name is saved in the environment variable $PYFILE
- file: 0-run

### 1. Run inline
A Shell script that runs Python code.

The Python code is saved in the environment variable $PYCODE
- file:1-run_inline

### 2. Hello, print
A Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
- Using the function print
- File: 2-print.py

### 3. Print integer
Python script that print integer stored in the variable number, followed by Battery street, followed by a new line.
- not allowed to cast the variable number into a string
- code must be 3 lines long
- use f-strings 
- file: 3-print_number.py

### 4. Print float
Python script that print float stored in the variable number with a precision of 2 digits
- not allowed to cast number to string
- use f-strings
- File:4-print_float.py

### 5. Print string
Python script that print 3 times a string stored in the variable str,followed by its first 9 characters.
- not allowed to use any loops or conditional statement
- program should be maximum 5 lines long
- File: 5-print_string.py

### 6.Play with strings
Python script that print Welcome to Holberton School!
- not allowed to use any loops or conditional statements.
- have to use the variables str1 and str2 in your new line of code
- program should be exactly 5 lines long
- File:6-concat.py

### 6-concat.py
Python script that slice the word 'Holberton'
- not allowed to use any loops or conditional statements
- program should be exactly 8 lines long
- word_first_3  contain the first 3 letters of the variable word
- word_last_2  contain the last 2 letters of the variable word
- middle_word should the value of the variable word without the first and last letters
- File: 7-edges.py

### 8. Create a new sentence
Python script that print object-oriented programming with Python, followed by a new line.
- not allowed to use any loops or conditional statements
- program should be exactly 5 lines long
- not allowed to create new variables
- not allowed to use string literals
- file: 8-concat_edges.py

### 9. Easter Egg
Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
- Your script should be maximum 98 characters long (check with wc -m 9-easter_egg.py)
- file: 9-easter_egg.py

### 10. Linked list cycle
Technical interview preparation:
A function in C that checks if a singly linked list has a cycle in it
- Prototype: int check_cycle(listint_t *list)
- Return: 0 if there is no cycle, 1 if there is a cycle
- Allowed fuctions
   - write
   - printf
   - putchar
   - puts 
   - malloc 
   - free
- File: 10-check_cycle.c, lists.h

### 11. Hello, write
Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
- Use the function write from the sys module
- not allowed to use print
- script should print to stderr
- script should exit with the status code 1
- File:100-write.py

### 12. Compile
 A script that compiles a Python script file.
- The Python file name is stored in the environment variable $PYFILE
- output filename  $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
- File: 101-compile

### 13. ByteCode -> Python 
Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:


- File: 102-magic_calculation.py


