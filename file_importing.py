# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:02:42 2023

@author:vaishnavi
"""
"""already Pizza.py file is created 
we are accessing  method,Fynction
 which is define in  Pizza.py """

import Pizzaa
from pizza import make_pizzaa
import pizzaa as p
from Pizzaa import make_pizzaa as mp




from Pizzaa import info  
info(a='b',c='d')
######## FILE IMPORTING ###########

import Pizzaa  # Now Python should be able to find "Pizzaa.py"


import Pizzaa
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
###############333
import Pizzaa

#importing specific function
from Pizzaa import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#using as to give a function alias
from Pizzaa import make_pizza as mp

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
################
#using as to give a module an Alias
import Pizzaa as p 
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')
#####################3
#importing all functions in a module

from Pizzaa import*
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

##############################################################

########Scope of Variable######
#initialised the variable first 
#and then call it .this is corect way
x=x+1
x=6
print(x)
#this is not correct method to intialized variablr and call them and increment



import Pizzaa
make_pizza()

import Pizzaa as p 
make_pizza(12,'abc')













