from array import *
arr = array('i', [1,2,3,4,5])
print(arr)

arr.extend([10,11])
print(arr)
# OR

arr1 = array('i', [27,28,29])
arr.extend(arr1)

print(arr)