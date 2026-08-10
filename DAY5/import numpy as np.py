import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = a.reshape(3, 2)
c = a.reshape(6, 1)
d = a.reshape(1, 6)
e = a.flatten()
f = a.transpose()

print("Original array:")
print(a)

print("\nReshape (3,2):")
print(b)

print("\nReshape (6,1):")
print(c)

print("\nReshape (1,6):")
print(d)

print("\nFlatten:")
print(e)

print("\nTranspose:")
print(f)
