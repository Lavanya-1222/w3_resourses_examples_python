# a,b='abc','xyz'

# print(a,b)

# temp=b[0:2]
# b=a[0:2]+b[2:]
# a=temp+a[2:]

# print(a,b)




#6----

# s=input();
# if(len(s)>2):
 
#  if(s[-3:]=='ing'):
#     print(s+'ly')
#  else:
#     print(s+'ing')


# 7------------


# s='The lyrics is not that poor!'

# i=s.find('not')
# if 'poor' in s[i:]:
#     s=s[:i]+'good'
#     print(s)

# 8----------

# s="lavanya is very87874878jfdnd peacfull person"

# list=s.split(" ")
# print(list)
# # len=0;
# max=0
# for i in list:
#     if(len(i)>max):
#         max=len(i)
#         var=i

# print(var,max)



# 9-----------

# s="lavanya"
# n=4
# s=s.replace(s[n],"")
# print(s)


# 11-----------

# s="abcdef"
# s2=''
# # s2=s[1]
# for i in range(len(s)):
#      if(i%2!=0):
#           s2=s2
#      else:
#           s2=s2+s[i]
    
    
# print(s2)



# 14-----------

# s="hello i am lavanya hello my name is lavanya "

# list=["lava","yellow","abc","tyu"]

# print(sorted(list))


# 15-----------

# s="python"
# tag="h"

# print("<{0}> {1} </{0}>".format(tag,s))


#16---------------------

# par='{{}}}'
# s="lavanya"
# lenth=len(par)//2
# print(par[:lenth],s,par[lenth:])


#17--------------------------

# s="laavv"

# print(s[-2:]*4)


# 19--------


# s="www.google.com-about"

# list=[]
# for i in range(33,49):
#     list.append(chr(i))


# print(list)
# for i in range(len(s)-1,0,-1):
#     if s[i] in list:
#         print(s[i+1:])
#         break;


#20-------------

# s="lavanyna"

# if(len(s)%4==0):
#    print(''.join(reversed(s)))

#21-------------------------

# s="lavNya"

# for i in s[:5]:
#     if(i.isupper()):
#         print(s.upper())

# 22-----------
# s="lavanya"
# print(''.join(sorted(s)))


#23-------------------------

# s="lavanaya\n"
# print(s.rstrip())
# print(s.startswith('lava'))

#24--------------------------

# s='''Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.'''

# print(s.lstrip())
# s=3.2456

# print('{:.0f}'.format(s))

# 33-------------

# w=5;
# s='L'
# print(s.rjust(w,'^'))

# 34-----------

# 38------------------------------
# s='knyanuknyanuuih'
# print(s.count('knyanu'))

# 39----------------------------------
s='lavanya'
p=len(s)-1
print(p)
# print(''.join(reversed(s)))

# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# 40---------------------------------------


# s=" i am lavanya"
# list=s.split(" ")

# print(list[::-1])

# 41---------------------------------------


# list=['a','i','o','u','e']
# l='aioue'

# s='samariteh'
# s2=''
# for i in range(len(s)):
#     if s[i] in l:
#         pass
#     else:
#         s2=s2+s[i]
# print(s2)


# 42-------------------------------------
# s="lavanyasamarthmadure"

# for i in s:
#     print(i,s.count(i))

# 43----------------------------------------


# s='lavanyasamarthmadure'

# for i in range(len(s)):
    
#     print('current char {} and index {}'.format(s[i],i
#                                                 ))
    

# a='abcdefghijklmnopqrstuvwxyz'

# s='the quick brown fox jumps over the lazy cat'
# s1=set(s);
# print(len(s1))
# flag=0
# for i in s1:
#     if(ord(i)>=97 or ord(i)<=122):
#         flag=1
#     else:
#         flag=0
#         break
# print(flag)


# 48---------------------------


# s="SAMARTH"

# n=2
# print(s[:n+1].lower()+s[n:])

# 49--------------------------------

# s='34.999,87'
# s2=''
 

# for i in s:
# s="lava mira."
# print(s[0:])
    