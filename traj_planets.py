import matplotlib.pyplot as plt
import numpy as np

g = 9.8
delta = 0.001
T = 20
N = int(T/delta)
x = [[0]*(N-1) for in range(Q)]
vx = [0]*N
ax = [0]*N
y = [0]*(N-1)
vy = [0]*N
ay = [0]*N
r = [0]*N
k = 7
x[0] = 0.5
y[0] = 0.0
vx[0] = 0.0
vy[0] = 9

r[0] = (x[0]**2+y[0]**2)**0.5
print('r0=', r[0])
ax[0] = -x[0]/(r[0])**3
ay[0] = -y[0]/(r[0])**3
print('accelertions', ax[0], ' ', ay[0])
vx[1] = vx[0] + (delta/2)*ax[0]
vy[1] = vy[0] + (delta/2)*ay[0]
print('velocities', vx[1], ' ', vy[1])
t = np.arange(0, T, delta)
for n in range(1, N-1):
    x[n] = round((x[n-1] + delta*vx[n]), k)
    y[n] = round((y[n-1] + delta*vy[n]), k)
    r[n] = round((x[n]**2+y[n]**2)**0.5, k)
    ax[n] = round(-x[n]/(r[n])**3, k)
    ay[n] = round(-y[n]/(r[n])**3, k)
    vx[n+1] = round(vx[n]+delta*ax[n], k)
    vy[n+1] = round(vy[n]+delta*ay[n], k)

for n in range(N-1):
   print('t', '   ', 'x', '   ', 'y', '    ', 'r', '   ', 'vx', '  ', 'vy')
   print(round(t[n], 2) ,' ', x[n], ' ' , y[n], ' ', r[n], ' ', vx[n], ' ', vy[n])

plt.plot(x, y)
plt.show()
