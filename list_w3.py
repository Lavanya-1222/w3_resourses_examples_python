
#6--------------------------

# list=input().split(" ")
# print(list)
# print(tuple(list))

# 7-----------------------------

# s=input()

# i=s.find('.')
# print(s[i+1:])

# list=[9,9,9,0]

# print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', 
#  '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
#  '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__',
#    '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', 
#    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
#    '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#   'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# list=[1,2,1,1,1]
# ----------------------1--------------------
# print(sum(list))
# s=0
# for i in list:
#     s=s+i;
# print(s)
# 3-----------------------------------------------
# print(max(list))
# max=0
# for i in list:
#     if i>max:
#         max=i
# print(max)

# 5-------------------------------------------------
# list=["abc","aca","121","mom"]

# for i in list:
#     if len(i)>=2:
#         if(i[0]==i[-1]):
#             print(i)

# 6---------------------------------------------------

# list=[2,3,4,2,6,7,4]

# for i in list:
#     if list.count(i)>=2:
#         list.remove(i)

# print(list)
# list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list2=list.copy()
# # print(len(list2)==0)
# print(list2)
# list2[0]="lava"
# print(list,list2)

# 10-----------------------------------------
# list=['i','p','o','am','lavanya','how','are','you','all','guyes','o']
# list2=[]
# n=3
# for i in list:
#     if len(i)<n:
        
#         list.remove(i)
#     print(len(i))
# # print(list)

# 11--------------------------------------------------

# list=[2,3,4,5,10]
# list2=['lava',7,8]

# list=['Hello', '', '', 'World', '', 'Lol']
# f=[]
# print(list)
# for  i in list:
        

#             # f.append(i.replace(i[0],i[0].upper()))
#             f.append(i.capitalize())
            
  
# print(f)
# //11----------------------------------------
# list1=[6,7,5,9,1,8]
# list2=[1,2,3,4,5]

# for i in list1:
#     for j in list2:
#         if j==i:
#             print("true")
#             break

# 12--------------------------------------

# list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(id(list))
# list=list[1:4]
# print(id(list))

# print(list)

# 14------------------------------
# list=[1,2,4,5,6,1,9,10,12]
# list2=[]
# for i in list:
#     if(i%2!=0):
#         list2.append(i)
# print(list2)

# 15---------------------------------
# from random import shuffle
# list=[1,2,4,5,6,1,9,10,12]
# # list.sort()
# # list=list[3:len(list)]+list[:3]
# # print(list)
# shuffle(list)
# print(list)

# 16-----------------------------------

# list=[1,2,3,4,5,23,23,24,25,1,2,3,4,5]
# list=[]
# for i in range(1,21):
#     list.append(i**2)
# print(list[:5],list[-5:])

# 17-------------------------------------

# list1=[2,3,5,7,13]
# # print(list1)
# def p(list1):
#  f="true"
#  for i in list1:
#     if(i==1):
#             return "false"
#     else:
#      for j in range(2,i):

#         if (i%j==0  and i!=2):
#             return 'false'
#         else:
#             pass
#  return f

# print(p(list1))


# 19-------------------------------------

list1=[10,20,30,3]
list2=[1,2,3,40,1,3,5]
# p=[]
# for i in range(len(list1)):
#     if(list1[i]>list2[i]):
#       p.append(list1[i]-list2[i])
#     else:
#       p.append(list2[i]-list1[i])
# print(p)
# d=[]
# if len(list1)>len(list2):
#   for i in list1:  
#     if i not in list2:
#         d.append(i)

# else:
#  for i in list2:  
#     if i not in list1:
#         d.append(i)
# print(d)

# 20----------------------------------

# list=[10,20,30,40]

# for i in list:
#     print(i,list.index(i))

# 21-----------------------------------
# list=['a','s','a','m','u']
# print("".join(list))

# 22-------------------------------------
                                                #    23,18 ?
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# # list1.append(list2)
# print(list1+list2)