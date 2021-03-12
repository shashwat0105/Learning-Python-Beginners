#methods allow us to interract with objects
#methods are like functions with few differences of self & dot notation, when we call a method we use . dot operator

class Computers:
    #__ __ are special methods
    # init automatically gets called
    def __init__(self, cpu, ram):  # self(use to refer to any instance) is a conventional parameter we pass (self, x, y)
        self.cpu = cpu
        self.ram = ram

    def config(self):  #we need to call config to use it
        print("Config is ", self.cpu, self.ram)

comp1=Computers('i5', '16')  # automatically calls init
comp2=Computers('Ryzen3', '8') 

print(type(comp1))

Computers.config(comp1)  # hey human ( computer) walk for us in that Ramesh
comp1.config()  # more used 

#######################################################################################################################
# define a method for coordinate class
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
                    # self use it to refer to any instance
    def distance(self, other):  # other is another parameter to method
        x_diff_self = (self.x - other.x)**2  # dot notation to access data
        y_diff_self = (self.y - other.y)**2
        return (x_diff_self + y_diff_self)**0.5

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
        # in order to print self, we need to add this str method in class Coordinate else it will give error

########################################################################################################################
class Employee:
    no_of_leaves = 8  # Class(static) variable

    def __init__(self, aname, asalary, arole):
        self.name = aname  # instance variable ( because it's inside init) 
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")  # harry is instance object is formed and at the same time init function is called for it. 
#i.e. name, salary & role are variables of harry object

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)

#########################################################################################################################
class Test:
    def __init__(self):  #atleast one argument here self
        self.a=10
        self.b=20
t1=Test()
print(t1.a, t1.b)

#### OR #### multiple arguments
class Test:
    def __init__(self, x, y):  
        self.a=x
        self.b=y
t1=Test(3, 5) # This 3 , 5 passed is received in x & y of init
t2=Test(7, 8)
print(t1.a, t1.b)
print(t2.a, t2.b)

###########################################################################################################################

# INHERITANCE

class A:  #super or parent class
    
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):  # we want this B to have new features along with existing features, so we inherit features of A into B, sub or child class
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B):  # Multi level inheritance
    def feature5(self):
        print("Feature 5 is working")

class D:
    def feature6(self):
        print("Feature 6 is working")

class E(A, D): # Multiple inhertence
    def feature7(self):
        print("Feature 7 is working")

a1 = A()  # a1 is object of class A
a1.feature1()
a1.feature2()
# a1.feauture3() is not possible

b1=B()
b1.feature3()
b1.feature4()
b1.feature1() # coz we can access the features of A in B

c1=C()
c1.feature1() # we can see what all we access as we press . 

e1=E()
e1.feature1() # We can access features of A, D & E offcourse

###################### Constructor in Inheritance ####################################
class A:  
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A): 
    # def __init__(self):
    #     super().__init__()  # will call init of super class i.e. A
    #     print("In B init") 
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1=B() # if u create object of Sub class (here B) it will first try to find init of Sub class(commented right now), 
       #if it is not found there it will call init of Super class
# MRO Method Resolution Order
# class C(A,B):  # The left thing i.e. init of A will called(nainsaafi) this is MRO
#     def __init__(self):
#         super().__init__() # init of super i.e. either of A or B is to be called
#         super().feature1() # we can use super methods to call other methods not just init method
#         print("In C init")

##################### POLYMORPHISM ##########################################
# Poly means Many, Morph means Form, ie many forms
# DUCKTYPING In Python


######## Method Overloading & Overriding ####################################
# Method overloading in C++/ Java i.e. 2 methods having same name
# class Student
#     def average(a, b)
#     def average(a, b, c)    # this such is not in Python

class A:

    def phone(self):
        print("I have Nokia phone")

class B(A):

    def phone(self):
        print("I have motorola phone")  # This motorola now overrides nokia phone

a1=B()
a1.phone()

########################  GENERATOR  ########################
# For ex we are fetching 1000 records & we don't want to store all but only 1 at a time
def topTen():

    yield 6  # a inbuilt function which converts function to generator

values = topTen()

print(values) 
print(values.__next__()) # generator giving iterator

### Dealing errors #### 3 types generally:- Compilation, Logical, Runtime
##### EXCEPTION HANDLING ########
a = 5
b = 0 # test by b = 0

try:
    print("Resource open")
    print(a/b)
except Exception:  # executes only when there is an error
    print("Hey you can't divide by 0")

finally:  # executes whether we get the error or not
    print("Resource Closed") 

























