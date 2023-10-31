from sympy import *

a_s = 1
a_H = 0
a_p = Symbol('t*')
t = Symbol('t')

A = Matrix([[a_H,0,0,0,t,0,0,0],[0,a_H,0,0,t,0,0,0],[0,0,a_H,0,t,0,0,0],[0,0,0,a_H,t,0,0,0],[t,t,t,t,a_s,0,0,0],[0,0,0,0,0,a_p,0,0],[0,0,0,0,0,0,a_p,0],[0,0,0,0,0,0,0,a_p]])
A.eigenvals()
A.eigenvects()
print(A.eigenvals())
print(A.eigenvects())