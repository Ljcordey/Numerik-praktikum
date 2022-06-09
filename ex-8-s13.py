# implicit method, a), b)

# %%
from math import exp
import numpy as np
import matplotlib.pyplot as plt

def euler_explicit(x0, y0, h, f,z):
    x = [0.] # by def, x>0
    y = [y0]
    
    while x[-1] < z:

        y.append((y[-1]+h*(f(x[-1], y[-1]))))
        x.append(x[-1]+h)

    return np.array(x), np.array(y)

def f(x,y):
    return np.dot(([0,1],[-2*(2*x**2+1),-4*x]),y)

def fe(x): #exact solution
    return([(1-x)*exp(-x**2)],[(2*x**2-2*x-1)*exp(-x**2)])


def err0r(yi,fex,X,h):
    index = int(np.round(X/h)) #I want to know at which element x+h  I need to compare w
    err = yi[index]-fex(X)
    return np.linalg.norm(err,2) #norm-2 is chosen here because it is the implied standard norm


h = [0.1,0.05,0.025]
X = [1.2,3]
y_0 =[1,-1]
stop = 30

for hi in h: 
    x,y = euler_explicit(0,y_0,hi,f,stop)
    for xi in X:

        #print(fe(xi))
        print('for N =',np.round(xi/hi),' ,X = ',xi,' the value of the error is = ',err0r(y,fe,xi,hi))


# %%

x,y =euler_explicit(0,y_0,0.1,f,stop)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x,y, color='blue')
plt.xlim([0,30])
plt.ylim([-2,2])
# %%
