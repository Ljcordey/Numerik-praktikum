import numpy as np
import matplotlib.pyplot as plt
A = np.matrix([[6, -4], [2, -3]])
# 1 Norm
x = np.matrix([[0, 1, 0, -1, 0], [1, 0, -1, 0, 1]]) # Eckpunkte
y = A@x
plt.figure(1)
plt.plot(x[0].A1, x[1].A1)
plt.plot(y[0].A1, y[1].A1)
# 2 Norm
a = np.linspace(0, 2*np.pi, 100)
x = np.matrix([np.cos(a),np.sin(a)])
y = A @ x;
plt.figure(2)
plt.plot(x[0].A1, x[1].A1)
plt.plot(y[0].A1, y[1].A1)
# inf norm
x = np.matrix([[1, 1, -1, -1, 1],[1, -1, -1, 1, 1]]) # Eckpunkte
y = A@x
plt.figure(3)
plt.plot(x[0].A1, x[1].A1)
plt.plot(y[0].A1, y[1].A1)