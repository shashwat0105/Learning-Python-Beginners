#### LINEAR SEARCH #######
pos = -1

def linearSearch(list, n):
    i = 0

    while i<len(list):   # can use for loop
        if list[i] == n:
            globals()['pos'] = i # coz pos is a global variable
            return True
        i = i+1
    
    return False

list = [5,6,7,8,9,10]
n=9

if linearSearch(list, n):
    print("Found at",pos + 1)
else:
    print("Not Found")

####### BINARY SEARCH ############
pos = -1

def binarySearch(list, n):

    l = 0
    r = len(list) - 1

    while l<=r:
        mid = l + ((r-l) // 2)

        if list[mid] == n:
            globals()['pos'] = mid         # instead of pos = mid
            return True
        else:
            if list[mid]< n:
                l = mid + 1
            else:
                r = mid - 1

    return False

list = [4, 7, 8, 45, 60, 90, 100]  # should be sorted
n = 10  

if binarySearch(list, n):
    print("Found at", pos + 1)
else:
    print("Not Found")

















