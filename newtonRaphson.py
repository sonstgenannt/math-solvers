from decimal import *
getcontext().prec = 24
from math import *

# function f from which roots are discovered
def f(x):
    return cos(x) - cosh(x) + 1
# derivative of function f with respect to x
def f_x(x):
    return -sin(x) - sinh(x)

# Newton-Raphson root finding iterative root finder
def nR(f, f_x, x_0, n):
    x_n = [x_0]
    for i in range(n):
        x_n.append(Decimal(x_n[-1]) - Decimal(f(x_n[-1])/f_x(x_n[-1])))
    return x_n

x_0 = Decimal(-1)   # initial approximation
n = 20  #   amount of iterations used
x_approximations = nR(f, f_x, x_0, n)
print(f"{n} iterations from {x_0}: {x_approximations[-1]}")
print(f"f_x({x_approximations[-1]}) =", Decimal(f_x(x_approximations[-1])))
