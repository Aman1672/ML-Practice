# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:22:31 2019

@author: Gaurav
"""
import math as m
import random as r

def BoxBettsQuadraticSum(x):
    def g(x,i):
        return m.exp(-0.1*(i+1)*x[0])\
    -m.exp(-0.1*(i+1)*x[1])\
    -m.exp(((-0.1*(i+1))-m.exp(-1*(i+1)))*x[2])

    D = 3
    res = 0
    for i in range(D):
        res += g(x,i)**2
    return res

min_fx = 99999
min_x = None
for i in range(10000):
    x = [r.uniform(0.9,1.2),r.uniform(9,11.2),r.uniform(0.9,1.2)]
    fx = BoxBettsQuadraticSum(x)
    if(fx<min_fx):
        min_fx = fx
        min_x = x

print(min_fx,min_x)