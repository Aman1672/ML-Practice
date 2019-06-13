#   Optimization using Ripple funtion through Randomization
import math as m 
import random as r

def rippleFunction(x):
    for i in range(2):
        fx=m.exp(-2*m.log2(((x[i]-0.1)/0.8)**2))*(((m.sin(5*m.pi*x[i]))**6)+0.1*(m.cos(500*m.pi*x[i]))**2)
        return fx

gfv=999
lfv=999
for k in range(25):
    for i in range(1000):
        x=[r.random(),r.random()]
        fv=rippleFunction(x)
        if fv<lfv:
            lfv=fv
            lx=x
    if lfv<gfv:
        gfv=lfv
        gx=lx
print(gfv,gx)
            
    