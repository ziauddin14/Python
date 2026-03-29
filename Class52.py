import numpy as np

# Create two 2d arrays

arr1 = np.arange(20).reshape(4,5)
print(arr1)
arr2 = np.arange(20,40).reshape(4,5)
print(arr2)
print(arr1 + arr2)
print(arr1 - 100)

arr3 = np.arange(30,50).reshape(5,4)
# print(arr1 - arr3) # This will give an error because the shapes of the arrays are different

arr1 = np.arange(20).reshape(4,5)
print(arr1[3])  # This will print the element at index 3 (0-based indexing)
print(arr1[-4]) # This will print the element at index -4 (negative indexing)
print(arr1[2, 2:4]) # This will print the elements from index 2 to 3 (inclusive) of the array at index 2
print(arr1[1:3, 1:4]) # This will print the elements from index 1 to 2 (inclusive) and index 1 to 3 (inclusive) of the array
print(arr1[2:3, 2:4]) # This will print the elements from index 2 to 2 (inclusive) and index 2 to 3 (inclusive) of the array
print(arr1[:, :]) # This will print all elements of the array
print(arr1[2:4, 3:5]) # This will print the elements from index 2 to 3 (inclusive) and index 3 to 4 (inclusive) of the array

arr4 = np.arange(64).reshape(8,8)
'''
#print [
    35,36,37,38
    43,44,45,46
    51,52,53,54
]
'''
print(arr4[4:8, 3:7]) # This will print the elements from index 4 to 7 (inclusive) and index 3 to 6 (inclusive) of the array
print(arr4[4, :]) # This will print the elements at index 4 of the array
print(arr4[4]) # This will print the elements at index 4 of the array (same as above)
print(arr4[:, 6]) # This will print the elements at index 6 of the array in horizontally
print(arr4[:, 6:7]) # This will print the elements at index 6 of the array in vertically
print(arr4[::2]) # This will print every second row of the array
print(arr4[::-1]) # This will print the array in reverse order (every row in reverse order)
print(arr4[5,4]) # This will print the element at index 5 and index 4 of the array
print(arr4[5:6, 4:5]) # This will print the element at index 5 and index 4 of the array in a 2d format

x = np.array(range(20))
#Slice the elemnt who multiply by 5
print(x[x % 5 == 0]) # This will print the elements of the array that are multiples of 5
print(x[x%2 != 0]) # This will print the elements of the array that are not multiples of 2
print(x[(x > 5) & (x < 15)]) # This will print the elements of the array that are greater than 5 and less than 15

'''
Transpose of a matrix is obtained by swapping its rows with its columns.
In NumPy, you can easily transpose a matrix using the .T attribute or the np.transpose() function.
'''
arr5 = np.arange(12).reshape(3,4)
print(arr5)
print(arr5.T)  # This will print the transpose of the array


from PIL import Image

img = Image.open('png.png')
print(f'Image Size: {img.size}, Mode: {img.mode}, Format: {img.format}') # This will print the size of the image (width, height) and mode
img_array = np.asarray(img)
print(img_array)
print(f'Number of dimensions: {img_array.ndim}') # This will print the number of dimensions of the array
pilimage = Image.fromarray(img_array)
pilimage.save('new_image.png') # This will save the array as a new image file

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
print(np.maximum(x, y)) # This will return the element-wise maximum of the two arrays
print(np.minimum(x, y)) # This will return the element-wise minimum of the two arrays



# Revision is countinue