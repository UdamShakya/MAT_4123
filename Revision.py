import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def objective(x):

    x1= x[0]
    x2= x[1]
    return -(-x1**2-5*x2**2+4*x1*x2+4*x2+10*x2)

def constraint1(x):

    x1 = x[0]
    x2 = x[1]
    return x1+x2 -5 

def constraint2(x):
    x1 = x[0]
    x2 = x[1]
    return 4*x1 +x2-18 

def non_linear_constraint(x):
    x1 = x[0]
    x2 = x[1]
    return x1**2 + x2**2 - 1

x0=[0,0]
b=(0,None)

bounds=[b,b]

con1= {'type': 'ineq', 'fun': constraint1}
con2= {'type': 'ineq', 'fun': constraint2}
con3= {'type': 'ineq', 'fun': non_linear_constraint}

cons =[con1, con2, con3]

solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)

print('Optimal value of x1 and x2:', solution.x)

