#Golden Section Method
#for Minimization

import math

def function(x):
    return x**2 +54/x

def golden_section():

    a=float(input("Enter the lower bound: "))
    b=float(input("Enter the upper bound: "))
    epsilon =float(input("Enter the minimum error value: "))
    golden_ratio = 0.618

    x1 = a + golden_ratio*(b-a)
    x2 = b - golden_ratio*(b-a)

    while abs(b-a) > epsilon:
        if function(x1) > function(x2):
            b = x1
        else:
            a = x2
        x1 = a + golden_ratio * (b - a)
        x2 = b - golden_ratio * (b - a)
    print(f'The minimum point is in between ({a},{b})')

golden_section()