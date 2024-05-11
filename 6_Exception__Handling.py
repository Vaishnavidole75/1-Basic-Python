# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:22 2023

@author: vaishnavi
"""

################## Exception Handling

#the error signifies a situation that mostly
#happens due to to absense of system resources
#the exception are the issues that can appear at runtime and compile time
print(5/0)

a=5
b=0
c=a/b

try:
    print(5/0)
except ZeroDivisionError:
    print("you cant divide by zero ")
print(c)

#handling the FileNotFoundError exception
file='alice.txt'

try:
    with open (file) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry ,file {file} does not exist")
#
file='alice.txt'
try:
    with open(file) as f:
        contents=f.read()
except FileNotFoundError:
    print("file not found")
#
try:
    print(5/0)
except ZeroDivisionError:
    print("not possible")
#################################3
file='username.csv'
with open(file) as f:
    contents=f.read()
    print(contents)
