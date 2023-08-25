import numpy as np
import matplotlib.pyplot as plt

epsilon=1

while 1 + epsilon !=1:
    epsilon*=0.5
    
print(epsilon)

def epsilon(x):
    return np.sin(x) - (x-x**3/6)

x= 3*np.pi/4
print(epsilon(x)/epsilon(x/2))

def function(x):
    return np.sin(x)

def ExactDerivate(x):
    return np.cos(x)

N=50
x=np.linspace(0,2*np.pi,N)
print(x)
y= function(x)
plt.scatter(x,y)

plt.show()


def DerivadaDerecha(f, x, h):
    d= 0.
    if h !=0:
        d= (f(x+h)-f(x))/h
    return d

RDerivate= DerivadaDerecha(function, x, h)
plt.plox(x, ExactDerivate, label="Exacta")