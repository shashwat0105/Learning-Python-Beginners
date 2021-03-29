# In python
# string = a b c water anything
# But in other like C++
# char = a b c & string = water

# All three below are string in python(only condition that they should be in quotes single or double)
x = '1'
y = 'a'
z = 'water'


###### METHODS IN PYTHON 
print(z.title()) # make first letter capital
print(z.upper()) # will convert to uppercase
print(dir("string"))  # will show all the methods of string

# INDEXING
a = "hello"
print(a[2])  # prints l
print(a.replace('l', 'k')) # replaces all l with k

# SLICING
b = "hello world"
print(b[1:4])  # this means upto o not o so, ell will print out
print(b[1:5])
print(b[2:8]) # prints llo wo  # space is also counted.
print(b[0:6])  # prints hello
print(b[:6])   # prints hello
# use of negative index
print(b[-2])   # prints l of world
print(b[-3:-1])  # prints rl

#### STRING FORMATING ####
p = 20
q = "Shashwat"
# Below all three gives same output 
r = "My name is {} & my age is {}".format(q, p)
s = "My name is {1} & my age is {0}".format(p, q)   
t = f"My name is {q} & my age is {p}"
print(r)
print(s)
print(t)
k = ["Shashwat", " Playing COD", "20"]
m = f"My name is {k[0]}, my age is {k[2]} & my hobby is{k[1]}"
print(m)

####### LIST #############
print(dir(list))  # will give all methods of list
e = ['red', 'blue', 'green', 'orange', 3, 3.14]
print(e[2])
print(e[-2])
e.pop()  #pops out last element
print(e)
e.remove('orange')
print(e)
e.append(5)  # adds at end
print(e)

######### DICTIONARY ########
#  It defines one-to-one relationship between keys and values.
dict = {'Country':'India','Capital':'Delhi','PM':'Modi', 'Age':50}
print(dict["Country"])
print(dict["Age"])

######### SET ###########
# A set is a collection which is both unordered and unindexed. Hence, Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
thisset = {"apple", "banana", "cherry"}
print(thisset) 

#### BOOLEAN ####
print(1>2)  # False


#### IDENTITY Operator ####
# is
# is not
# They return true or false 

#### MEMBERSHIP Operator ######
##### Unique in Python
# in 
# not in
r = [1,4,7,8,9]
print(3 in r)  # false
print(7 not in r)  # false
# can used for string as well



