# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 10:43:08 2021

@author: Heinrich
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Model parameters

tp=1.0
tShft=77.63565829952906
#tval=120.0
Temp=1150
dCat=1.9
#Crat=0.4
CratInf = 0.8666363299836257
CratPow = -0.7473596674118302
k0 = 6655.590279343692
EaoR = 17579.95147734162

# Model expression

def func(Cratf,tvalf,Tempf):
    alpha_m = Cratf*CratInf*(Cratf)**CratPow
    alpha_p = alpha_m*(1-np.exp((-1)*Cratf*k0*alpha_m/dCat*(tvalf+tShft)**tp*np.exp((-1)*EaoR/(273.15+Tempf))))
    feval = alpha_p*100
    return feval

toffset = 60

# Create 2D input grid

xf = np.linspace(0.01,1.0,200)
yf = np.linspace(0+toffset,180,200)
xxf,yyf = np.meshgrid(xf,yf)
yyf = yyf - toffset

zf1 = np.zeros((len(xf),len(yf)))

for i in range(len(xf)):
    for j in range(len(yf)):
        zf1[j,i] = func(xf[i],yf[j],Temp)

## Repeat for two more values of Temp input

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.view_init(elev=20, azim=125)
# ax.view_init(elev=5, azim=90)

ax.plot_surface(xxf,yyf, zf1*1.01, cmap="RdYlGn")
# plt.show()

zf2 = np.zeros((len(xf),len(yf)))
for i in range(len(xf)):
    for j in range(len(yf)):
        zf2[j,i] = func(xf[i],yf[j],Temp+100)

# ax.plot_surface(xxf,yyf, zf2*1.01, cmap="YlGnBu")
ax.plot_surface(xxf,yyf, zf2*1.01, cmap="viridis_r")
# plt.show()

zf3 = np.zeros((len(xf),len(yf)))
for i in range(len(xf)):
    for j in range(len(yf)):
        zf3[j,i] = func(xf[i],yf[j],Temp+200)

# ax.plot_surface(xxf,yyf, zf3*1.01, cmap="PuBuGn")
ax.plot_surface(xxf,yyf, zf3*1.01, cmap="cividis")

ax.set_title('Output surfaces')
ax.set_xlabel('Input 2')
ax.set_ylabel('Input 3')
# ax.set_yticklabels([])
ax.set_zlabel('Output %')

plt.show()

## Additional plots for analyzing contours in more detail

# fig = plt.figure()
# plt.contourf(xxf,yyf, zf1*1.01, 20, cmap="RdYlGn");
# plt.colorbar();plt.show()

fig = plt.figure()
plt.contour(xxf,yyf, zf1*1.01, 20, cmap="RdYlGn");
plt.title('Output')
plt.xlabel('Input 3')
plt.ylabel('Input 2')

cbar = plt.colorbar()
cbar.set_label('%')

plt.show()

# fig = plt.figure()
# plt.contourf(xxf,yyf, zf2*1.01, 20, cmap="RdYlGn");
# plt.colorbar();plt.show()

# fig = plt.figure()
# plt.contour(xxf,yyf, zf2*1.01, 20, cmap="RdYlGn");
# plt.colorbar();plt.show()

# fig = plt.figure()
# plt.contourf(xxf,yyf, zf3*1.01, 20, cmap="RdYlGn");
# plt.colorbar();plt.show()

# fig = plt.figure()
# plt.contour(xxf,yyf, zf3*1.01, 20, cmap="RdYlGn");
# plt.colorbar();plt.show()




