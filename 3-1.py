import matplotlib.pyplot as plt
import numpy as np

l=3  
r=0.1  #step length
y=[0.9901,0.9615,0.9174]  # y when x=r

x1=np.arange(0,l+r,r,dtype=float)    #Forward difference
y1=[]
y1.append(1)
for i in range(0,int(l/r)):
    y1.append(-2*x1[i]*y1[i]*r+y1[i]) 

plt.title('Forward difference',size=20)
plt.xlabel('x',size=15)
plt.ylabel('y',size=15)
plt.plot(x1,y1)
plt.show()

x2=np.arange(0,l+r,r,dtype=float)    #Backward difference
y2=[]
y2.append(1)
for i in range(0,int(l/r)):
    y2.append(y2[i]/(2*x2[i+1]*r+1)) 

plt.title('Backward difference',size=20)
plt.xlabel('x',size=15)
plt.ylabel('y',size=15)
plt.plot(x2,y2)
plt.show()

x3=np.arange(0,l+r,r,dtype=float)    #Central difference
y3=[]
y3.append(1)
y3.append(y[int(r*10)-1])    # y when x=r
for i in range(0,int(l/r)-1):
    y3.append(-4*x3[i+1]*y3[i+1]*r+y3[i]) 

plt.title('Central difference',size=20)
plt.xlabel('x',size=15)
plt.ylabel('y',size=15)
plt.plot(x3,y3)
plt.show()

plt.title('Contrast',size=20)
plt.xlabel('x',size=15)
plt.ylabel('y',size=15)
plt.plot(x1,y1,label='Forward')
plt.plot(x2,y2,label='Backward')
plt.plot(x3,y3,label='Central')
plt.legend()
plt.show()