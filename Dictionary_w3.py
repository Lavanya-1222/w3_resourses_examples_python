# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# d={0:10,1:20}
# d.update({10:20})
# print(d)

# 1. Write a Python script to sort (ascending and descending) a dictionary by values

# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dic4={}
# for i in (dict1,dict2,dict3):
#     dic4.update(i)
# print(dic4)     

# 4. Write a Python script to check whether a given key already exists in a dictionary.
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print(6 in d.keys())

# 5. Write a Python program to iterate over dictionaries using for loops.
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# for i,v in d.items():
#     print(i,v)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n=5
# # dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# dict={}

# for i in range(1,5):
#     dict[i]=i**2
# print(dict)

# 8. Write a Python script to merge two Python dictionaries.
# dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# dict2={'o':90,'p':90,'l':9}
# dict1.update(dict2)

# print(dict1)

# 10. Write a Python program to sum all the items in a dictionary.

# dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(sum(dict.values()))

 
#11. Write a Python program to multiply all the items in a dictionary.
# dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# c=1
# for i in dict.values():
#     c*=i
# print(c)

# 12. Write a Python program to remove a key from a dictionary.
# dict1={'a': 1, 'b': 2, 'c': 3, 'd': 4}

# dict1.pop('c')
# print(dict1)


# 13. Write a Python program to map two lists into a dictionary.
# keys = ['red', 'green', 'blue']
# values = ['#FF0000', '#008000', '#0000FF']

# d=dict()

# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)
# # 14. Write a Python program to sort a given dictionary by key.
# dict2=dict()
# for key in sorted(d):
#     dict2[key]=d[key]
# print(dict2)

# 15. Write a Python program to get the maximum and minimum values of a dictionary.
# my_dict = {'x': 500, 'y': 5874, 'z': 560}

# print(max(my_dict.values()))

# 17. Write a Python program to remove duplicates from the dictionary.
# s={   'id1': {
#         'name': ['Sara'],
#         'class': ['V'],
#         'subject_integration': ['english, math, science']
#     },
#     'id2': {
#         'name': ['David'],
#         'class': ['V'],
#         'subject_integration': ['english, math, science']
#     },
#     'id3': {
#         'name': ['Sara'],
#         'class': ['V'],
#         'subject_integration': ['english, math, science']
#     },
#     'id4': {
#         'name': ['Surya'],
#         'class': ['V'],
#         'subject_integration': ['english, math, science']
#     }
# }
# dict1={}
# for k,v in s.items():
#      if v not in dict1.values():
#          dict1[k]=v
#     #  else:RuntimeError: dictionary changed size during iteration
#     #    s.pop(k)RuntimeError: dictionary changed size during iteration
   
          
# print(s.keys())
# print(dict1.keys())


# 18. Write a Python program to check if a dictionary is empty or not.
# d={1:90}
# if len(d)==0:
#     print('empty')
# else:
#     print("s")

'''19 Write a Python program to combine two dictionary by adding values for common keys.

Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for k,v in d1.items():
#     if k in d2.keys():
#         d3[k]=v+d2[k]
#     else:
#         d3[k]=v
                  
# print(d3)

# 20. Write a Python program to print all distinct values in a dictionary.
l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s=set()
for i in l:
    for k in i.values():
        s.add(k)
print(s)
