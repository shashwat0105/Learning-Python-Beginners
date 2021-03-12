
def greet():
    print("Hello Noob Coders")
    print("Good morning")

greet()

def add(x,y):
    c=x+y
    print(c)

add(4,5)
#or
def add1(w,v):
    d=w+v
    return d

result=add(4,5)
print(result)

def person(name, **data): #keyword along with variable length

    print(name)

    for i,j in data.items():
        print(i,j)

person('Shashwat', age=20, city='Banda', Mob=96289)

#factorial using recursion
def fact(n):

    if n==0:
        return 1

    return n*fact(n-1)

result = fact(5)
print(result)

f = lambda a,b: a+b

result=f(4,5)

print(result)

nums=[1,2,3,4,5,6,7,9]

evenss=list(filter(lambda n: n%2==0, nums)) #filter is an inbuilt function

print(evenss)


# The Map function
#can take user defined or lambda function as a parameter
output = map(lambda x: x+3, [1,2,3,4])  #add 3 to each of the iterable present in this list


#Filter function
#filter(function, iterables)
def new1(i):
    if i>=3:
        return i
j = filter(new1, (1,2,3,4,5,6,7))
print(j)
print(tuple(j))
print(list(j))

z = filter(lambda x:(x>=3), (1,2,3,4,5,6,7))
print(list(z))


#Reduce function
#reduce(function, iterables)
#we need to import reduce 
from functools import reduce
output = reduce(lambda x,y: x+y, [1,2,3,4,5,6])

#filter() within map()
c = map(lambda x:x+x, filter(lambda x:(x>=4), [1,2,3,4,5,6,7]))  # x+x every number will be doubled
print(tuple(c))
# The output of filter function will be the input of map function
#Output (8, 10, 12, 14)

#map() within filter()
c = filter(lambda x:x+x, map(lambda x:(x>=4), [1,2,3,4,5,6,7]))
print(tuple(c))
#Output (4,6,10,12,14)

#map() & filter() within reduce()
r = reduce(lambda x,y:x+y, map(lambda x: x+x, filter(lambda x:(x<=4), [1,2,3,4,5,6,7,8,9])))
print(r) #numbers less than equal to 4 are filterede are passed to map then gets doubled and all the numbers get added0

def div(a,b):
    if a<b:
        a,b=b,a #swapping

    print(a/b)

div(2,4) 

 # Using decorators(adds extra features to the existing function)
def div(a,b):
   
    print(a/b)

def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

div1 = smart_div(div)

div1(2,4) 






