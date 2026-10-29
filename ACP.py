
import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# 1. Addition
print("Addition:", arr + 5)

# 2. Subtraction
print("Subtraction:", arr - 5)

# 3. Multiplication
print("Multiplication:", arr * 2)

# 4. Division
print("Division:", arr / 2)

# 5. Find the sum
print("Sum of elements:", np.sum(arr))

# 6. Find the maximum and minimum
print("Maximum element:", np.max(arr))
print("Minimum element:", np.min(arr))

# 7. Find the mean
print("Mean:", np.mean(arr))

# 8. Sort the array
arr2 = np.array([40, 10, 50, 20, 30])
print("Sorted Array:", np.sort(arr2))

# 9. Access an element
print("First element:", arr[0])

# 10. Slice the array
print("First three elements:", arr[:3])

# 11. Reshape the array
arr3 = np.array([1, 2, 3, 4, 5, 6])
print("Reshaped Array:\n", arr3.reshape(2, 3))

# 12. Find the number of elements
print("Number of elements:", arr.size)
