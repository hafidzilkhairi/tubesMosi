import numpy as np
import random

dots = []
def findW(N, a, b):
    return (b-a)/N

def partisi(N, a, b):
    # for i in range(N):
    #     dots.append(random.uniform(a, b))
    file = open('dataUniform.csv', 'r')
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
    partisi(N,a,b)
    defineFX(N)
    result = summary(N,a,b)
    return result


result = run(200,2,4)
print(result)

