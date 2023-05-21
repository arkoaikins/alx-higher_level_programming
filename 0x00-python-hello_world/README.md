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
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/016114f6-d68f-4fb1-a597-a4de409333d6)
- file: 0-run

### 1. Run inline
A Shell script that runs Python code.

The Python code is saved in the environment variable $PYCODE
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/5fe8245d-ec3b-4817-aae3-c62ab6ad0add) 
- file:1-run_inline

### 2. Hello, print
A Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
- Using the function print
#### Tested code with

- File: 2-print.py

### 3. Print integer
Python script that print integer stored in the variable number, followed by Battery street, followed by a new line.
- not allowed to cast the variable number into a string
- code must be 3 lines long
- use f-strings 
#### Tested code with

- file: 3-print_number.py

### 4. Print float
Python script that print float stored in the variable number with a precision of 2 digits
- not allowed to cast number to string
- use f-strings
#### Tested code with

- File:4-print_float.py

### 5. Print string
Python script that print 3 times a string stored in the variable str,followed by its first 9 characters.
- not allowed to use any loops or conditional statement
- program should be maximum 5 lines long
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/494770a6-20a5-4643-aea9-dd492543b1df)
- File: 5-print_string.py

### 6.Play with strings
Python script that print Welcome to Holberton School!
- not allowed to use any loops or conditional statements.
- have to use the variables str1 and str2 in your new line of code
- program should be exactly 5 lines long
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/f1b6bfdb-b361-44b2-bb3a-45aff705de36)
- File:6-concat.py

### 7. Copy - Cut - Paste
Python script that slice the word 'Holberton'
- not allowed to use any loops or conditional statements
- program should be exactly 8 lines long
- word_first_3  contain the first 3 letters of the variable word
- word_last_2  contain the last 2 letters of the variable word
- middle_word should the value of the variable word without the first and last letters
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/33cb5525-f8a9-4853-95be-0028a1ad3f63)
- File: 7-edges.py

### 8. Create a new sentence
Python script that print object-oriented programming with Python, followed by a new line.
- not allowed to use any loops or conditional statements
- program should be exactly 5 lines long
- not allowed to create new variables
- not allowed to use string literals
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/ae3c8838-363d-4b00-8b9b-0f9700cc3944)
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
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/401b8f7f-cff7-430c-a516-c68d421d43f5)
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/59a018b5-fa8e-4359-bf06-1d9674fffb4a)
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/9b3c34cd-fa3f-4198-97b2-78e0cd6c21f7)i
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/4b5efacc-22de-4846-9897-1e47e12463fd)
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/3f582a1c-cba8-42d7-a85b-e34b8ff838e6)
- File: 10-check_cycle.c, lists.h

### 11. Hello, write
Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
- Use the function write from the sys module
- not allowed to use print
- script should print to stderr
- script should exit with the status code 1
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/ba7a858a-1b93-4a3a-aef7-00ea035feeac)
- File:100-write.py

### 12. Compile
 A script that compiles a Python script file.
- The Python file name is stored in the environment variable $PYFILE
- output filename  $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/27f1127e-8ffa-4b3f-82e5-c9b48c58bf44)
- File: 101-compile

### 13. ByteCode -> Python 
Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

#### Tested code with
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/498a87e1-5c44-42cb-bec1-29abc2cb4690)
- File: 102-magic_calculation.py
