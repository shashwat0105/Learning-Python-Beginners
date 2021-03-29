### MULTITHREADING ####
from time import sleep
from threading import *
class Hello(Thread): # Inside thread class we have a method called run
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1) # we give a gap of 1 second

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello() # t1 thread prints Hello
t2 = Hi()   # t2 thread prints Hi
t1.start()  
sleep(0.2)   # to avoid some collisions that occur even in giving a gap of 1 sec
t2.start()

t1.join()  # asks main thread to wait for t1 else the main thread will interupt and print in between
t2.join()  # asks main thread to wait for t2
print("Bye") # Our main thread prints Bye
# We wanted one Hi, One Hello ,, something is happening in parallel but not as we wanted
# Our system is so fast that it executing them at the same point
# We cure this by importing time
# You can adjust values 5 & 500 to see differences


############## FILE HANDLING ####################################
# reading a file
f = open('function.py', 'r') # r is your intension i.e. you are opening this file for reading
# when we handle a file we save somewhere so we say it as f
print(f.read()) # prints everything inside function file
print(f.readline()) # prints only the first line
print(f.readline()) # pointer moves to 2nd line and prints it

# writing in a file
f1 = open('abc.py', 'w') # there was not any file abc.py as we press run, it created a abc.py file
f1.write("Writing first") # the abc files gets this data inserted from here 

f1 = open('abc.py', 'a')
f1.write("Trying to append something")

for data in f:
    f1.write(data)


###### Date & Time in Python
import datetime as dt 

x = dt.datetime.now()
print(x)  # prints complete time
print(x.year) # prints year
# gooogle date formatting methods in pyhton.
# strf time()  string formatting time







