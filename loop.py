#while loop
# count=1
# while count<=5:
#     print(count)
#     count+=1

# count=10
# while count>=1:
#     print(count)
#     count-=1

# count=1
# while count<=10:
#     if count%2==0:
#         print(count)
#     count+=1

# sum=0
# n=int(input("enter a number: "))
# while n!=-1:
#     sum=sum+n
#     n=int(input("enter a number: "))
# print(sum)

#for loop

# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))   

# tuple_=("python","loops","sequence","condition","range.")
# for iterator in range(len(tuple_)):
#     print(tuple_[iterator].lower(),end=" , ")

# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The List of squares is:",squares)

# string="Python Loop"
# for s in string:
#     if s=="o":
#         print("If Block")
# else:
#     print(s)

# i=int(input("enter a number: "))
# rev=0
# n=len(str(i)) 
# num=0
# for y in range(n):
#     n=i%10
#     rev=rev*10+n
#     i=i//10
# print(rev)

# num=int(input("Enter the number: "))
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

# num=int(input("Enter the number: "))
# j=int(input("Enter the range: "))
# mul=0
# for i in range(1,j+1):
#     mul=i*num
#     print(i,"*",num,"=",mul)

# text=input("Enter the string: ")
# reverse=""
# for i in text:
#     reverse= i+reverse
#     print("reversed string is:",reverse)


# a=text[::-1]
# print(a)

# while true condition
# sum=0
# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multipication")
#     print("4. Division")
#     print("5. Modules")
#     print("6. Exit")
    
#     choice = int(input("Enter your choice: "))
#     if choice==1:
#         a=int(input("Enter the number: "))
#         b=int(input("Enter the number: "))
#         print("sum=",a+b)

#     elif choice==2:
#         a=int(input("Enter the number: "))
#         b=int(input("Enter the number: "))
#         print("sub=",a-b)

    
#     elif choice==3:
#         a=int(input("Enter the number: "))
#         b=int(input("Enter the number: "))
#         print("mul=",a*b)

    
    # elif choice==4:
    #     a=int(input("Enter the number: "))
    #     b=int(input("Enter the number: "))
    #     if b!=0:
    #         print("div=",a/b)
    #     else:
    #         print("Not Divisible")

    # elif choice==5:
    #     a=int(input("Enter the number: "))
    #     b=int(input("Enter the number: "))
    #     print("mod=",a%b)

    # elif choice==6:
    #     break

        # print("Invalid Choice")

        
# registration
# username=""
# password=""    
# while True:
#     print("1.REGISTRATION")
#     print("2.LOGIN")
#     print("3.EXIT")
#     choice= int(input("Enter the choice: "))
#     if choice==1:
#         name=(input("ENTER YOUR NAME: "))
#         age=int(input("ENTER YOUR AGE: "))
#         if age<=18:
#             print(age)
#         else:
#             print("invalid age")
#         address=(input("ENTER YOUR ADDRESS: "))
#         phone_number=int(input("ENTER YOUR PHONE NUMBER: "))
#         if phone_number==10:
#             print(phone_number)
#         else:
#             print("invalid number")
#         username=(input("ENTER YOUR USERNAME: "))
#         password=(input("ENTER YOUR PASSWORD: "))

#     elif choice==2:
#         username1=(input("ENTER YOUR USERNAME: "))
#         password1=(input("ENTER YOUR PASSWORD: "))
#         if username==username1:
#             if password==password1:
#                 print("name:",name,
#                 "age:",age,
#                 "address:",address,
#                 "phone number:",phone_number)
#         else:
#             print("invalid")

#     elif choice==3:
#         break
         
# changing the numbers
# a= "Hello World!"
# print(a[0:9:2])

# reversing the word
# a= "Hello World!"
# print(a[::-1])

# immutable 
# a= "Hello World"
# print(a[::-1])
# a[1]="y"
# print(a)

# length
# a="Hello World"
# for i in range(len(a)):
#     print(a[i])

# upper case
# message='PYTHON IS FUN'
# print(message.lower())

# lower case
# message='python is fun'
# print(message.upper())

# count
# txt="betty brought a better butter to make her bitter butter better "
# x=txt.count("r")
# print(x)

# find
# message= 'Python is a fun  programming language'
# print(message.find('language'))

# replace
# text='baseball bat is quite expensive than cricket bat'
# replaced_text=text.replace('ba','ro')
# print(replaced_text)

# append
# numbers=[21,34,54,12]
# print("before append:",numbers)
# numbers.append(90)
# print("after append:",numbers)

# insert
# vowels=['a','e','i','u']
# vowels.insert(3,'o')
# print('list:',vowels)

# extend
# prime_numbers=[2,3,5]
# print("list1: ",prime_numbers)
# even_numbers=[4,6,8]
# print("list2: ",even_numbers)
# prime_numbers.extend(even_numbers)
# print("list after append: ",prime_numbers)

# change list items
# languages=['python','swift','c++']
# languages[2]='c'
# print(languages)

# list is a mutable datatype;

# empty strng
# a=""

# empty list
# a=[]

# appending the numbers to the list
# a=[]
# n=int(input("Enter how  many numbers u want to print: "))
# for i in range(0,n):
#     m=int(input("Enter the numbers: "))
#     a.append(m)
# print(a)

# appending only even numbers in the list

# printing a pattern 
# n=5
# count=0
# for i in range(1,n):
#     for j in range(0,i):
#         count=j+1
#         print(count,end=" ")
#     print()

# 1st method
# for r in range(1,6):
#     num=r
#     for st in range(1,r+1):
#         print(num,end=" ")
#         num+=r
#     print(" ")

# 2nd method
# for r in range(1,6):
#     for st in range(1,r+1):
#         print(st*r,end=" ")
#     print(" ")

# for i in range(1,6):
#         for j in range(1,i+1):
#                 print(i*j,end=" ")
#         print()