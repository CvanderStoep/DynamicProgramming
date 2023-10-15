import numpy as np

# print(np.__version__)

# a = np.array([1, 2, 3, 4, 5, 6, 7])
# a = np.arange(1, 7)
# b = a.reshape((2, 3))
# print(a)
# print(a.shape)
# print(b)
# print(b.shape)
# even = np.argwhere(a % 2 == 0).flatten()
# print(even)

A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])
x = np.linalg.inv(A).dot(b)
print(x)

x = np.linalg.solve(A, b)
print(x)
