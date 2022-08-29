# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:21:24 2020

@author: luisb
"""
from Operator import Operator
from Population import Population
import random

class SelectionOperator(Operator):
    
    def apply(pob: Population, i: int):
        colGenome = pob.colGenome
        usedVector = list()
        resultVector = list()
        usedVector.append(i)
        resultVector.append(colGenome[i])
        
        while len(usedVector) < 4:
            valor = random.randint(0,len(colGenome)-1)
            
            if (valor not in usedVector):
                usedVector.append(valor)
                resultVector.append(colGenome[valor])
        # Fin while (len(usedVector))
        
        return resultVector