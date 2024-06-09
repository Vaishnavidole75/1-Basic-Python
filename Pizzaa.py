# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:45:15 2023


@author:  vaishnavi
"""

def make_pizza(*toppings):
    print("\n making pizzz with folowings topping: ")
    for topping in toppings:  
        print(f"-{topping}")
        
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#

def info(**me):
    print("Here is my info:",me)
info(a='b',c='d')


    