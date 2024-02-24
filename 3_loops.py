############  24/7/2023  #######################

#      IF-ELSE

#Check even odd
n=int(input("enter no:"))
if n%2==0:
    print("Even no:")
else:
    print("Odd number")
    
#### elif condition

savings=float(input("enter the savings"))
if savings==0:
    print("no savings")
elif savings<500:
    print("well done")
elif savings <1000:
    print("thats a tidy sum")
elif savings <10000:
    print("welcome mam")
else:
    print("enter valid amount")
########################################3
#           while loop

# To print 1 to 10 number  
count=1
while count <=10:
    print(count)
    count+=1
#######  
count=0
print("starting")
while count <=10:
    print(count)
    count+=1
##############################################

##              for loop
#using for loop print the values in given range
print('print out values in a range')
for i in range (2,10):
    print(i)
    print('done')
###### 

n=int(input("Enter the number:"))
for i in range(0,n):
    print(i)
####
   
print('print out values in a range')
for i in range (1,10):
    print(i)
print('done')
#####

p=int(input("enter value"))
for i in range(p):
    print(i)
    

    
################################3
print('only print code if aoo iteration completed')
num= int(input('enter a number to check for:'))
for i in range (0,16):
    if i == num:
        break
    print(i)
print('done')   

##################################

"""#imp for interview"""

######    Anonymous variable
#instead of for i we can use _ it work like i
for _ in range(0,10):
    print(_)
#############
for _ in range(0,10):    
    print('_',end="")
    print()
#######
#imp for interview
for _ in range(0,10):
    print('*',end="")
    print() 
    
''' 
#output:  
    *
    *
    *
    *
    *
    *
    *
    *
    *
    *
'''
##################################
##
#location of print is changed
for i in range(0,6):
    if i == num:
        break
    print(i,'', end='')
    print('done')
 
################################33

"""IMP For Interview"""
#write a program to find odd number in given range 
start ,end=4,19

for num in range(start,end+1):
    #checking condition
    if num%2!=0:
        print(num,end=" ")
        
#### ODD NO
start=0
end=5
for num in range(start,end+1):
    if num%2!=0:
        print(num)
#####################
##python prgram to even no.
start ,end=4,19

for num in range(start,end+1):
    #checking condition
    if num%2==0:
        print(num,end=" ")
##############################

#Using another variable
s=1 
e=20

for i in range(s,e+1):
    if i%2!=0:
        print(i)
     
################################
        
###########

for i in range(0,10):
    if i%2==0:
        print("all Even no:",i)
 
 
#all even no. in range

for even_no in range (4,15,2):
     print(even_no,end=' ')
#all odd no.in range
#here some wrong code odd no not print here 
for odd_no in range (4,15,2):
     print(odd_no,end=' ')
###########################

start=int(input("enter start range"))
end=int(input("enter the end of range"))
#iterting each no in list
for num in range (start,end+1):
    #checking condtion
    if num%2!=0:
        print(num,end=" ")
################################
#even no using start and end
start=int(input("enter start range"))
end=int(input("enter the end of range"))
#iterting each no in list
for num in range (start,end+1):
    #checking condtion
    if num%2==0:
        print(num,end=" ")
        
#############################

####prime number for given range#######
l_val = int(input ("Enter the Lowest Range Value: "))  
u_val = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for no in range (l_val, u_val + 1):  
    if no > 1:  
        for i in range (2, no):  
            if (no % i) == 0:  
                break  
        else:  
            print (no)  
##################################

####check whether year is leap year or not #########

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#pr


######################################

####palidrome or not##########
#
def isPalindrome(s):    
    return s == s[::-1]
s=input('enter string')
palindrome=isPalindrome(s)

if palindrome:
    print('palindrome')
else:
    print('not palindrome')
    
###############################

#Using Another way

s=input("Enter a string")

string_palindrome=s[::-1]
print("check Palindrome string or not :")
if string_palindrome:
    print("palindrome")
else:
    print("not palindrome")                  
 
    
##############################################    

#####prime number
def prime_no(num):
    for i in range(2,num):
        if num%i==0:
            return "the no. is not prime"
            break
    return "the no.is prime"

print(prime_no(2))
        
######################################################

####         Pattern   ###########

#########   Pyramid
rows=int(input('enter the number'))

for i in range(rows):
     for j in range(i+1):
         print('*',end=' ')
     print()
     
     
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

################################

for i in range(4):
      for j in range(4-i):
          print('*',end=' ')
      print()
'''
Output
* * * * 
* * * 
* * 
* 
''' 
    
     
##########box pattern
rows=int(input('enter the number'))

for i in range(rows):
     for j in range(rows):
         print('*',end=' ')
     print() 
     
'''
Output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *     
'''
     
######
for i in range(4):
      for j in range(4):
          print('*',end=' ')
      print()  
      
'''
output:
* * * * 
* * * * 
* * * * 
* * * *'''
     
################
   
##################################################

