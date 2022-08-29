# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:23:00 2021

@author: luisb
"""
import sys
import math

from EA import *

#160 lumen/watt es el rendimiento luminoso de los leds actuales 
rendimientoLED = 160

def fun(sol):
    lumens = sol[0]
    angulo = sol[1]
    litArea = litAreaCalc(angulo, floorHeight)
    lightsNeeded = math.ceil(floorArea/litArea)
    luxProduced = (lumens/litArea) * lightsNeeded
    kwh = (lumens/rendimientoLED)/1000
    price = kwh * kwhPrice * lightsNeeded
    fitness = abs(luxDesired - luxProduced) + price + abs(lightsNeeded * litArea - floorArea)
    return fitness

def litAreaCalc(angulo: int, h: float):
    angulo = angulo/2
    angulo = math.radians(angulo)
    radio = math.tan(angulo) * h
    litArea = math.pi * (radio**2)
    return litArea

def printRes(sol):
    lumens = sol[0]
    angulo = sol[1]
    litArea = litAreaCalc(angulo, floorHeight)
    lightsNeeded = math.ceil(floorArea/litArea)
    luxProduced = (lumens/litArea) * lightsNeeded
    kw = (lumens/rendimientoLED)/1000
    price = kw * kwhPrice * lightsNeeded
    print("Luces necesarias: ", lightsNeeded)
    print("Lumens de la luz: ", lumens)
    print("Angulo de apertura de la luz: ", angulo)
    print("Gastos de consumo: %f €/h"%(price))
    print("lux: ", luxProduced)

################ Inputs de usuario ################

while(True):
    try:
        luxDesired = int(input("Introduzca Lux a nivel de suelo deseados: "))
        if(luxDesired < 1):
            print("Valor no valido, debe ser mayor que uno")
            print("Introduzca Lux a nivel de suelo deseados: ")
        else:
            break
    except:
        print("Error de formato")

while(True):
    try:
        kwhPrice = float(input("Introduzca precio del kWh contratado: "))
        if(kwhPrice <= 0):
            print("Valor no valido, debe ser mayor que cero")
            print("Introduzca precio del kWh contratado: ")
        else:
            break
    except:
        print("Error de formato")
    
while(True):
    try:
        floorArea = float(input("Introduzca Area en metros cuadrados de su superficie: "))
        if(floorArea <= 0):
            print("Valor no valido, debe ser mayor que cero")
            print("Introduzca Area en metros de su superficie: ")
        else:
            break
    except:
        print("Error de formato")
    
while(True):
    try:
        floorHeight = float(input("Introduzca altura en metros de su superficie: "))
        if(floorHeight <= 0):
            print("Valor no valido, debe ser mayor que cero")
            print("Introduzca altura en metros de su superficie: ")
            print("\n")
        else:
            break
    except:
        print("Error de formato")

################ Fin inputs de usuario ################

myBounds = [(20,32400),(15,160)]

myEA = EA(fun,myBounds,55)

myEA.run(1500)
bestGenome = myEA.best()
printRes(bestGenome.genVector[0])

sys.exit()