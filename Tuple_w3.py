# 1. Write a Python program to create a tuple.


# t=("lava",)
# t2=tuple()
# print(t,t2)

#  2 Write a Python program to create a tuple with different data types.

# t=(1,2,False,4.7,"lss")
# print(t)

# 3. Write a Python program to create a tuple of numbers and print one item.
# t=tuple(range(1,20))
# t2=5,3,4,
# t3=5,
# print(t,t2,t3)

# 4. Write a Python program to unpack a tuple into several variables
# lava,sneha,sharda=("Samarth","sujith","Balkrushna")
# print(lava,sneha,sharda)

# 5. Write a Python program to add an item to a tuple.

# t=(1,2,3,4,5)
# t=list(t)
# t.append(19)
# t=tuple(t)
# print(t)

# t=t+(20,)
# print(t)

# # 6. Write a Python program to convert a tuple to a string.
# t=('1','2','3','4','89')
# # t=list(t)
# # t=str(t)
# t="-".join(t)
# print(type(t),t)

# 7. Write a Python program to get the 4th element from the last element of a tuple.
# t=(0,1,2,3,4,5,6,7,8,9,10)
# print(t[4],t[-4])

# 8. Write a Python program to create the colon of a tuple.
# t1=(1,2,3,4)
# t2=t1
# print(t2)

# # 9. Write a Python program to find repeated items in a tuple.
# t=(1,2,3,4,1,2,5,6,8,2,4,9)
# p=[]
# for i in t:
#     if i not in p:
#         p.append(i)
#     else:
#         print(i)

# 10. Write a Python program to check whether an element exists within a tuple.
# t=(1,2,3,4)
# i=40

# print(i in t)

# 11. Write a Python program to convert a list to a tuple.
# list=[1,2,3,4]
# list=tuple(list)
# print(list,type(list))

# 12. Write a Python program to remove an item from a tuple.
# t=(12,2,3,45,6,90)
# t=list(t)
# t.remove(45)
# print(t)

# 13. Write a Python program to slice a tuple.

# t=(10,20,30,40)
# print(t[2:4])

# 14. Write a Python program to find the index of an item in a tuple.
# t=(10,20,30,40)
# print(t.index(20))

# 15. Write a Python program to find the length of a tuple.
# t=(10,2,3,40)
# print(len(t))

# 16. Write a Python program to convert a tuple to a dictionary.

# 18. Write a Python program to reverse a tuple.

# t=('one','two','three')
# print(t[::-1])

# 19. Write a Python program to convert a list of tuples into a dictionary.


# 20. Write a Python program to print a tuple with string formatting.
# t=(100,200,300)
# print('Tis is a tuple ',str(t))


# 21. Write a Python program to replace the last value of tuples in a list.
# list=[(10,20,30),(40,50,60),(70,80,90)]
# list2=[]
# for i in list:
#     # print(type(i[:2]))
#     list2.append(i[:2]+(100,))

# print(list2)

# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.

# list=["",{}, (),0,False, ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# list2=[]
# for i in list:
#     if(i):
#         list2.append(i)

# print(list2)

'''23. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] '''

list1=[10, 20, 30, (10, 20), 40]
c=0
# for i in list1:
#     if type(i) == tuple:
#         break
#     else:
#         c=c+1

# for i in list1:#2nd method
#     if isinstance(i,tuple):
#         break
#     c=c+1;
# print(c)
# print(type(list1)==tuple)

#25 Write a Python program to convert a given string list to a tuple.
# Original string:  python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# <class 'tuple'>

# s="python 3.0"
# s=list(s)
# print(tuple(s))
# print(" ".isspace())

# 26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648
# mul=1
# t=(4, 3, 2, 2, -1, 18)
# for i in t:
#     mul=mul*i;
# print(mul)


# 27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]

# t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# list=[]
# for i in t:
    
#     list.append(sum(i)/len(i))
# print(list)

# 28. Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

# t=(('333', '33'), ('1416', '55'))
# list1=[]
# for i in t:
#      list1.append((int(i[0]),int(i[1])))

#     #  list2=tuple(list2)
#     #  list1.append(list2)
# print(list1)



# 29. Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

# t=(10, 20,0,30)
# l=""
# for i in t:
#     l=l+str(i)
# print(int(l))

# 30. Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False

# t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# def check(t):
#  for i in t:
#         if "Whitew" in i:
#             return True
#  return False
# print(check(t))

# 31. Write a Python program to compute the element-wise sum of given tuples.
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

# for i in x+y+z:

'''33. Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''

# t=[(1, 2), (2, 3), (3, 4)]
# list1=[]
# for i in t:
#     list1.append(list(i))
# print(list1)