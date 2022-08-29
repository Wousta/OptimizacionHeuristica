# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:29:06 2020

@author: luisb
"""
from Operator import Operator
from Population import Population

class ReplacementOperator (Operator):    
    
    def apply(pob1: Population, pob2: Population):
        result = Population()
        colGenome1 = pob1.colGenome
        colGenome2 = pob2.colGenome
        i = 0
        while i < len(colGenome1):
            elem1 = colGenome1[i]
            elem2 = colGenome2[i]
            if elem2.genVector[1] < elem1.genVector[1]: 
                result.appendGenome(elem2)
            else:
                result.appendGenome(elem1)
            i = i+1
                
        return result