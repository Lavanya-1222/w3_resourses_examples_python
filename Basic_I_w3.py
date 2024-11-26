# print("Hello", end="\n ")

# Using as String:
# %s is used to refer to a variable which contains a string.
i=78
p=9.0
# print("Integer:%s"%i)

# using multiple varibles
# print("float Variable %f & %f"%(i,0.9))
# The default Precision Width is set to 6.

# you can specify width
# print("%.2f"%9.5)


# Zero padding
# Zero padding is done by adding a 0 at the start of fieldwidth
# print("%010.2f"%i)

#  proper alignment
# For proper alignment, a space can be left blank in the field 
# width so that when a negative number is used, proper alignment is maintained.
# print("% .2f"%i)

# specifying a negative symbol
# As mentioned above, the data right aligns itself when the field width mentioned is larger than the actually field width. But left alignment 
# can be done by specifying a negative symbol in the field width.
# print('%10.2f'%i)// if not given then it take space at right
# print("%-10.2f"%i)# now it takes space at right side




# print('{:<10}'.format("lavanya"))#add spaces in right
# print('{:>10}'.format("lavanya"))#adds space in right side
# print('{:^10}'.format('lavanya'))#is add space in center

# truncate string
# print('{:.10}'.format("i am lavanya"))

# Combining truncating and padding
# print('{:0>10.10}'.format("i am"))

# Padding numbers:
# print('{:0<5d}'.format(9))
# print('{:0>10.2f}'.format(7.89))

# Signed Number
# print('{: d}'.format(-23))
# print('{:+d}'.format(23))

# you can control space of sign
print('{:=5d}'.format(8))
print('{:05d}'.format(8))