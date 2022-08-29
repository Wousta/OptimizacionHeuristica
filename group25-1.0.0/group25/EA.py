import sys
from abc import ABC, abstractmethod
from Population import *
from Genome import *
from SelectionOperator import *
from MutationOperator import *
from CrossoverOperator import *
from ReplacementOperator import *
import random

class EA(object):
    """docstring for EA"""
    
    mejorPoblacion = Population()
    
    ## Constructor de la clase EA ##
    def __init__(self,minifun,bounds,psize):
        super(EA, self).__init__()
        self.minifun = minifun
        self.bounds = bounds 
        self.psize = psize
        
        #Te da el mejor genoma de una poblacion
    def bestPob (self, poblacion: Population()):
        colGenome = poblacion.colGenome
        best = colGenome[0]
        bestFitness = colGenome[0].genVector[1]
        for i in range (0,len(colGenome)):
            elemento = colGenome[i]
            if elemento.genVector[1] < bestFitness: 
                bestFitness = elemento.genVector[1]
                best = elemento
            i = i+1
        return best
    
    
    #Te da el mejor genoma de la última población
    def best (self):
        global mejorPoblacion
        colGenome = mejorPoblacion.colGenome
        best = colGenome[0]
        bestFitness = colGenome[0].genVector[1]
        for i in range (0,len(colGenome)):
            elemento = colGenome[i]
            if elemento.genVector[1] < bestFitness: 
                bestFitness = elemento.genVector[1]
                best = elemento
            i = i+1
        return best
        
    #Ejecuta el algoritmo
    def run (self,iteraciones: int):
        global mejorPoblacion
        poblacionActual = Population()
        bounds = self.bounds
        #grafica = list()
        
        i = 0
        while i < self.psize:     
            solucion = list()
            
            j = 0
            while j < len(bounds):
                boundsActual = bounds[j]
                solucion.append(random.uniform(boundsActual[0],boundsActual[1]))
                j = j+1
            # Fin while (len(bounds)) 
                
            fitness = self.minifun(solucion)
            genoma = Genome (solucion,fitness)
            poblacionActual.appendGenome(genoma)
            i = i+1
        # Fin while (psize)
            
        #grafica.append(self.bestPob(poblacionActual).genVector[1])
        
        i = 0
        while i < iteraciones:
            iRand = random.randint(0,len(poblacionActual.colGenome))
            nuevaPoblacion = Population()
            
            j = 0
            while j < len(poblacionActual.colGenome):
                seleccion = SelectionOperator.apply(poblacionActual,j)
                mutation = MutationOperator.apply(seleccion)
                soluciones = mutation.genVector[0]
                
                p = 0
                while p < len(soluciones):
                    elementoBounds = self.bounds[p]
                    if soluciones[p] < elementoBounds[0]: 
                        soluciones[p] = elementoBounds[0]    
                    if soluciones[p] > elementoBounds[1]:
                        soluciones[p] = elementoBounds[1]  
                    p = p+1
                # Fin while (len(soluciones))     
                
                mutation.genVector[1] = self.minifun(mutation.genVector[0])
                if j == iRand: 
                    crossover = mutation
                    nuevaPoblacion.appendGenome(crossover)
                else:
                    crossoverList = [poblacionActual.colGenome[j],mutation]
                    crossover = CrossoverOperator.apply(crossoverList)
                    nuevaPoblacion.appendGenome(crossover)
                j = j+1
            # Fin while (pop.lenPob(poblacionActual))
            
            poblacionActual = ReplacementOperator.apply(poblacionActual,nuevaPoblacion)
            #col = poblacionActual.colGenome
            
            #grafica.append(self.bestPob(poblacionActual).genVector[1])
            i = i+1
        # Fin while (iteraciones)
        
        mejorPoblacion = poblacionActual
        return poblacionActual       

