import numpy as np

A = np.array([[5,-1,7],[-1,-1,1],[7,1,5]])
x = np.array([1.,1.,1.])
for i in range(9):
    x = A @ x
    l = np.amax(x)
    x = 1./l * x

print(f"The returned eigenvalue is: {l}, and the eigenvector is: {x}")

print(f"The max real eigen value is: {np.max(np.linalg.eig(A)[0])}")

The returned eigenvalue is: 11.999954223865643, and the eigenvector is: [ 9.99997457e-01 -1.27156414e-06  1.00000000e+00]
The max real eigen value is: 12.000000000000004
