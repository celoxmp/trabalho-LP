import sys
from GA import GA
from EntryData import EntryData
from Grasp import Grasp
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:19:13 2019

@author: Marcelo
"""

ga2 = GA(EntryData)
ga2.geneticAlgorithm(popSize=100, eliteSize=20, mutationRate=0.01, generations=100)
