import numpy as np 


def f(x):
    return x**2 + 54/x

def Derivative(x):

    if abs(x) > 0.01:
        delta_x= 0.01*abs(x)
    else:
        delta_x= 0.0001

    return (f(x+delta_x) - f(x-delta_x))/(2*delta_x)
    
    
def bisection():

    a=float(input("Enter the lower bound: "))
    b= float(input("Enter the upper bound: "))
    e=float(input("Enter the minimum error value: "))

    if Derivative(a)< 0 and Derivative(b) > 0:
        x1=a
        x2=b

        while True:
            z=(x1+x2)/2
            if abs(Derivative(z)) < e:
                break

            if Derivative(z) < 0:
                x1 = z
            else:
                x2 = z

        print(f"The minimum point is {z}")
        print(f"Approximate minimum value is {f(z)}")

    else:
        print("Choose different bounds such that the derivative at the bounds have opposite signs")



bisection()