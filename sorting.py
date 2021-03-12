######## BUBBLE SORT ############

def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):     # going back(-1) from last to first
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

        print(nums) # if you want to know how the list looks after every iteration

nums = [5, 3, 8, 6, 7, 2]
bubbleSort(nums)

print(nums)

############## SELECTION SORT ##########
# In bubble sort every iteration has multiple swappings(consumes processing power), we don't want that
# Swapping should be done once
# With one iteration we find min or max value and swap only with first or last element

# we take implementation for min value(hence we go from low index to high index)
def selectionSort(nums):
    for i in range(5):
        minpos = i   # variable to hold min position
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j 
        
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)  # if you want to know how the list looks after every iteration

nums = [5, 3, 8, 6, 7, 1]
selectionSort(nums)

print(nums)












