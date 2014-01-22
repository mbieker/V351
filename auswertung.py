# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 23:48:11 2014

@author: martin
"""
import matplotlib.pyplot as p
from numpy import *
def saege(x,n):
    output = 0
    for i in range(1,n+1):
        output += -2*(-1)**i/(pi*i)*sin(2*pi*i*x)
    return output
    
    
def rechteck(x,n):
    output = 0.5
    for i in range(1,n+1):
        output += 2*(1-(-1)**i)/(pi*i)*sin(2*pi*i*x)
    return output
    
def triangle(x,n):
    output = 0.
    for i in range(1,n+1):
        output += 2*(1-(-1)**i)/(pi**2*i**2)*cos(2*pi*i*x)
    return output
t = linspace(-2,2,10000)
'''
p.close()
p.plot(t, [triangle(x,100) for x in t]) 
p.savefig('./abb/abb1.png')

p.close()
p.plot(t, [rechteck(x,100) for x in t]) 
p.savefig('./abb/abb2.png')

p.close()
p.plot(t, [saege(x,100) for x in t]) 
p.savefig('./abb/abb3.png')'''

print("saege")
for i in range(1,11):
    print("Koeffizient b%i: %s " % (i,str( -2*(-1)**i/(pi*i)/( -2*(-1)**1/(pi*1)))))

print("triangle")
for i in range(1,11):
    print("Koeffizient a%i: %s "  %(i,   str(2*(1-(-1)**i)/(pi**2*i**2)))) 
print("rechteck")
for i in range(1,11):
    print("Koeffizient b.%i: %s " % (i,  str(2*(1-(-1)**i)/(pi*i)/(2*(1-(-1)**1)/(pi*1)))))
