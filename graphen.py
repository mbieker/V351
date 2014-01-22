# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:03:21 2014

@author: martin
"""

from matplotlib.pyplot import plot, close, savefig , xlim , ylim, xlabel, ylabel
from numpy import sign, linspace, floor

print(-1.5%1)
def rect(x):
    x =  x - floor(x+0.5)
    if(x < 0):
        return -1
    else:
        return 1

def hut(x):
    x =  x - floor(x+0.5)
    return 1-abs(2*x)   
    
def saw(x):
     x =  x - floor(x+0.5)
     return 2*x
t_1 = linspace(-1.5,-0.50001,200)
t_2 = linspace(-0.5,0.4999,200)
t_3 = linspace(0.5,1.5,200)

close()
plot(t_1, [saw(i) for i in t_1],'b--')
plot(t_2, [saw(i) for i in t_2],'b-')
plot(t_3, [saw(i) for i in t_3],'b--')
xlim(-1.5,1.5)
ylim(-1.1,1.1)
xlabel(r'$\frac{t}{T}$')
ylabel(r'Amplitude')
savefig('./abb/Abb1.png')

close()
plot(t_1, [hut(i) for i in t_1],'b--')
plot(t_2, [hut(i) for i in t_2],'b-')
plot(t_3, [hut(i) for i in t_3],'b--')
xlim(-1.5,1.5)
ylim(-0.1,1.1)
xlabel(r'$\frac{t}{T}$')
ylabel(r'Amplitude')
savefig('./abb/Abb2.png')

close()
plot(t_1, [rect(i) for i in t_1],'b--')
plot(t_2, [rect(i) for i in t_2],'b-')
plot(t_3, [rect(i) for i in t_3],'b--')
xlim(-1.5,1.5)
ylim(-1.1,1.1)
xlabel(r'$\frac{t}{T}$')
ylabel(r'Amplitude')
savefig('./abb/Abb3.png')




