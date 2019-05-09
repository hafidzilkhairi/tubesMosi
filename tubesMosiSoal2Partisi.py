# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:09:49 2019

@author: Wiranata
"""

from numpy import random as rnd

dots = []

def findW(N, a, b):
    return (b-a)/N

def partisi(N):
    # for i in range(N):
    #     dots.append(rnd.normal(0.5, 0.5))
    file = open('dataNormal.csv', 'r')
    datas = file.readlines()
    for i in datas:
            dots.append(float(i))
    return dots

def defineFX(N):
    for i in range(N):
            x = dots[i]
            dots[i] = pow(x,3) + 3*pow(x,2) + 3*x + 1
    return dots

def summary(N, a, b):
    for i in range(N):
            dots[i] = dots[i]*findW(N,a,b) 
    return sum(dots)

def run(N,a,b):
    partisi(N)
    defineFX(N)
    result=summary(N,a,b)
    return result

result=run(200,2,4)
print(result)



#result = run(200,0.5,0.5)
#print(result)
