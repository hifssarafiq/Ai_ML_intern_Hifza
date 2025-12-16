# Importing NumPy library
import numpy as np 
# 1. Array Creation
print("1. Array Creation")
arr1 = np.array([1, 2, 3, 4, 5])                 
arr2 = np.array([[1, 2, 3], [4, 5, 6]])           
arr3 = np.zeros((2, 3))                            
arr4 = np.ones((3, 2))                             
arr5 = np.arange(0, 10, 2)                        
arr6 = np.linspace(0, 1, 5)                        
print("1D array:", arr1)
print("2D array:\n", arr2)
print("Zeros:\n", arr3)
print("Ones:\n", arr4)
print("Arange:", arr5)
print("Linspace:", arr6)
print("-"*50)
# 2. Array Indexing and Slicing
print("2. Array Indexing and Slicing")
print("Original arr1:", arr1)
print("Indexing arr1[2]:", arr1[2])
print("Slicing arr1[1:4]:", arr1[1:4])
print("2D array element arr2[1,2]:", arr2[1,2])
print("2D array row arr2[0,:]:", arr2[0,:])
print("2D array column arr2[:,1]:", arr2[:,1])
print("-"*50)
# 3. Vectorized Mathematical Operations
print("3. Vectorized Mathematical Operations")
arr = np.array([1,2,3,4,5])
print("Original array:", arr)
print("Add 5:", arr + 5)
print("Square:", arr**2)
print("Multiply by 2:", arr * 2)
print("Sine values:", np.sin(arr))
print("-"*50)
# 4. Aggregation / Summary Statistics
print("4. Aggregation / Summary Statistics")
arr = np.array([1,2,3,4,5])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Cumulative Sum:", np.cumsum(arr))
print("-"*50)
# 5. Reshaping Arrays
print("5. Reshaping Arrays")
arr = np.arange(12)
print("Original 1D array:", arr)
arr_reshaped = arr.reshape((3,4))  # 3 rows, 4 columns
print("Reshaped to 3x4:\n", arr_reshaped)
print("-"*50)
# 6. Matrix Operations
print("6. Matrix Operations")
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition:\n", A + B)
print("Matrix Multiplication:\n", A @ B)    # or np.dot(A,B)
print("Element-wise Multiplication:\n", A * B)
print("Transpose of A:\n", A.T)
print("-"*50)
# 7. Broadcasting
print("7. Broadcasting")
arr = np.array([[1,2,3],[4,5,6]])
print("Original array:\n", arr)
arr_added = arr + 10        # Add scalar to each element
print("After broadcasting +10:\n", arr_added)
row_vector = np.array([1,0,1])
arr_added2 = arr + row_vector  # Broadcast row vector
print("After broadcasting row vector:\n", arr_added2)
print("-"*50)
# 8. Random Number Generation
print("8. Random Number Generation")
np.random.seed(42)           # Set seed for reproducibility
rand_arr = np.random.rand(3,3)      # 3x3 array with random floats between 0 and 1
rand_int = np.random.randint(0, 10, (2,4))   # 2x4 array with random integers between 0 and 9
print("Random float array:\n", rand_arr)
print("Random integer array:\n", rand_int)

