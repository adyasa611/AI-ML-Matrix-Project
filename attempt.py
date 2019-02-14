import numpy as np
import matplotlib.pyplot as plt
A = np.array([1,-1])
B = np.array([7,-1])
C = np.linalg.norm(A)
D = np.linalg.norm(B)

E = np.array([(A[0]/C),(A[1]/C)])
F = np.array([(B[0]/D),(B[1]/D)])
G = E-F
H = E+F
slope1 = (G[1]/G[0])
slope2 = (H[1]/H[0])

POI = np.array([1,2])
x = np.linspace(0.,5.)

fig,ax = plt.subplots()
ax.plot(x,(slope1*(x-(POI[0]))+POI[1]),'-o',markersize=10,markevery=x.size)
ax.plot(x,(slope2*(x-(POI[0]))+POI[1]),'-o',markersize=10,markevery=x.size)

ax.set_xlim((0.,5.))
ax.set_ylim((0.,5.))

ax.xaxis.set_ticks(np.arange(0.,5.,0.5))
ax.yaxis.set_ticks(np.arange(0.,5.,0.5))

plt.show()
point1 = np.array([0,(slope1*(0-(POI[0]))+POI[1])])
point2 = np.array([0,(slope2*(0-(POI[0]))+POI[1])])

if point1[1] != 0:
	print(point1)
else:
	print(point2)
		
