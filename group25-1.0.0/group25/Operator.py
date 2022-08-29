# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:19:40 2020

@author: luisb
"""
from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def apply(self):
        pass