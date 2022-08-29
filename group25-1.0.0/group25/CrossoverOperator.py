# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:37:02 2020

@author: luisb
"""
from Operator import Operator
from Genome import Genome
import random

class CrossoverOperator(Operator):    

    def apply(colGenome: list()):
        cr = 0.6
        if(random.random() <= cr):
            return colGenome[1]
        else: 
            return colGenome[0]
