import numpy as np
from numpy.linalg import norm
from scipy.linalg import lu, solve_triangular

#def
L1 = 2
L2 = 1

# def des positions pour le calcul
x = 3
y = 0

def g(THETA):

    # extracting x,y values from the array
    theta1 = THETA[0]
    theta2 = THETA[1]

    return np.array([L1*np.cos(theta1)+L2*np.cos(theta1+theta2)-x, 
                    L1*np.sin(theta1)+L2*np.sin(theta1+theta2)-y])


# jacobi matrix definition for g(X)
def dg(THETA):

    # extracting x,y values from the array
    theta1 = THETA[0]
    theta2 = THETA[1] 

    return np.array([-L1*np.sin(theta1)-L2*np.sin(theta1+theta2), -L2*np.sin(theta1+theta2)],
                    [L1*np.cos(theta1)-L2*np.cos(theta1+theta2), L2*np.cos(theta1+theta2)])


# initialisation

tol = 1e-14 # Abbruchtoleranz
N = 30      # max. Iterationen
n = 0       # Iterationsschritt

x = np.array([0.5,0.5]) # Startwert
xN = [np.array(x)]  

res = norm(g(x),np.inf)

while (res > tol) and (n < N):
    n +=1

    # Lineares System lösen
    A = dg(x)
    b = g(x)
    P,L,R = lu(A)  # oder mit QR
    z = solve_triangular(L,P.T@b, lower = True)
    delta = solve_triangular(R,z)

    # Update x
    x -= delta
    res = norm(G(x),np.inf)
    xN.append(np.array(x)) # Kopie speichern!
    print(n,x,res)
xN = np.array(xN)