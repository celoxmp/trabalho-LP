import sys
from GA import GA
from EntryData import EntryData
from Grasp import Grasp
from Two_opt import Two_opt
from Greedy import Greedy
from Greedy_random import Greedy_random
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:19:13 2019

@author: Marcelo
"""
print("Resolução de problema caixeiro viajante com 38 cidades a serem visitadas.")
print("Será impressa a menor distancia que cada algoritmo encontrou.")
print()

print("Começando o cálculo com algoritmo genético: ")
ga2 = GA(EntryData)
print(ga2.calculate())
#ga2.geneticAlgorithmPlot(popSize=100, eliteSize=20, mutationRate=0.01, generations=100)
print()

print("Começando o cálculo com algoritmo Grasp: ")
grasp = Grasp(EntryData)
print(grasp.calculate())
#grasp.calculate_GRASP_Plot(1000, 0.5)
print()

print("Começando o cálculo com algoritmo Busca Local de k = 2: ")
two_opt = Two_opt(EntryData)
print(two_opt.calculate())
print()

print("Começando o cálculo com algoritmo Guloso: ")
greedy = Greedy(EntryData)
print(greedy.calculate())
print()

print("Começando o cálculo com algoritmo Guloso Randômico: ")
greedy_random = Greedy_random(EntryData)
print(greedy_random.calculate())
print()
