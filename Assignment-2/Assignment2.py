import matplotlib.pyplot as plt

def f(x):
    return x**2-0.2*x-3

def bisection_method(f, a, b, eps):
    iter = 0
    while(True):
        iter += 1
        z = (a + b) / 2
        if f(z) == 0 :
            return z, iter
        else:
            if f(a)*f(z) < 0 :
                b = z
            else:
                a = z
        if(abs(b-a) < 2*eps):
            break
    return ((a + b) / 2), iter

def regular_falsi(f, a, b, delta, real):
    prev2 = a
    prev1 = b
    iter = 0
    while (True):
        iter += 1
        curr = prev1 - f(prev1) * ((prev1-prev2)/(f(prev1)-f(prev2)))
        if f(curr) == 0:
            return curr, iter
        else:
            if f(curr)*f(prev1) < 0:
                prev2 = curr
            else:
                prev1 = curr
        if(abs(curr-real) < delta):
            break
    return curr, iter

def main():
    a = -1
    b = 4
    eps = 10**-8

    bm_true, bm_iter = bisection_method(f, a, b, eps)

    #a
    print(f"bisection true method result for x is {bm_true} in {bm_iter} iterations\n")

    x_axis = []
    y1_axis = []
    y2_axis = []

    #b
    for d in range(-1,-6, -1):
        x_axis.append(d)
        eps = 10**d
        bm_approx, bm_iter = bisection_method(f, a, b, eps)
        y1_axis.append(bm_iter)
        rf_approx, rf_iter = regular_falsi(f, a, b, eps, bm_true)
        y2_axis.append(rf_iter)
        print(f"for d = {d}:")
        print(f"bisection method result for x is {bm_approx} in {bm_iter} iterations")
        print(f"regular falsi result for x is {rf_approx} in {rf_iter} iterations")


    plt.plot(x_axis, y1_axis, color='red', marker="o", label='Bisection Method')
    plt.plot(x_axis, y2_axis, color='green', marker="o", label = 'Regula Falsi')
    plt.xlabel("d")
    plt.ylabel("iterations")
    plt.title(f"BM and RF methods iterations per d comparison")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()