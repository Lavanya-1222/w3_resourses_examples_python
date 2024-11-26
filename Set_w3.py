# 1. Write a Python program to create a set.
# s=set()
# print(s)

# 2. Write a Python program to iterate over sets.

# s=list(range(1,5))
# s=
# for i in s:
    # print(i)

# 3. Write a Python program to add member(s) to a set.

# s=set(range(1,5))
# s.add(6)
# print(s)

# 4. Write a Python program to remove item(s) from a given set.
# s=set(range(1,5))
# print(s.pop())
# print(s)



# 5. Write a Python program to remove an item from a set if it is present in the set.
# s=set(range(1,4))

# s.remove(9)
# print(s.discard(3))
# print(s)

# 6. Write a Python program to create an intersection of sets.

# s1={'samarth,"lavanya',"saranya"}
# # s2=["saransh","saranya"]
# s2={"saransh","saranya"}
# print(s1.intersection(s2))
# print(s1 & s2)//it gives error if you try to intersect onthet than set type

# 7. Write a Python program to create a union of sets.

# s1={'samarth','lavanya',"saranya"}
# s2={"saransh","saranya"}
# s3={"nagesh","chandra kala"}
# print(s1.union(s2,s3))

# 8. Write a Python program to create set difference.
# print(s1.difference(s2))

# 9. Write a Python program to create a symmetric difference.
# print(s1.symmetric_difference(s2))

# 10. Write a Python program to check if a set is a subset of another set.

# s1={'samarth','lavanya',"saranya"}
# s2={"saranya"}
# print(s2.issubset(s1))
# print(s1.issubset(s2))

# 11. Write a Python program to create a shallow copy of sets.

s={1,2,3,4,5}
# s2=s.copy()
# s.pop()
# s3=s
# print(s2,s3)

# 12. Write a Python program to remove all elements from a given set.
# del s
# s.clear()
# print(s)

# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.

# 14. Write a Python program to find the maximum and minimum values in a set.
s=set(range(1,10))
# print(max(s),min(s))

# 15. Write a Python program to find the length of a set.
# print(len(s))

# 16. Write a Python program to check if a given value is present in a set or not.
# print(90 in s)

# 17. Write a Python program to check if two given sets have no elements in common.
s={"lava","sama","sara","kara"}
s2={"kara","sara"}
# print(s.isdisjoint(s2))
# if s.intersection(s2):
#     print(True)
# else:
#     print(False)

# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
# print(s.issuperset(s2))
# print(s.issuperset(s))

# 19. Write a Python program to find elements in a given set that are not in another set.
# s={"l","a","v","s"}
# s2={"s","k","o"}
# print(s.difference(s2))

# 20. Write a Python program to remove the intersection of a second set with a first set.
# s.discard(s.intersection(s2))

# 21,


# 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
# nums = set({10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20})
# c=0
# list=[]
# for i in nums:
#     c=35-i;
#     if c in nums:
#         list.append({i,c})
# print(list)