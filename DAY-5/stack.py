import numpy as  np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Vertical stack
v = np.vstack((a, b))

# Horizontal stack
h = np.hstack((a, b))

print("\nVertical Stack:")
print(v)

print("\nHorizontal Stack:")
print(h)

c=np.concatenate((a,b),axis=0)#ROW WISE axis=0
print("\nConcatenate along axis 0:")
print(c)
d=np.concatenate((a,b),axis=1)#COLUMN WISE axis=1
print("\nConcatenate along axis 1:")
print(d)