from array import *
##import array 

arr = array('i', [])

#default input is string so we convert it into int
n = int(input("Enter the length of the array"))

for i in range (n):
    x = int(input("Enter the values"))
    arr.append(x)

print(arr)

val = int(input("Enter the number you want to search"))

k = 0
for e in arr:
    if e==val:
        print(k)
        break

    k+=1