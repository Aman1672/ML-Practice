#   Optmimization through Booth function by randomization
import random as r
def boothFunc(x):
    s=(x[0]+2*x[1]-7)**2+(2*x[0]+x[1]-5)**2
    return s

minfv = 9999
for i in range(10000):
    x=[r.randint(-10,10),r.randint(-10,10)]
    fv=boothFunc(x)
    if fv < minfv:
        minfv = fv
        minx = x

print(minx,minfv)