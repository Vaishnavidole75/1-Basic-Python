# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:59:35 2023

@author: Vaishnavi
"""

################  DICTIONARY  ############
#it is 
#it dont allow duplicate 
#dictinary cant have two items with the same key
#mutable & indexed 
#it have key and values that is unordered
#we can access the values in tuple and list as keys values

#creating dictionary
capitals={'Maharashtra':'Mumbai',
          'up':'lakhnow',
          'karnataka':'Banglore'}
capitals

#Accessing items via keys

print('capitals[Maharashtra]:',capitals['Maharashtra'])


#Adding a new entry
capitals['west bengol']='kolkatta'
capitals

#changing a keys values

capitals['up']='gandinagar'
capitals
###############
capitals['mp']='gajyabaad'
capitals
######
capitals.pop('mp')
capitals
#Removing an entry
capitals.pop('up')
capitals

#del method
del capitals['up']
capitals

#########################################
capitals={'Maharashtra':'Mumbai',
          'up':'lakhnow',
          'karnataka':'Banglore'}
capitals

##accessing only keys in given dict
for states in capitals:
    print(states, end=" ,")
#we get only keys in this dict


#accessing the values and keys
##### IMP
for states in capitals:
    print(states, end=" ,")
    print(capitals[states])
#here we access keys and values
##########################################33

print(capitals.values())
capitals.keys()
capitals.items()

##############
#checking key membership

print('karnataka' in capitals)
print('bihar' not in capitals)

###########
#obtaining the length of dict
print(len(capitals))    

########################
#Dictinary can have values in tuple
seasons={'summer':('feb','mar','apr','may'),
        'Rainy':('june','july','augest','sep'),
        'winnter':('oct','nov','december','jan')
        }
print(seasons['Rainy'])
print(seasons['Rainy'][0])

#####################################

############### Dictinary method  #########3
#get() method
print(capitals.get('up'))

#dictinary cant have two items with the same key

dict2={'brand':"Maruti",
       'model':"breeza",
       "year":2019,
       'year':2023
       }
dict2
#################
## loop through a dictionary it will shows only keys
 
for x in dict2:
    print(x)
##################################
############  Assignment 

#write apython program to add a key into dictionary
#sample Dictionary ={0:10,1:20}
#expected dict={0:10,1:20,2;30}

d={0:10,1:20}
d
d.update({2:30})
d
##########
#another way for above code
d={0:10,1:20}
d
d[2]=30
d
##############
"""write python program to concatenate the following dictionary
to create new one 
Sample Dictionary:
dict1={1:10,2:30}
dict2={3:30,4:40}
dict3={5:50,6:60}

expected result
"""
dict1={1:10,2:30}
dict2={3:30,4:40}
dict3={5:50,6:60}
dic4={}
for d in (dict1,dict2,dict3):
    dic4.update(d)
print(dic4)
###
##########3
#write python program to script to check whether given key is already is exist or not
d={1: 10, 2: 30, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("key is  prsent in dictionary")
    else:
        print("key is not  prsent in dictionary")
is_key_present(5)
is_key_present(9)
#################################
#write a python program to iterate over dictionaries using for loop 
d={'x':10,'y':20,'z':30}
for dict_key ,dict_value in d.items():
    print(dict_key,':',dict_value)
#######################################
