import numpy as np
from matplotlib import pyplot as plt
from math import pi
P1 = np.array([1,0])
P2 = np.array([2,3])

omat = np.array([[0,1],[-1,0]])
tangent1 = np.array([0,1])
normal1 = np.matmul(omat,tangent1)#centre passes through the normal
normal = normal1.T
C1 = (P2-P1).T
D1 = np.matmul(P2,P2)-np.matmul(P1,P1)
D_1 = D1 * 0.5
D2 = 1
e = np.array([D2,D_1])
H = np.vstack((normal,C1))
inverse = np.linalg.inv(H)
centre = np.matmul(inverse,e)
radius = np.linalg.norm((P1-centre))
a=radius 
print (radius)
print (centre)

t = np.linspace(0, 2*pi, 100)
x = np.linspace(-2,4)
y = np.linspace(0,0)
r1 = np.linspace(P1[0],centre[0])
r2 = np.linspace(P1[1],centre[1])
fig,ax = plt.subplots()
ax.plot( centre[0]+a*np.cos(t) , centre[1]+a*np.sin(t) )
ax.plot( centre[0], centre[1],'o')
ax.text(centre[0]- 0.2*centre[0], centre[1]-0.2*centre[1],centre)
ax.plot( P1[0],P1[1],'o')
ax.text(P1[0]-0.5*P1[0],P1[1]-0.5*P1[1],P1)
ax.plot( P2[0],P2[1],'o')
ax.text(P2[0]-0.1*P2[0],P2[1]-0.1*P2[1],P2)
ax.plot(x,y)
ax.plot(r1,r2)
diameter = radius*2
print('Diameter is  ' + str(diameter))

plt.grid(color='lightgray',linestyle='--')
plt.axis('equal')
plt.show()
