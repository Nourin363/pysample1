# 1 left hand triangle numbers floyds
# n=5
# count=0
# for i in range(0,n):
#     for j in range(0,i+1):
#         count+=1
#         print( count ,end=" ")
#     print()

#2 left hand triangle
# n=5
# # count=0
# for i in range(0,n):
#     for j in range(0,i+1):
#         # count+=1
#         print( "*" ,end=" ")
#     print()

# 3 right hand triangle
# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

#4 full pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

#5 floyds triangle with 1 number ahead
# n=4
# for i in range(0,n):
#     count=i+1
#     for j in range(0,i+1):
#         print(count,end=" ")
#         count+=1
#     # for k in range(0,n-1):
#     #     print("*",end=" ")
#     print()


#6 inverted right hand triangle
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()



#7 RHOMBUS PATTERN
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-1):
#         print("*",end=" ")
#     print()

#8 inverted full pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()


#9 hourglass pattern
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()
# n = 5
# for i in range (1,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()


#10 diamond
# n = 5
# for i in range (0,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range (1,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()

#11 hallow square
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()

#12 hollow diamond
# n = 5
# for i in range(0, n):
#     for j in range(0, n - i):
#         print(" ", end="")

#     for k in range(0, i + 1):
#         if k == 0 or k == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(1, n):
#     for j in range(0, i + 1):
#         print(" ", end="")

#     for k in range(0, n - i):
#         if k == 0 or k == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#13 hallow inverted full pyramid
# n = 5
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print(" ", end="")

#     for k in range(0, n - i):
#         if i==0 or k == 0 or k == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#14 hallow full pyramid
# n = 5
# for i in range(0, n):
#     for j in range(0, n - i):
#         print(" ", end="")

#     for k in range(0, i + 1):
#         if i==0 or i==n-1 or k == 0 or k == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()