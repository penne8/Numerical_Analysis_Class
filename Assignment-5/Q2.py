import math

# params
h = 0.1
lam = 2. / 3.
alpha2 = (1. / (2. * lam))
alpha1 = 1. - alpha2
iter = 10


def exact_res(x):
    return 2 * math.pow(math.e, x) - x - 1

print("-----------------------TASK2:A-----------------------")
x = 0.
for i in range(1, iter + 1):
    x = round(x + h, 2)
    print(f"Exact: x_{i} = {x},      y_{i} = {exact_res(x)}")
print("\n-----------------------TASK2:B-----------------------")

def f(x, y):
    return x + y


# Euler Method
def calc_EM_next_y(x, y, h):
    return y + h * f(x, y)


x = 0.
y_EM = 1.
for i in range(1, iter + 1):
    y_EM = calc_EM_next_y(x, y_EM, h)
    x = round(x + h, 2)
    print(f"EM: x_{i} = {x},      y_{i} = {y_EM}")
print("---------------------------------------------------")

# Runge-Kutta
def calc_RK2_next_y(x, y, h):
    k1 = f(x, y)
    k2 = f(x + lam * h, y + lam * h * k1)
    return y + h * (alpha1 * k1 + alpha2 * k2)

x = 0.
y_RK2 = 1.
for i in range(1, iter + 1):
    y_RK2 = calc_RK2_next_y(x, y_RK2, h)
    x = round(x + h, 2)
    print(f"RK2: x_{i} = {x},     y_{i} = {y_RK2}")

print("\n-----------------------TASK2:E-----------------------")
x = 0.
y_EM = 1.
y_RK2 = 1.
h_EM = 0.05
h_RK2 = 0.1
for i in range(1, iter + 1):
    y_EM = calc_EM_next_y(x, y_EM, h_EM)
    y_EM = calc_EM_next_y(round(x + h_EM), y_EM, h_EM)
    y_RK2 = calc_RK2_next_y(x, y_RK2, h_RK2)
    print(f"-- For x_{i} = {round(x + h_RK2, 2)}:")
    print(f"EM:    y_{i} = {y_EM}")
    print(f"RK2:   y_{i} = {y_RK2}")
    x = round(x + h_RK2, 2)
    y_exact = exact_res(x)
    print(f"EM  error is: {abs(y_exact - y_EM)}")
    print(f"RK2 error is: {abs(y_exact - y_RK2)}\n")
print("---------------------------------------------------")