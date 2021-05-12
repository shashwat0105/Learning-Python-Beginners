from array import array

arr1 = array([2,4,5,3,6])

#copies both values and address
# arr2 = arr1
# #copies values but address becomes different & changing value in one array changes other too.
# #shallow copy
# arr2 = arr1.view()
# #copies values, different address makes independent
# #deep copy
arr2 = arr1.copy()

arr1[1]=7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
