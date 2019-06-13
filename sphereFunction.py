# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:20:16 2019

@author: Gaurav
"""

def SphereFunction(x):
    res = 0
    for n in x:
        res += n**2
    return res

import random as r
D = 10
min_fx = 9999
min_x = None

for i in range(10000):
    x = [r.randint(0,10) for i in range(D)]
    fx = SphereFunction(x)
    if(fx<min_fx):
        min_fx = fx
        min_x = x

print(min_fx,min_x)