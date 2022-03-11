#!/usr/bin/env python
# coding: utf-8

# In[1]:


## NUMERICAL PYTHON (NUMPY)
# It is used for working with numerical data in python
# It makes computation easier and faster
# Consumes less memory

## Array in NumPy?
# Like list in Python an array is a data structure in NumPy.
# An Array in NumPy can hold collection of ordered elements
# An array in NumPy can hold data of same type


# In[2]:


import numpy as np
python_list = [3, 49, 3, 29, 10, 8]
numpy_array1 = np.array (python_list)
print (numpy_array1)
#Display Numpy array

print (python_list)
#Display python list

list_x = list(range (1000000))
list_y = list(range (1000000))

numpy_arr_x = np.array (list_x)
numpy_arr_y = np.array (list_y)

z = numpy_arr_x + numpy_arr_y
print (z)


# In[3]:


a = [[2, 3, 1], [9, 0, 0], [3, 38, 20], [18, 47, 5]]
arr = np.array(a)
arr.size
#This displays the number of elements in the array
arr.dtype
# Data type (integer, string, float)
arr.shape
# shape of the array (row, colum). The number of rows and columns in the array
arr.ndim
# dimension of the array
type(arr)
# identifies the type of object. Is it numpy, list, tuple, range, boaleans etc.?
np.arange(10)
# a range of numbers from 0 to 9
np.zeros(4)
# a range of zeros. The quantity of zero that is displayed depends on the number in the bracket
np.ones (5)
# a range of ones. The quantity of zero that is displayed depends on the number in the bracket
t = np.full (shape = (2,3), fill_value = 3)
# Displays an array with the specified shape "(2,3)"and fills it with the specified value "(3)"
np.linspace(start = 1, stop = 10, num = 5)
#It divides the numbers from start to stop into num parts. If no num argument is given, then it takes 50 automatically.
np.linspace (2, 9, 4)
# Another method of writing linspace. Writing start, stop and num is not necessary.
np.append (arr, [43, 2, 9])
#Adding an element or list[43, 2, 9] .
np.delete(arr, 3)
#Deletes the 4th element.
np.sort(arr)
#sorts the array in ascending order. Sorts each row in ascending order from left to right.
np.reshape (arr, (3, 4))
# This reshapes the array.
arr.reshape (2,3,2)
# Another method of reshaping an array. In this method, I reshaped the array into a 3 dimension array.
arr.flatten ()
# This flattens the array into a one dimensional array no matter the dimension of the array.
arr[2][0]
# Array Indexing and slicing
arr [2, 0:3]
# Another method of Array Indexing and slicing
arr [-2, -1]
# Negative Indexing
arr[0:5:2]
# Array striding. (start:0, stop:5, stride:2). This is the steps to jump
arr.mean(axis=1)
# Mean of each row
arr.mean(axis=0)
# Mean of each column


# In[4]:


test_1 = np.array ([True, False, False, True])
test_2 = np.array ([False, True, False, True])

test_3 = np.array([[3,2], [4,5]])
test_4 = np.array([[3,3],[8,5]])

np.logical_or(test_1, test_2)
# If there exists "True" in either array, it displays True. if not it displays False
np.logical_and(test_1, test_2)
# If there exist "True" in both arrays, it displays True. if not it displays False
np.logical_not(test_1)
# If the array doesn't have "True" (which means it has "False") then "True" is displayed, if not "False" is displayed.

np.equal(test_3, test_4)
# The elements of test_3 array that equals the corresponding element of test_4 array displays "True", if not "False" displays.
np.less (test_3, test_4)
# the elements of test_3 array that are less than test_4 displays "True", otherwise "False" is shown
np.less_equal(test_3, test_4)
# the elements of test_3 array that are less than or equal to test_4 displays "True", otherwise "False" is shown
np.greater (test_3, test_4)
# the elements of test_3 array that are greater than test_4 displays "True", otherwise "False" is shown
np.greater_equal (test_3, test_4)
# the elements of test_3 array that are greater than or equal test_4 displays "True", otherwise "False" is shown
np.array_equal (test_3, test_4)
# Compares the entire array
np.vstack((test_1, test_2))
# Stacks array in a vertical format
np.hstack((test_1, test_2))
# Stacks array in a horizontal format
np.column_stack((test_1, test_2))
# Stacks array column-wise. This is also the transpose of the vertical format array.
np.c_[test_4]
# Another method of stacking arrays column-wise. Note: Do not misplace the () for [].
np.transpose(test_3)
# Transposes the array
test_4.T
# Another method of Transposing an array


# In[5]:


a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])) 
b = np.max(a, axis=0).sum() 
print (b)


# In[6]:


original = np.random.randint(1,200, size = (3, 28,28) )
flat = original.reshape(1,3,28,28)
#Reshaping the matrix to a 1 x (3 x 28 x 28) matrix
print(flat.flatten().ndim)
print (flat.flatten().shape)
print (original.shape)
print (flat.shape)
print (original.data)
print(flat.data)
print (flat.flatten().data)
print (original.dtype)
print (flat.dtype)
print (flat.flatten().dtype)
first_10 = original [1][1][0:10]
# The first 10 elements of the second row of the second matrix
original [2].shape
#The shape of the third matrix
first_3 =original[2][0:3]
#The first 3 rows


# In[7]:


first_50 = np.arange(2, 102, 2)
p = first_50.reshape(10,5)
row_means = p.mean(axis=1)
print (row_means)
print (p)


# In[ ]:




