import numpy as np
nd=128
st=1.40
n0=24
nv0=55/st
nv=55/st
nv=5
F=500

#print("vueltas:",nv,"R:",nv*25*2*3.14159,st-0.5)
#t=np.arange(nd*nv)/nd+1.5
t=np.arange(nd*nv)/nd+40

x=st*t*np.cos(t*np.pi*2)
y=st*t*np.sin(t*np.pi*2)

import matplotlib.pyplot as plt
#plt.plot(x,y)
#plt.show()
print("M3S1000F1")
i=0;
X=x[i]
Y=y[i]
print("G0Z3;")
print(f"G1F{F}X{X:.4f}Y{Y:.4f};")
print(f"G1F{F}Z{X/350-0.02:.4f};")
#x0=1/350;
#y0=1/350;
x0=0
y0=0
z0=0
for i in range(int(nd*nv)):
    X=x[i]
    Y=y[i]
    print(f"G1F{F}X{X:.4f}Y{Y:.4f}Z{X*x0+Y*y0+z0:.4f};")

