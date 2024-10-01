from math import sqrt

def HeronsFormula(a,b,c):
    p = (a+b+c) / 2
    return sqrt(p * (p-a)*(p-b)*(p-c))

