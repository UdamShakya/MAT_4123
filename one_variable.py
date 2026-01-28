import numpy as np
import scipy as sp

def function(x):
    return x**2 + 54/x


def exhaustive_Search(a,b,n):
    delta = (b-a)/n
    x1 = a 
    x2 = x1+delta
    x3 = x2+delta


    while x3 <= b:
        if function (x1) >=function(x2) and function(x2)<= function(x3):
            print(f"minimum function lies in  ({x1},{x3})")
            return 
        
        x1 =x2
        x2 = x3

        x3 =x2+delta

    print(f"no minimum inside({a},{b}); boundary point maybe a minimum ")




exhaustive_Search(0.00001,5,10)





