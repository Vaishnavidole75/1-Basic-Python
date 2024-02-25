
#########   25/7/2023   ############

############ Variable ################
 
 #Type Of variable
 #1]Local  (Accessible by only inside he function)
 #2]Global (Accessible by outside the function)

###################################

#local vriable
x='awesome'
def my_function():
    x='easy'
    print("python is "+x)
my_function()
 
#global varivable
x='awesome'
def my_function():
    print("python is "+x)
my_function()



############# FUNCTIONS ############

'''#Type Of Argument'''

#Default Argument
#Arbitary Argument
#KEYWORD ARGUMENT


#function with argument
def prime_no(num):
    for i in range(2,num):
        if (num%i==0):
            return "This number is not prime no."
            break
    return "This is prime no"
print(prime_no(7))

###############################
#function without argument
def greet_user():
    print("Heyyyyyy Hello")
greet_user()
#################################
#passing a simple information
def greet_user(username):
    print(f"hello,{username}!")
greet_user("Vaishnavi")
#practice
def greet_user(username):
    print(f"Here is user:{username}")
greet_user('vd')
####################################
#argument and paramenter
#postional argument
def describe_pet(animal_type,pet_name):
    print(f"\nI Have a{animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('Dog','Sunny')

#####################

#Default argument
#assign the value directly to parameter
#this is used in stack overflow
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI Have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='Sunny')
#############
#Positional
def s_info(F,L):
   print(f'my name is {F} {L} ')
s_info('vaishnavi','Dole')  
##########
#now,Default

def s_info(F,L="Dole"):
   print(f'my name is {F} {L} ')
s_info('vaishnavi') 

#########  
##Signature of Function
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI Have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet("sunny")
##############################################

#######################ASSIGNMENT##################
#Task-1
#Question=> create a program using math package and 
#F string and tell us how many days ,weeks 
#and months.we will leave until 80 years

import math
age=int(input("Enter your age"))
lifespan=80-age
print("Remaining age is:",lifespan)
days=lifespan*365
weeks=lifespan*52
months=lifespan*12

print(f"Here your remains days: {days}\nYour remains Weeks: {weeks} \nYour remains months are:{months}")
#####################################

##########*
######## Another way

print("What is your todays age")
years_today=input("years:")  
months_today=input("months:") 
days_today=input("days:")

