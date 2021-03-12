# Method 1 by using temp (Extra memory of a variable is used)
a = 5   
b = 6   
temp = a
a = b
b = temp

print(a)
print(b)

##############################################
# Method 2 without 3rd variable (Extra memory of a bit is used)
x = 5   # 101
y = 6   # 110
x = x + y  # x = 11 i.e. 1011 in binary(4 bits)
y = x - y  # y = 11 - 6 = 5
x = x - y  # x = 11 - 5 = 6

print(x)
print(y)

###########################################
# Method 3 (Using XOR)
p = 5
q = 6

p = p^q
q = p^q
p = p^q

print(p)
print(q)

# Method 4 Exclusive to python
w = 5
v = 6
w,v = v,w  # use the concept of rot two in python

print(w)
print(v)


