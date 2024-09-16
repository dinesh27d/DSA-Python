from array import *
arr = array('i', [1,2,3,4,5])

output = arr.tobytes()
print(output)
ints = array('i')
ints.frombytes(output)
print(output)