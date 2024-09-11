# Importing the 'array' module to work with arrays.
import array

arr = array.array('i', [1, 2, 3, 4]) # Creating an integer array with initial values [1, 2, 3, 4].
print(arr)                           # Printing the array with values.
arr.insert(4, 6)            # Inserting the integer value 6 at index 4 in the array.
print(arr)                           # Printing the array after inserting the value.
