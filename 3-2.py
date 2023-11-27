import matplotlib.pyplot as plt
import math
import numpy as np

det_t=10
det_x=50000
cnt_t=int(600*3600/det_t)   #q3 600->2000
cnt_x=int(5000000/det_x)
c=0.5
b=det_t/det_x*c
t=[i*det_t for i in range(0,cnt_t+1)]
x=[i*det_x for i in range(0,cnt_x+1)]
u=np.zeros((cnt_t+1,cnt_x+1))

for i in range(0,cnt_t+1):
    u[i][0]=0
    u[i][cnt_x]=0

for j in range(0,cnt_x+1): 
    u[0][j]=10*math.sin(2*math.pi*j*det_x/1000000)

for i in range(0,cnt_t):
    for j in range(1,cnt_x):
        u[i+1][j]=u[i][j]-b*(u[i][j]-u[i][j-1])

#====================================================q1&q2
plt.title('Contrast',size=20)
plt.xlabel('x',size=15)
plt.ylabel('u',size=15)
plt.plot(x,u[0],label="t=0")
plt.plot(x,u[int(cnt_t/2)],label="t=300h")
plt.plot(x,u[cnt_t],label="t=600h")
plt.legend()
plt.show()

#====================================================q3
v=[]
for i in range(0,cnt_t+1):
    v.append(u[i][49])
plt.title('Intermediate point',size=20)
plt.xlabel('t',size=15)
plt.ylabel('u',size=15)
plt.plot(t,v)
plt.show() 

