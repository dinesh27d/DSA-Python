# Importing the 'array' module to work with arrays.
import array

my_array = array.array('i')                # Creating an empty integer array using 'array' module.
print(my_array)                            # Printing the empty array.
my_array1 = array.array('i', [1, 2, 3, 4]) # Creating an integer array with initial values [1, 2, 3, 4].
print(my_array1)                           # Printing the array with values.


# Importing the 'numpy' library to work with arrays.
import numpy as np
np_array = np.array([], dtype=int) # Creating an empty numpy array with integer data type.
print(np_array)                           # Printing the empty numpy array.
np_array1 = np.array([1, 2, 3, 4])        # Creating a numpy array with initial values [1, 2, 3, 4].
print(np_array1)                          # Printing the numpy array with values.

