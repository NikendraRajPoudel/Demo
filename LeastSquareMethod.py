import matplotlib.pyplot as plt
import numpy as np
print('Python Program for fitting straight line y = a + b*x')
n = int(input('enter the number of data points(n):'))
x= np.zeros(n)
y = np.zeros(n)
print('Enter the values of x and y')
for i in range (n):
    x[i] = float(input("x["+str(i)+"]= "))
    y[i]= float(input("y["+str(i)+"]="))
SUMX,SUMX2,SUMY,SUMXY=0,0,0,0
for i in range(n):
    SUMX+=x[i]
    SUMX2+=x[i]*x[i]
    SUMY+=y[i]
    SUMXY+=x[i]*y[i]

b= (n*SUMXY-SUMX*SUMY)/(n*SUMX2-SUMX*SUMX)
a=(SUMY- b*SUMX)/n
print("the best fitted line by least square method is  y = %0.6f + %0.6fx"%(a,b))
plt.scatter(x,y)
plt.show()
plt.plot(x,y)
plt.show()