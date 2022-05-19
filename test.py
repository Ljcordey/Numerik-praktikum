import numpy as np
from matplotlib import pyplot as plt
import constants as cst


# delta's discretisation
delta_t = 0.5
delta_r = 0.001
n = 4

def t_i(i):
    return i*delta_t

def r_j(j):
    return j*delta_r

print(cst.size_rhor)



#Dichte nach Radius
def rho(r):

    #dichte;

    if(r>= 0.0 or r <= 0.025):
        dichte = cst.WASSER[0]

    if((r>= 0.025 or r <= 0.030) or (r>= 0.055 or r<=0.060) ):
        dichte =cst.STAHL[0]

    if(r>= 0.030 or r <= 0.055):
        dichte = cst.GLASSWOLLE[0]

    return dichte

# Wärmekapazität nach Radius
def c_p(r):

    #cap;

    if(r>= 0.0 or r <= 0.025):
        cap = cst.WASSER[1]

    if((r>= 0.025 or r <= 0.030) or (r>= 0.055 or r<=0.060)):
        cap = cst.STAHL[1]

    if(r>= 0.030 or r <= 0.055):
        cap = cst.GLASSWOLLE[1]

    return cap


#Wärmeleitungskonstante nach Radius
def Lambda(r):

    #lam;

    if(r>= 0.0 or r <= 0.025):
        lam = cst.WASSER[2]

    if((r>= 0.025 or r <= 0.030) or (r>= 0.055 or r<=0.060) ):
        lam = cst.STAHL[2]

    if(r>= 0.030 or r <= 0.055):
        lam = cst.GLASSWOLLE[2]

    return lam



Gt=20
n = int(cst.size_rhor/delta_r)
time =int(1000 / delta_t)

print(n)
print(cst.size_rhor)
print(delta_r)

# explicit
T = np.zeros([time+1, n+1])
T[0, :] = 0
T[0, n] = Gt

print(T[0, :])

for i in range(0, time):


    for j in range(1,n):

        k_j = Lambda(j) / (c_p(j)*rho(j))
        u_j = (delta_t*k_j) / r_j(j)

        A = T[i][j-1]
        B = T[i][j]
        C = T[i][j+1]
    
        T[i+1][j] = u_j*r_j(j)/(delta_r**2)*A + (1-u_j*(1/delta_r + 2*r_j(j)/delta_r**2))*B + u_j*(1/delta_r + r_j(j)/delta_r**2)*C

    T[i+1, 0] = T[i+1, 1]  
    T[i+1, n] = Gt
    


# Graphische Darstellung
x = np.array(range(n+1))*delta_r
t = np.array(range(time+1))*delta_t

xA, tA = np.meshgrid(x, t)
print(tA.shape, xA.shape)

# Plot the surface.
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, num=1)
surf = ax.plot_surface(xA, tA, T)


