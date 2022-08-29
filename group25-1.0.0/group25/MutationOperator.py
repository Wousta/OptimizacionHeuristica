# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:35:05 2020

@author: luisb
"""
from Operator import Operator
from Genome import Genome

class MutationOperator(Operator):
    
    def apply(colGenome: list()):
        F = 0.7
        xi = colGenome[0].genVector[0]
        xr1, xr2 = colGenome[1].genVector[0], colGenome[2].genVector[0]
        xrand = colGenome[3].genVector[0]
        solucion = list()
        
        i = 0
        while i < len(xi):
            vi = xi[i] + F*(xrand[i] - xi[i]) + F*(xr1[i] - xr2[i])
            solucion.append(vi)
            i = i + 1
            
        return Genome(solucion,0)