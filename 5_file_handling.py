# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:43:26 2023

@author: vaishnavi
"""

################# File handling in python ###############

#Pre-requisites::
    
#The open() function needed
#one argument :the name of the file you want to open

#path=> THERE ARE TWO TYPE OF PATH

#1]absolute path 
''' 
c:/1-python/pi_digits.txt

Back slash(/) is used
#windos=> \ backslash
'''
#2] Realtive path

'''
pi_digits.txt
'''
#for windos=> \ backslash 
#for linux=> /frontslash

########################################################

#1]Realitve path

'''here we created a sample pi_digits.txt file
in C:/1-python folder for file operation(read,write,append)
'''

with open('pi_digits.txt') as file_object:
    contents=file_object.read()
print(contents) 

'''open method open pi-digits file read the content of file
 and print that content in output window'''
 
########

with open('pi_digits.txt') as f:
    c=f.read()
print(c.rstrip())
#rstrip() used - To remove whitespace or used to remove sepcified element from contents

########33

with open('pi_digits.txt') as file_object:
    contents=file_object.read()
print(contents.rstrip())

################################3

#######     Absolute path  #########

#need c:/1-python/file_name
# need to select working directory in absolute  path

with open('c:/1-python/pi_digits.txt') as file_object:
    contents=file_object.read()
print(contents.rstrip())
#####################################

#reading line by line
#blank line space is appear due to new line 
filename='c:/1-python/pi_digits.txt'
with open (filename) as file_object:
    
    #we again use this syntax to let python open &closethe file porperly
    for line in file_object:
        print(line)
        print(line.rstrip())


######################################
#working the file contents  after the read file 
#we get the addtion of contents
filename='c:/1-python/pi_digits.txt'
with open (filename) as file_object:
    lines=file_object.readlines()
    pi_string= ''
    
    for line in lines:
        pi_string +=line.rstrip()
        print(pi_string)
        print(len(pi_string))

file='c:/1-python/pi_digits.txt'
with open('c:/1-python/pi_digits.txt') as f:
    for line in f:
        print(line)
##########################################
file="c:/1-python/programming.txt"

with open (file, 'w') as file_object:
    file_object.write("i love programming")
#  

###
#write()-is used to write data to a file


file="c:/1-python/programming.txt"

with open (file, 'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love to learn it.\n")
   
####################
#program in append mode    
# append() method is used to add elements  
file="c:/1-python/programming.txt"

with open (file, 'a') as file_object:
    file_object.write("i also love finding meaning in large database. \n")
    file_object.write("i love to creating apps..\n")
    