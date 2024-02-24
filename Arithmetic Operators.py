
############   24/7/2023    ###########

######### Arithmetic Operators    ###########

home =10
away =15

print(home+away)
print(type(home+away))

print(49*3)
print(type(49*3))

#################
#Subtraction
goals_for=10
goal_agins=7
print(goals_for-goal_agins)

###########
#Division
#if we divide integer two number then result will be in  a flaot
print(100/7)
print(type(100/7))

###########
#Floor Division
#if we divide integer two number then result will be in  a int use //
print(100//7)
print(type(100//7))

###################
#Modulas
#finding of reminder
print("modules division 100%3",100%3)
print(type(100%3))

###################

#Exponential
a=3
b=5
print(3 ** 5)

#######################################################

#########     Asssigment Operators

#1]  =,+=
#Adds the value on the right to the variable on 
#the left and assigns the result back to the variable.

x =2
x+=1   #has the same behavoir as x= x+1
x 


#2] -=

# Subtracts the value on the right from the 
#variable on the left and assigns the result back to the variable
x =2
x-=1   #has the same behavoir as x= x-1
x 

################################
#3] *=
#Multiplies the variable on the left by the value 
#on the right and assigns the result back to the variable.

x =2
x*=1   #has the same behavoir as x= x*1
x
#########################

# 4]  /=
# Divides the variable on the left by the value 
#on the right and assigns the result back to the variable.
x =2
x/=1   #has the same behavoir as x= x+1
x 

#########################################

#           Identity Operator
'''
1)is: Returns True if both operands refer to the 
same object, otherwise returns False.

2)is not: Returns True if both operands do not 
refer to the same object, otherwise returns False.

'''
winner = None 
print(winner is None)

winner = None 
print(winner is not None)

print(type(winner))

winner = True 
print(type(winner))

#############################################333

#indendation
num =10
if num >2:
    print("number is grther than 2")
    if num>5:
        print("number is grther than 5")
        if num>15:
            print("number is grther than 15")
#################

num1=int(input("enter the number: "))
if num1 < 0:
    print("number is -ve")
else:   
    print("number is Positive")
