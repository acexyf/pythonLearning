import numpy as np

arr0 = np.array([[1,2,3]])

arr1 = np.array([[1],[2],[3]])


arr2 = np.transpose([[2,3,1]])

# print(arr2)


A = np.array([[2,1,-2], [3,0,1], [1,1,-1]])
b = np.transpose([[-3,5,-2]])


x = np.linalg.solve(A,b)

print(x)