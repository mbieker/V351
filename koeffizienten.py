# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:06:39 2014

@author: martin
"""

# BERECHNUNG DER FOURIER KOEFFIZIENTEN

from numpy import *

def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{tabular}{'
    #Get dimensions
    if(onedim == 'true'):
        if(flip == 'false'):
        
            data = array([[i] for i in data])
        
        else:
            data = array([data])
        

    row_cnt, col_cnt = data.shape
    header_cnt = len(header)
    
    if(header_cnt == col_cnt and flip== 'false'):
        #Make Format
        output += '|'
        for i in range(col_cnt):
            output += 'c|'
        output += '}\n\\hline\n'+ header[0]
        for i in range (1,col_cnt):
            output += ' & ' +  header[i]
        output += ' \\\\\n\\hline\n'
        for i in data:
            output += str(i[0])
            for j in range(1,col_cnt):
                output += ' & ' + str( i[j])
            output += '\\\\\n'
        output += '\\hline\n\\end{tabular}\n'
                            
        return output
    else:
        if(row_cnt == header_cnt):
            output += '|c|' + (col_cnt)*'c' + '|}\n\\hline\n'
            for i in range(row_cnt):
                output += header[i] 
                for j in range(col_cnt):
                    output += ' & ' + str(data[i][j])
                output += '\\\\\n\\hline\n'
                
            output += '\\end{tabular}\n'  
            return output
        else:
            return 'ERROR'


def hut(n):
    return 2*(1-(-1)**n)/(pi**2*n**2)

def rect(n):
    return 2*(1-(-1)**n)/(pi*n)
    
def saw(n):
    return -2*(-1)**n/(pi*n)
    

data = array([[int(i), round(hut(i),3), round(saw(i),3) , round(rect(i),3)] for i in range(1,10) ])

print make_LaTeX_table(data, ["n", r'Dreick [$a_n]$',r'S\"agezahn [$b_n$]',r'Rechteck $[b_n]$']) 


data_ = [[i, round(hut(i)*0.6/ hut(1),3),'x',round(saw(i)*0.6/saw(1),3),'x',round(rect(i)*0.6/rect(1),3),'x'] for i in range(1,10)]
header = ["n","Amplitude [V]",r"$\Delta \varphi$","Amplitude [V]",r"$\Delta \varphi$","Amplitude [V]",r"$\Delta \varphi$"]

print(array(data))
print make_LaTeX_table(array(data_),header)


print 'Analyse Ergebnisse'
rechteck = array([6.08,2.08,1.32,1.04,0.880,0.78,.720,.648,.608])

rechteck_norm = array([round(i/rechteck[0],3) for i in rechteck])

theo_rect_norm = array ([round(rect(2*i+1)/rect(1),3) for i in range(0,9)])
error =array([round((rechteck_norm[i]-theo_rect_norm[i])/rechteck_norm[i] ,3) for i in range(9)])
data = array([rechteck,rechteck_norm,theo_rect_norm, error])

print(make_LaTeX_table(data.T, ['x','x','x','x']))


################################################################################
rechteck = array([5.6,0.656,0.184,0.112,0.040])

rechteck_norm = array([round(i/rechteck[0],3) for i in rechteck])

theo_rect_norm = array ([round(hut(2*i+1)/hut(1),3) for i in range(5)])
error =array([round((rechteck_norm[i]-theo_rect_norm[i])/rechteck_norm[i] ,3) for i in range(5)])
data = array([rechteck,rechteck_norm,theo_rect_norm, error])
print "Dreiecksfunktion"
print(make_LaTeX_table(data.T, ['x','x','x','x']))



################################################################################
rechteck = array([2.94,2.34,1.02,1.16,.066,.8,.520,.600,.456])

rechteck_norm = array([round(i/rechteck[0],3) for i in rechteck])

theo_rect_norm = array ([round(abs(saw(i+1)/saw(1)),3) for i in range(9)])
error =array([round((rechteck_norm[i]-theo_rect_norm[i])/rechteck_norm[i] ,3) for i in range(9)])
data = array([rechteck,rechteck_norm,theo_rect_norm, error])

print "Sägezahnspannung"
print(make_LaTeX_table(data.T, ['x','x','x','x']))
