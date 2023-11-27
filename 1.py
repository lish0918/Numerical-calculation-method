import pandas as pd
import matplotlib.pyplot as plt

x1=[]
x2=[]
x1.append(0.7)
x2.append(0.700000001)
for i in range(1,50):
    m=2.5*x1[i-1]*(1-pow(x1[i-1],2))
    if m>1:
        break
    n=2.5*x2[i-1]*(1-pow(x2[i-1],2))
    if n>1:
        break
    x1.append(m)
    x2.append(n)

x_axis=list(range(0,i+1))
plt.title('Sensitivity analysis',size=20)
plt.plot(x_axis,x1,color='green',label='x0 = 0.700000000')
plt.plot(x_axis,x2,color='skyblue',label='x0 = 0.700000001')
plt.legend()
plt.xlabel('times',size=15)
plt.ylabel('x',size=15)
plt.show()