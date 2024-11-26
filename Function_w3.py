# # 1. Write a Python function to find the maximum of three numbers.
# def max_3(x,y,z):
#     if(x>y and x>z):
#         return x
#     elif(y>x and y>z):
#         return y
#     else:
#         return z
# print(max_3(19,20,10))

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# def sumlist(list):
#     return sum(list)
# print(sumlist([8,2,3,0,7]))

# 4. Write a Python program to reverse a string. Website builder
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def restring(s):
#     return s[::-1]
# print(restring("1234abcd"))

# 5. Write a Python function to calculate the factorial 
# of a number (a non-negative integer). The function accepts the number as an argument.

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(fact(4))

# 6. Write a Python function to check whether a number falls within a given range.
# Click me to see the sample solution
# def frange(n,e,s=0):
#     if n>=s and n<=e:
#         return True
#     return False
# print(frange(5,7,2))

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# def ulcheck(s):
#       cl=0
#       cp=0
#       for i in s:
#             if(i.isupper()):
#                   cp+=1
#             elif(i.islower()):
#                    cl+=1
#       return cl,cp
# print(ulcheck('The quick Brow Fox'))

# def listcheck(l):
#     l=set(l)
#     return list(l)
# print(listcheck([1,2,3,3,3,3,4,5]))


# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# def primecheck(n):
#     if(n==2):
#         return True
#     else:
#         for i in range(2,n):
#             if (n%i==0):
#                 return False
#             else:
#                 return True
# print(primecheck(14))
    

'''10. Write a Python program to print the even numbers from a given list. Website builder
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

# def checkeven(list):
#     list1=[]
#     for i in list:
#         if(i%2==0):
#             list1.append(i)
#     return list1
# print(checkeven([1,2,3,4,5,6,7,8,9]))


# 12. Write a  Python function that checks whether a passed string is a palindrome or not.
# def checkpalindrom(s):
#     if s[::-1]==s:
#         return True
#     else:
#         return False
# print(checkpalindrom("mosm"))

'''14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy cat"'''

def checkpangram(s):
 flag=0
 list=set(s)

print(4+'5')
 

print(checkpangram("The quick brown fox jumps over the lazy cat"))