# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:37:51 2023

@author: Vaishnavi
"""
###################### SET ##################

#dont allow duplicate element
#set define in {} 


#creating set
basket={'apple','orange','pear','apple'}
basket
#it will show only one time apple
#############################################
#Acessing element  in a set
basket={'apple','orange','pear','apple'}
basket
for item in basket:
    print(item)
###

    
##############3
#Adding item in set
basket={'apple','orange','pear','apple'}
basket.add('appricot')   
basket
#Updating 
basket={'apple','orange','pear','apple'}
basket.update(['apricot','mango']) 
basket


###########33
#obtaining the lengh set
basket={'apple','orange','pear','apple'}
print(len(basket))
###obtaining max and min

b={1,23,3,4,4,67,8}
print(max(b))
min(b)

######Removing the item . remove() method
basket={'apple','orange','pear','apple'}
basket
basket.remove('apple')
basket.discard('pear')
basket


###############'##############################3
###########  set opertion #########
#Union opertion
s1={'a','b','c','v'}
s2={'p','v','w'}
s1|s2
#intersection
s1&s2
#Diffwerence
s1-s2
####################################



    
