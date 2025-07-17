# def square( num ): #function
#     return num**2 #function {num is an argument} {return statement is optional}
# object_=square(6)  #function calling {object_ is a variable}
# print("The square of the given number is:",object_)

#without return statement
# def square( num ): 
#     print (num**2)
# square(6)  

# funtion can be called multiple times
# parameters are inside the paranthesis of function definition and arguments are inside the paranthesis of function call

# print the length of a string
# def a_function( string ):
#     return len(string)
# print(a_function("Functions"))
# print(a_function("Python"))

# function calling 4 types
# with argument with return
# square of a number
# def square(num):
#     return num*num
# result=square(5)
# print("Square:",result)

# with arg without return
# function to print greetings
# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")

# without arg with return
# welcome message
# def get_message():
#     return "Welcome to Python programming! "
# msg=get_message()
# print(msg)

# without arg without return
# print numbers
# def print_numbers():
#     for i in range(1,6):
#         print (i)
# print_numbers()

# function arguments 2 types
# default argument
# def function(n1,n2=20):
#     print("number 1 is: ",n1)
#     print("number 2 is: ",n2)
# print("Passing only one argument")
# function(30)

# keyword argument
# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Without using keyword")
# function(n1=20,n2=30)

# FACTORIAL WITHOUT RETURN
# a=int(input("Enter the number: "))
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# fact(a)

# displaying name and age using def
# def display(name,age):
#     print(f"Hi! My name is {name}. My age is {age}. ")
# display(name="Nourin",age="20")
    
# displaying name and age using **
# def display(**a):
#     print(f"Hi {a['name']}. Welcome to {a['course']} course.")
# display(name="Nourin",course="Python")

# calculation
# def display(**kwargs):
#     print(kwargs)
#     print(kwargs['message'],kwargs['answer'])

# def add(x,y):
#     ans=x+y
#     display(message=f"Sum of {x} and {y} is", answer=ans)
# def sub(x,y):
#     ans=x-y
#     print(ans)
# def mul(x,y):
#     ans=x*y
#     print(ans)
# def div(x,y):
#     ans=x/y
#     print(ans)
# def mod(x.y):
#     ans=x%y
#     print(ans)
#  while True:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print("Please enter your choice: \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Modulus")
#     choice = int(input("Enter your choice: "))
#     if choice==1:
#        add(a,b)

#     elif choice==2:
#         sub(a,b)

    
#     elif choice==3:
#         mul(a,b)

    
#     elif choice==4:
#         div(a,b)
        

#     elif choice==5:
#        mod(a,b)

#     else:
#         print("Please enter a valid input from choices given:")

# multiple values can be returned

# recursion
# a function calling itself
# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)

# print (fact(5))

# def fun():
#     print("hello")
#     fun()
# fun()

# first,second=0,1
# print(first,second,end=" ")
# for j in range(8):
#     third=first+second
#     print(third,end=" ")
#     first,second=second,third