total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total ags today in days {total_days_today}")
print("Lets assume you expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"your remaining life in days {remaining_days_to_live}")
###################
###Task-2
#Question=>create a program for roller coster if your height is greater than or equal to 120cm
#then display you are eligible to play roller coster

height=int(input("Enter your height:"))

if height>=120:
    print("Your Eligible to play roller coster ")
else:
    print("Your not Eligible tp play roller coster ")
#anthor wayy
print("Welcome to roller coaster")
height=int(input("Enter the height in cm"))
bill=0
if height>=120:
    print("Your are eligible for roller coster")
    age=int(input("Enter your age"))
    if age<12:
        print("Child tickets $5")
        bill=5
    if age<18:
        print("Youth tickets are $7")
        bill=7
    else:
        print("Adults tickets are $12")
        bill=12
    want_photo=input("Do you want Y OR N")
    if want_photo=='Y':
        bill+=3
        print(f"your total bill be {bill}")
    else:
        print(f"you total bill be {bill}")
else:
    print("Sorry you need to grow taller")
    
##################
#####Task-3
#Question=>
""" if your age is under 18 then ticket will be 20 rupees
if your age is grater than 18 then ticket will be 50 RS
if your age is grater then 12 and height is equal ro 120 cm then ticket
will be 20RS
if your age is between 12-15 and height is 120 then tickets is 15RS"""

age=int(input("Enter your age"))
height=int(input("Enter yuor height"))

if age<18:  
    print("Ticket is 20Rs")
elif age>18:
    print("Ticket is 50 RS")
elif age<12 and height==120:
    print("Ticket is 20 RS")
elif age<=12 or age<=15 and height==120:
    print("Ticket is 15 RS")
else:
    print("Enter valid value")    
#########################################################    
#Assignment
##Password creation 
#1)Username
users=["admin","Employee","manger","Worker","Staff"]

for user in users:
    if user=="admin":
        print("Hello admin")
    elif user=="Employee":
        print("Helllo Employee")
    elif user=="manger":
        print("Hello Manger")
    elif user=="Worker":
        print("Hello worker")
    elif user=="Staff":
        print("Hello worker")
    else:
        print("Invalid user")
#################################################

##linked in Question
def main():
    numbers = [10, -5, 20, -3, 8, -1, 15, -7, 12]
    
    positive_numbers = [num for num in numbers if num > 0]
    positive_sum = sum(positive_numbers)
    
    print("List of numbers:", numbers)
    print("Positive numbers:", positive_numbers)
    print("Sum of positive numbers:", positive_sum)
main()
## 
def p_no():
    l=[2,3,-1,-2,-3]
    
    add=[num for num in l if num>0]
    positve_add=sum(add)
    print("addtion of +ve no:",positve_add)
print(p_no())
#####
def main():
    sentence = input("Enter a sentence: ")
    
    words = sentence.split()
    word_count = len(words)
    
    print("Input sentence:", sentence)
    print("Number of words:", word_count)

if __name__ == "__main__":
    main()
####
def count_words():
    sentence=input('enter sentence')
    
    word=sentence.split()
    count_words=len(word)
    print("Total word is:",count_words)
print(count_words())

########################################################
####                assignment=password generation
import string
#pick the adjectives
adjectives=['sleepy','slow','fat','smelly','green','purple']
#pick the nouns
nouns=['panda','apple','goat','duck','dinosaur','ball']
#pick the word
import random  
#here we use choice mehod to get adjective and noun

adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select the number
number=random.randrange(0,100)
#select special character
special_char=random.choice(string.punctuation)
#create new secure password
password=adjective + noun + str(number) +special_char
print("Your new password is: %s" %password)
#below is my way
print(f"my New password is :{adjective}{noun}{number}{special_char}")
###############################################3
#another way
#by using while loop
print("Welcome to password picker")
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    #select the number
    number=random.randrange(0,100)
    
    #select special character
    special_char=random.choice(string.punctuation)
    #create new secure password
    password=adjective + noun + str(number) +special_char
    print("Your new password is: %s" %password)
    response = input("Wolud you like to generate another password ? type y or n")
    if response =='n':
        break
#####################################################################
 
#write python code for password is good or not
#determin strong password or not.we define strong password if it follows
#following conditions
#it must have at least 8 character
#at least one Uppercase letter
#at least one lowercase letter


def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
#check each character in the password and see which
#requirment meets

    for ch in password:
        if ch>="A" and ch<="Z":
            has_upper=True
        if ch>="a" and ch<="z":
            has_lower=True
        if ch>="0" and ch<="9":
            has_num=True
            
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
    
password=input("Enter password")    
if checkPassword(password):
    print("Strong Pasword")
else:
    print("Weak Password")
################################
#task
######
print("Welcome to pizza hut")
size_pizza=input("Enter pizza size")
add_pepp=input("Do you want to add pepp")
add_chees=input("Do you want extra chees")
bill=0
if size_pizza=="small":
    bill = 15
elif size_pizza=="medium":
    bill = 20
elif size_pizza=="large":
    bill = 25
if add_pepp=='y' and size_pizza=="small":
        bill+=2
if add_pepp=='y' and size_pizza=="medium" or size_pizza=="large":
        bill+=3
if add_chees=="y":
        bill+=1
print(f"Your bill is {bill} $")   
##################33
def build_person(first_name,last_name):
    #return dictionary of information about a person
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('Ram', 'sarkar')
print(musician)
############################
#passing list 
#
def greet_user(usernames):
    for name in usernames:
        msg=f"Hello! {name.title()}"
        print(msg)
usernames=['Anu','sakshi','Rutu']
greet_user(usernames)
########################
###above code in different way
def greet_user(names):
    for name in names:
        msg=f"Hello! {name.title()}"
        print(msg)
usernames=['Anu','sakshi','Rutu']
greet_user(usernames)

########################################################
################2ndTYPE =>Arbitary Argument


#passing an arbitary number of arguments 
def make_pizza(*topping):
#print the list of toppings that have been requsted    
    print(topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#we can replace the print()call with a loop that runs through
#ths list toppings and describes the pizza being ordered
def make_pizza(*toppings):
    print("\n making pizzz with followings topping: ")
    for topping in toppings:  
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
###########################3
#Mixing Positional and arbitary arguments
def make_pizza(*toppings):
    print("\n making pizzz with folowings topping: ")
    for topping in toppings:  
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

####################

def info(*me):
    print("Here is list:",me)
print(info('a','b','c','d'))
######################################

############KEYWORD ARGUMENT############
#this type of argument is used in AI
#output will be in from of dictionary i.e. keys &values

#represent as **kwargs
def person(name,**data):
    print('name is:',name)
    print(data)
person(name='Navin',age=28,place='Mumbai',mob_no=987654321)

#################
##another way
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='Navin',age=28,place='Mumbai',mob_no=987654321)

#another way     
def info(**me):
    print("Here is my info:",me)
info(a='b',c='d')
        


