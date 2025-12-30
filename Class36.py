'''
================First Class Of Data Analysis====================================
Data Science: A story telling based on Data
ETL : 
IOT : Internet Of Things 
Types Of Data:
Numerical Data ----> Age , Salary, ..........
Categorical Data ====> Gender, City, COuntry ...............
Time Based Data,  ---> Dates, 
Boolen ----> True, False 
'''
#-------------------Numpy--------------------------------#
'''
It builds for Numerical data handling and performing   mathematicl operations
'''
import numpy as np
arr =  np.array([1,2,3,4,5,7.5, True , 'h'])  # it is more memory effeciant then python list and faster then python list Only Stores single type of data at a time (homogenous) becaues Pythone list is (hetirogenous)
print(arr)
np.zeros(5)  # it will create an array of 0's with size 5
np.ones((3))  # it will create an array of 1's with 3 rows and 4 columns
np.arange(1,10,2)  # it will create an array from 1 to 10 with a step of 2
arr = np.array([[1,2,3],[4,5,6]])  # 2D array
print(arr.shape)  # it will give the shape of array (rows, columns)
print(arr.dtype)  # it will give the data type of array elements
print(arr.ndim)   # it will give the number of dimensions
print(arr.size)   # it will give the total number of elements in array
print(arr.reshape(3,2))  # it will reshape the array to 3 rows and 2 columns

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

arr = np.array([2,4,6,8,10,12, 14,16,18,20])
print(np.sqrt(arr))  # it will give the square root of each element
print(np.mean(arr))  # it will give the mean of array elements
print(np.max(arr))   # it will give the maximum element in array
print(np.add(arr, 5))  # it will add 5 to each element in array
print(arr.size) # it will count the number of elements in array