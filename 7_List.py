# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:07:03 2023

@author: Vaishnavi
"""

#############  LIST #############
#use square brackets []
#creating list
#list allows duplicate value
#List is mutable and index order 

########

#linkdin question
lst=[1,2,3]
a=sum(lst)
print("Total sum is:",a)
total_avg=a/len(lst)
print("Total average:",total_avg)
##################
lst1=['john','paul','gergo','ringo']
lst1
################
#### Nested list

lst1=[1,43.5,True]
lst2=['apple','orange',31]
root_lst=['john',lst1,lst2,'Denise']
root_lst
#my try
l1=[1,2,3]
l2=[3,4,5]
l3=['ok',l1,l2]
l3
###########
l1=[1,2,3]
l2=[4,5,6]
l3=[0,l1,l2]
l3
##################

#Accessing element in list

#delete element using pop method
lst1=['john','paul','gergo','ringo']
l=lst1.pop()
lst1


print(lst1[-1])
lst1[0]
lst1[-2]
lst1[-4:-3]

###################################
##Acessing the element through indexing 0 1 2 

lst1=['john','paul','gergo','ringo']
lst=lst1.append('a')
lst=lst1.insert(2,['b','c','d'])
lst=lst1.extend(['x','y','z'])
lst1[-1]
lst1
lst1[2]
lst1
lst
lst1


print('lst[1]:',lst1[0])
print('lst[-1]:',lst1[-1])
print('lst[1:3]:',lst1[1:3])
print('lst[:3]:',lst1[:3])
print('lst[1:]:',lst1[1:])
#######################
#Adding to a list
#append() method have only one argument .we can add only one element in list by single append() method
#append()  method . it will add element in the end
lst1=['john','paul','gergo','ringo']
lst1.append('Pete')
lst1

#######
##### extend() method
#use to extend the 
#by ths method we can add multiple number ,we want
lst1=['john','paul','gergo','ringo']
lst1
lst1.extend(['albert','Bob','p','u'])
lst1

###########
#   insert() method
#insert method have only 2 arugrment &we can add only 2 argument at a time by single insert9() method
#inserting into a list
a_list=['apple','madonna','cher']
a_list
a_list.insert(1,'paloma')
a_list
#my try
lst=['a','b','c']
lst
lst.append('d')
lst
lst.extend(['1','g','h','j'])
lst
lst.insert(1, 'v')
lst
############
#list concatenation

l1=[1,2,3]
l2=[4,2,6]
l3=l1+l2
l3
#for tuple concat 
t=(1,2)
t1=(3,4)
t2=t+t1
t2
####################  assignment #############

##Question 1=> Find min and max in list
lst1=[1,2,3,4,5]
lst=min(lst1)
lst
lst2=[8,34,6,7]
lst3=max(lst2)
lst3

#Question 2=> Take 5 string in list & make it reverse
l=['a','b','c','d','e']
l1=l[::-1]
l1

#Question 3 => Take 10 no in list &write program to search for value
lst=[1,2,3,4,5,6]
i=9

if i in lst:
    print("number exists")
else:
    print("not exists")
    
#this way like accessing element through indexing
lst=[9,8,7,6,5,4,3,2,1,22]
l1=lst[0]
l1
l2=lst[1]
l2
l3=lst[2]
l3
l4=lst[3]
l4
l5=lst[4]
l5
l6=lst[5]
l6
l7=lst[6]
l7
l8=lst[7]
l8
l9=lst[8]
l9
ll2=lst[9]
ll2
###another way
lst=[9,8,7,6,5,4,3,2,1,22]
i=2 
if i in lst:
    print('No. is present')
else:
    print('NO is not present')

#Question 4 => Take 10 no. in list ,add some duplicate value in the list
#and write a program to find that duplicate value


lst=[1,8,7,6,7,4,3,2,1,2]
lst1=set(lst)
lst1
lst.append(8)
lst.append(7)
lst.insert(5,4)
lst
lst.insert(1,2)
lst
# find duplicate value 
print('dpilicate of 8:',lst.count(8))
lst.count(1)
lst.count(2)
lst.count(7)
#another way by online
my_list = [1, 2, 3, 4, 2, 5, 2]

# Convert the list to a set to remove duplicates
unique_elements = set(my_list)
unique_elements
# Check if the length of the set is different from the original list
if len(unique_elements) < len(my_list):
    print("Duplicate values exist in the list.")
else:
    print("No duplicate values found.")


#Question 5 => create list which contain vowels and non-vowels find out the
#total vowels are present

######
l=['h','i','a','e','i','o','u']
vowels=len([l for l in l if l.lower() in 'aeiou'])
print('Total no of vowels are :',vowels)
######
l1=['h','e','l','l','o']
vowels=len([l for l in l1 if l.lower() in 'aeiou'])
vowels
#######
l1=['H','E','L','L','O']
vowels=len([l for l in l1 if l.upper() in 'AEIOU'])
vowels
#another way
l=['h','i','a','e','i','o','u']
vowels=len([l for l1 in l if l1.lower() in 'aeiou'])
print('Total no of vowels are :',vowels)

#################################################

#Removing list
#This method is used in web scrapping
another_lst=['Gary','Mark','Robbie','Jason']
another_lst
another_lst.remove('Mark')
another_lst

#Remove() method and pop() method is same but only
#we have to pass entity values in remove method 
#and in pop method we have to pass the index of values

#Pop method 
another_lst=['Gary','Mark','Robbie','Jason']
another_lst
another_lst.pop(2)
another_lst

#####
lst6=['once ','a', 'upon','time']
lst6
lst6.pop(2)
lst6

######
#inserting in list
a_list=['a','b','c']
a_list
a_list.insert(2,'p')
a_list

###############   Assignment
#write python program to add all item  in the list    

#Arithmetic opertion
def sum_lst(sum_lst):
    sum=0
    for x in sum_lst:
        sum=sum+x  
    return sum

print(sum_lst([5,6,-8]))

#create a python program to multiply all the item in the list
def mul_lst(mul_lst):
    total=1
    for x in mul_lst:
        total*=x
    return total

print(mul_lst([1,2,-8]))
###
#python program to get largest number from a list

lst=[12,34,56,6,7,8]
print(max(lst))
print(min(lst))        
####

#######################################3
#python program  to count a number of string which satisfies
#the condition that string length is 2 or more and first and last character are the same
#from a given of strings,
#given list is ['abc','xyz','aba','1221']

#my try not matched XXX
def count_no(string):
    for i in string:
        if len(i)>2 and i[0] ==i[1]:
            print()
    print(i)
count_no((['aba','xyz','aba']))
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  
def match_words(words):
    ctr=0
    for word in words:
        if len(word)>2  and word[0] ==word[-1]:
            ctr +=1
    return word
print(match_words(['abc','xyz','aba','1221']))
#op= is 2

#######################
"""write a python program to get a list,sorted in incerasing
order by the last element in each tuple from given list
of non-empty tuples
sample list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
Expected result=[(2,1),(1,2),(2,3),(4,4),(2,5)]"""
########my try but not incerasing order
sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sorted(sample_list))
###
lst=[4,3,2,1]
sorted(lst)

####### sir logic with proper code

def last(n):
    return n[-1]

def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

######################################
###write a python program to remove duplicate value
lst1=[10,20,30,40,10,50,60,70,80]
st1=set(lst1)
#since set remove duplicate item ,hence list is converted to set
print(st1)
lst2=list(st1)
print(lst2)
#####################3
######
#python program to clone or copy a list
original_lst=[10,22,44,32,4]
new_list=list(original_lst)
original_lst
new_list

###########
#python  program to find the list of words that are larger than
# from a given list of words

def long_word(n,str):
    word_len=[]
    txt=str.spilt(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_word(3, "the quick brown fox jumps over the lazy dog"))
#write python function that makes two list and returns
#true if they have at least  one common number
def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
        
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
###########################################

#write a program to calculate the difference between two ists

list1=[1,2,3,4,5]
list2=[1,6,7,8,9]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
total_diff=diff1+diff2
total_diff
################### imp=> RR
#write a python program to convert a list of characters into a string
s=["a","b","c","d"]
str1=''.join(s)
str1="".join(s)
print(str1)
######## imp => RR
#write python program to find index of an item in  a specified list
num=[10,20,30,40]
print(num.index(30))

#write python program to append a list to the second list

lst1=[1,2,3,0]
lst2=['Red','Green','Black']
final_lst=lst1+lst2
final_lst
