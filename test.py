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

#梯度为零

for j in range(0,cnt_x+1): 
    u[0][j]=10*math.sin(2*math.pi*j*det_x/1000000)

for i in range(0,cnt_t):
    for j in range(1,cnt_x+1): #u[i][0]=u[i][1] u[i][cnt_x]=u[i][cnt_x-1]
        u[i+1][j]=u[i][j]-b*(u[i][j]-u[i][j-1])
    u[i+1][0]=u[i+1][1]

v=np.zeros((cnt_t+1,cnt_x+1))

#相同变化趋势
for j in range(0,cnt_x+1): 
    v[0][j]=10*math.sin(2*math.pi*j*det_x/1000000)

for i in range(0,cnt_t):
    for j in range(1,cnt_x+1): 
            v[i+1][j]=v[i][j]-b*(v[i][j]-v[i][j-1])
    v[i+1][0]=v[i][0]+v[i+1][1]-v[i][1]

w=np.zeros((cnt_t+1,cnt_x+1))

#海绵边界条件
for j in range(0,cnt_x+1): 
    w[0][j]=10*math.sin(2*math.pi*j*det_x/1000000)

a=[0,0.25,0.5,0.75,1]
for i in range(0,cnt_t):
    for j in range(0,cnt_x+1): #u[i][j]=(1-a)*u[i][4]+a*u[0][0]
        if j<5:
            w[i+1][j]=a[j]*w[i][4]-0.25*b*w[i][4]
        else:
            w[i+1][j]=w[i][j]-b*(w[i][j]-w[i][j-1])

#====================================================q3
plt.title('t=300h',size=20)
plt.xlabel('x',size=15)
plt.ylabel('u',size=15)
plt.plot(x,u[int(cnt_t/2)],label="1")
plt.plot(x,v[int(cnt_t/2)],label="2")#u[int(cnt_t/2)]
plt.plot(x,w[int(cnt_t/2)],label="3")#u[cnt_t]
plt.legend()
plt.show()

plt.title('t=600h',size=20)
plt.xlabel('x',size=15)
plt.ylabel('u',size=15)
plt.plot(x,u[cnt_t],label="1")
plt.plot(x,v[cnt_t],label="2")#u[int(cnt_t/2)]
plt.plot(x,w[cnt_t],label="3")#u[cnt_t]
plt.legend()
plt.show()


