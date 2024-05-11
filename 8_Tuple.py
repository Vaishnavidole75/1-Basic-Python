# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:34:26 2023

@author: lk
"""

###############TUPLE############
#accesss in ()
#it is collection of object
#it is immutable type
#Tuple allow dulicate value

#creating tuple
tup1=(1,3,5,7)
tup1[0]
#Accessing elements in tuple
print(f'tup1[0]:\t{tup1[0]}')
print(tup1[0])
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])

#Tubles can hold different types
tup2=(1,'john',True,-23.45)
print(tup2)
#iterating over tuples
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x)
#####################################################    
###########Tuple related functions##################
#len()
len(tup3)
####################
tup4=('apple','orange','plum','apple')
#Tuple allow dulicate value
tup4.count('apple')
###############
print(tup4.index('apple'))
print(tup4.index('plum'))
#######
#checking if element is exists
if 'orange' in tup3:
    print('orange is in tuple')
###############################################
#############Nested Tuples#############33
#in one tuple mulitple tuple
#Nesting of tuple
tuple1=(1,3,5,7)
tuple2=('john','Denise','phone','Adan')
tuple3=(42,tuple1,tuple2,5.5) 
print(tuple3)  

#
t=(1,2,3)
t1=(4,5,6)
t3=(0,t,t1)
t3

    
