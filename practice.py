def function(x):
    return x**2 +(54/x)

def exhaustive_search(a,b,step):
    # a= float(input("Enter the lower bound: "))
    # b= float(input("Enter the upper bound: "))
    # step= float(input("Enter the step size: "))
    delta= (b-a)/step
    x1= a
    x2= x1 + delta
    x3 =x2 + delta
    while x3 <= b:
        if function(x1) >= function(x2) and function(x2) <= function(x3):
            print(f"the minimum lies between {x1} and {x3}")
            return
        
        x1= x2
        x2= x3
        x3= x3 + delta

    print(f"no minimum between {a} and {b} with step size {step}")

exhaustive_search(0.00001,5,10)


def bounding_phase(x_0, delta):
    k=0
    x_prev=x_0
    x_k=x_0

    f1= function(x_0- delta)
    f2= function(x_0)
    f3= function(x_0+ delta)

    if f1 >= f2 and f2 >= f3:
        delta=+delta
    elif f1<= f2 and f2 <= f3:
        delta=-delta
    else: 
        print("choose a different initial guess")
        return 
    
    x_next= x_k + (2**k)*delta

    while function(x_k) >= function(x_next):
        k += 1
        x_prev = x_k
        x_k = x_next
        x_next = x_k + (2**k)*delta

    print(f"Minimum lies between ({x_prev}, {x_next})")

bounding_phase(0.6, 0.5)

def interval_halving(a,b,eps):
    xm = (a+b)/2
    L=b-a

    while abs(L) >= eps:
        x1=(xm+a)/2
        x2=(xm+b)/2
        if function(x1) < function(xm):
            b=xm
            xm=x1
        elif function(x2) < function(xm):
            a=x1
            xm=x2
        else:
             a=x1
             b=x2
        
        L=b-a

    print(f"Minimum lies between ({a}, {b})")

interval_halving(0.00001,5,0.001)