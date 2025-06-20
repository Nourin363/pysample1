#if statement
#program to check whether the number is positive
# i=10
# if i>=0:
#     print("the number is positive")

#program to check whether the number is divisible by 5
# i=30
# if i%5 == 0:
#     print("the number is divisible by 5")

#program to check whether the letter is a vowel
# let=input("enter a character:")
# vowel=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
# if let in vowel:
#     print(f"'{let}'is a vowel")
# else:
#     print(f"'{let}'is not a vowel")


#program to check whether the entered string is "PYTHON"
# i="python"
# if i=="python":
#     print("the string is python")

#if else statement
# i=199
# if i%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

#program to chech whether the person is eligible to vote
# i=14
# if i==18:
#     print("the person is eligible to vote")
# else:
#     print("the person is not eligin]ble to vote")

#program to find the greater number between 2 numbers
# i=20 
# j=10
# if i>j:
#     print("i is greater")
# else:
#     print("j is greater")

#program to find the leap year
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

#Write a Python program to calculate the water bill based on the number of units consumed
# units = int(input("Enter total units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 8
# else:
#     bill = (100 * 5) + (100 * 8) + (units - 200) * 10

# print(f"Total water bill for {units} units is: ₹{bill}")


#loops

#Sum of digits
# sum=0
# n=0
# i=int(input("enter a number: "))
# while i>0:
#     n=i%10
#     sum+=n
#     i=i//10
# print(sum)

#count the number of digits
# count=0
# i=int(input("enter a number: "))
# while i>0:
#     n=i%10
#     count +=1
#     i=i//10
# print(count)

#armstrong
# i=int(input("enter a number: "))
# temp=i
# sum=0
# num_digits = len(str(i))
# while temp>0:
#     n=temp%10
#     sum += n ** num_digits
#     temp=temp//10
# if sum==i:
#     print("it is an armstrong number")
# else:
#         print("it is not an armstrong number")

#palindrome
temp=0
rev=0
i=int(input("enter a number: "))
temp=i
while temp>0:
    n=temp%10
    rev=rev*10+n
    temp=temp//10
if rev==i:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")



