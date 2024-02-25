#             24/7/2023 
#
##############################

#Data type of given variable
x={'name':'name','age':45}
print(type(x))
     
####

x=range(6)
print(type(x))
   
   
str1="hello"
str2=2
str3=str1+str2    
str3     
#throw error
###############3
x='this is python'
print(x)

#string slicing
print(x[2:8])
#slice from start
print(x[:3])
#slice from end
print(x[2:])     
#negative indexing
print(x[-5:-2])
print(x[-11:-7])
#make string in uppercase
print(x.upper())
print(x.lower())
#check whether string is upper or not
print(x.isupper())
#check whether string is lower or not 
print(x.islower())
#to remove white space
print(x.strip())
 ###replacing the string  
#replace method()
#it take replcae(old,new)   odd means=>old string replcaed by new  i.e. new string
    
x = "hello world"
x = x.replace("hello world", "hi")
print(x)
x='hhh'
print(x.replace("hhh","ggg")) 
x
##use of split which replace white space
x="hello world" 
print(x.split(","))
x      
## remove white space with space
x="hello world" 
print(x.split(" "))      
        
#reverse string
x="hello world"
string=x[::-1]
#here :: is start & end ,-1
print(string) 

x="hello world"
string=x[::-2]
print(string) 

######use of find() method in program it will find the specified value
x="this is a python and it is very powerful"
print(x.find("and"))       
###
#to add whitespace
x="hello"
y="world"
print(x+y)
print(x+" "+y)  

##### f operator
x=21
y="my name is vaishnavi"
print(x+y)
#it will show error
#to remove this error we are writting 
print(f" my name is vaishnavi and my age is {x}") 

#Display int with string 
quantity=3 
item_no=64
price=67
print(f"i want {quantity} piceces and item number is {item_no},its price{price}")
#accessing the values through empty {}      
my_order="i want {} piceces and item number is {},its price{}"  
print(my_order.format(quantity,item_no,price))      
#another way by there index no        
my_order="i want {0} piceces and item number is {1},its price{2}"  
print(my_order.format(quantity,item_no,price))  
############################
###escape opertor
#the escape charachter is allow you to use double quotes
text="this is fun fair and  its has got big \"round rigo\""
print(text)  

#################################################
#python operator
###operator preciding

#rule for mathematical opertion
#PEMDAS
#p=paranthesis
#E=Expontentional
#M=Multiply
#D=Division
#A=Addtion
#S=Subtraction

##################################
#linkdin Question

s=input("Enter a string")

string_palindrome=s[::-1]
print("check Palindrome string or not :")
if string_palindrome:
    print("palindrome")
else:
    print("not palindrome")                  

############

a="aaaa"
b="bbbb"
c=a+b
c
print(a+" "+b)
#

