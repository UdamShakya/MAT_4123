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


#exhaustive_Search(0.00001,5,10)

#bounding phase 

def bounding_phase() :
     
    x0= float(input("enter the number you need to start the iteration from "))
    delta = float(input("enter the increment value"))
    k= 0
    x_prev=x0
    x_k= x0
    


    f1 = function(x0-delta)
    f2 = function(x0)

    if f1>= f2 and function(x0)>= function(x0+ delta):
        delta = +1 * delta
    elif function(x0-delta) <= function(x0) and function(x0) <= function(x0+ delta):
        delta = -1 * delta 
    else:
        print("choose a different starting point and increment")
        x0= float(input("Enter the new number you need to start the iteration from "))
        delta = float(input("enter the new increment value"))


    x_next = x_k + (2**k)*delta

    while function(x_next) <= function(x_k):
        k = k+1
        x_prev = x_k
        x_k = x_next
        x_next = x_k + (2**k)*delta

    print(f"Minimum point lies in ({x_prev},{x_next})")

bounding_phase()

# Region elimination method 




    





