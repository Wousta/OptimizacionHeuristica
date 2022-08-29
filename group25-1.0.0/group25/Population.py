# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:24:53 2020

@author: luisb
"""
from Genome import Genome

class Population(object):
    
    ## Constructor de la clase Population ##
    def __init__(self):
        self.colGenome = list()
        
    ## Devuelve el tamaño de una poblacion ##
    def lenPoblacion (self):
        return len(self.colGenome)
        
    ## Añade un genoma pasado por argumento al final de la población ##
    def appendGenome(self, g: Genome):
        self.colGenome.append(g)
    
    ## Inserta un genoma pasado como argumento en una posición determinada de la población ##
    def insertGenome(self, g: Genome, pos: int):
        self.colGenome.insert(pos, g)
    
    ## Devuelve un genoma de la población y lo elimina de esta, pasándole la posición del genoma en la población como argumento ##
    def popSolucion (self, pos: int):
        return self.colGenome.pop(pos)
    
    ## Elimina un genoma de la población pasándole el genoma como argumento ##
    def removeGenome (self, element: Genome):
        self.colGenome.remove(element)
        
    ## Obtener la posicion de un genoma en la población a partir del genoma ##    
    def posGenome (self, element: Genome):
        lista = self.colGenome
        res = -1
        for i in range (0,len(lista)):
            elem = lista[i]
            if(elem == element):
                res = i
                break
        return res
    
    ## Obtener la posicion de un genoma en la población a partir del genVector del genoma ##
    def posGenVector (self, genVector: object):
        lista = self.colGenome
        res = -1
        for i in range (0,len(lista)):
            gV = lista[i].genVector
            if(gV == genVector):
                res = i
                break
        return res
    
    ## Obtener la posicion de un genoma en la población a partir de la solucion del genoma ##
    def posSolucion (self, solucion: object):
        lista = self.colGenome
        res = -1
        for i in range (0,len(lista)):
            elem = lista[i].genVector
            sol = elem [0]
            if(sol == solucion):
                res = i
                break
        return res
    
    ## Obtener la posicion de un genoma en la población a partir del fitness del genoma    ##
    ## Devuelve la primera aparición del fitness, si hay más de una aparición no lo indica ##
    def posFitness (self, fitness: int):
        lista = self.colGenome
        res = -1
        for i in range (0,len(lista)):
            elem = lista[i].genVector
            fit = elem [1]
            if(fit == fitness):
                res = i
                break
        return res
    
    ## Intercambia un genoma por otro pasando la posición del primero y el nuevo genoma ##
    def swap (self, genoma: Genome, pos: int):
        lista = self.colGenome
        lista[pos] = genoma;
    
    ## Intercambia un genoma por otro pasando ambos como argumento ##
    def swapGenome (self, genomaOriginal: Genome, genomaNew: Genome):
        pos = self.posGenome(genomaOriginal)
        self.swap(genomaNew,pos)
    
    ## Devuelve la población ordenada de menor a mayor fitness pero no sustituye la original, solo te pasa un nuevo colGenome ##
    def ordenacionAscendente (self): 
        a = self.colGenome[:]
        n = len(a) 
        intercambio = True
        limInf = 0
        limSup = n-1
        while (intercambio==True): 
        
            intercambio = False
        
            for i in range (limInf, limSup):
                elmA = a[i].genVector
                elmB = a[i+1].genVector
                if (elmA[1] > elmB[1]) : 
                    a[i], a[i+1]= a[i+1], a[i] 
                    intercambio=True

            if (intercambio==False): 
                break

            intercambio = False
 
            limSup = limSup-1

            for i in range(limSup-1, limInf-1,-1):
                elmC = a[i].genVector
                elmD = a[i+1].genVector
                if (elmC[1] > elmD[1]): 
                    a[i], a[i+1] = a[i+1], a[i] 
                    intercambio = True
                    
            limInf = limInf+1
            
        return a
    
    # Devuelve la población ordenada de mayor a menor fitness 
    #pero no sustituye la original, solo te pasa un nuevo colGenome
    def ordenacionDescendente (self):
        a = self.colGenome[:]
        n = len(a) 
        intercambio = True
        limInf = 0
        limSup = n-1
        while (intercambio==True): 
        
            intercambio = False
        
            for i in range (limInf, limSup):
                elmA = a[i].genVector
                elmB = a[i+1].genVector
                if (elmA[1] < elmB[1]) : 
                    a[i], a[i+1]= a[i+1], a[i] 
                    intercambio=True

            if (intercambio==False): 
                break

            intercambio = False
 
            limSup = limSup-1

            for i in range(limSup-1, limInf-1,-1):
                elmC = a[i].genVector
                elmD = a[i+1].genVector
                if (elmC[1] < elmD[1]): 
                    a[i], a[i+1] = a[i+1], a[i] 
                    intercambio = True
                    
            limInf = limInf+1
            
        return a