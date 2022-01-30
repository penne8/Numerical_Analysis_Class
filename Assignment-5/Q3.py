import numpy as np
from scipy.integrate import quad

# Solve y''-(1-(x/5))y=x

# parameters
goal_func = lambda x: 1 - (x / 5)
y_start = 2.
y_end = -1.
approximation_range = [1., 3.]
num_of_partitions = 5

X = np.linspace(approximation_range[0], approximation_range[1], num_of_partitions)
h = X[1] - X[0]

def n0(x):
    if x >= X[0] and x <= X[1]: return (X[1] - x) / h
    return 0.
def n1(x):
    if x >= X[0] and x <= X[1]: return (x - X[0]) / h
    if x >= X[1] and x <= X[2]: return (X[2] - x) / h
    return 0.
def n2(x):
    if x >= X[1] and x <= X[2]: return (x - X[1]) / h
    if x >= X[2] and x <= X[3]: return (X[3] - x) / h
    return 0.
def n3(x):
    if x >= X[2] and x <= X[3]: return (x - X[2]) / h
    if x >= X[3] and x <= X[4]: return (X[4] - x) / h
    return 0.
def n4(x):
    if x >= X[3] and x <= X[4]: return (x - X[3]) / h
    return 0.

N = [n0, n1, n2, n3, n4]

def n0_prime(x):
    if x >= X[0] and x <= X[1]: return -1/h
    return 0.
def n1_prime(x):
    if x >= X[0] and x <= X[1]: return 1/h
    if x >= X[1] and x <= X[2]: return -1/h
    return 0.
def n2_prime(x):
    if x >= X[1] and x <= X[2]: return 1/h
    if x >= X[2] and x <= X[3]: return -1/h
    return 0.
def n3_prime(x):
    if x >= X[2] and x <= X[3]: return 1/h
    if x >= X[3] and x <= X[4]: return -1/h
    return 0.
def n4_prime(x):
    if x >= X[3] and x <= X[4]: return 1/h
    return 0.

N_prime = [n0_prime, n1_prime, n2_prime, n3_prime, n4_prime]

A = []
for i in range(1, num_of_partitions - 1):
    row_i = []
    for j in range(num_of_partitions):
        func_i_j = lambda x: N_prime[i](x) * N_prime[j](x) + goal_func(x) * N[i](x) * N[j](x)
        integral, *_ = quad(func_i_j, approximation_range[0], approximation_range[1])
        row_i.append(integral)
    A.append(row_i)
A = np.asmatrix(A)
print("\nCoefficient matrix A:")
print(A)

B = []
for i in range(1, num_of_partitions - 1):
    integral, *_ = quad(lambda x: x*N[i](x), approximation_range[0], approximation_range[1])
    B.append(-integral)
B = np.asarray(B)
print("\nDependent variables B:")
print(B)

B[0] = B[0] - (A[0,0] * y_start)
B[-1] = B[-1] - (A[-1,-1] * y_end)

A = A[:, 1:-1]

C = np.linalg.solve(A, B)
C = np.asarray([y_start, *C, y_end])

print("\nC's:")
print(C)
