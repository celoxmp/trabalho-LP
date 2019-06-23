import sys
from GA import GA
from EntryData import EntryData
from Grasp import Grasp
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:19:13 2019

@author: Marcelo
"""
print("Começando o cálculo com algoritmo genético: ")

ga2 = GA(EntryData)
ga2.geneticAlgorithm(popSize=100, eliteSize=20, mutationRate=0.01, generations=100)
print()

print("Começando o cálculo com algoritmo Grasp: ")

grasp = Grasp(EntryData)
best, best_solution = grasp.calculate_GRASP(1000, 0.5)
print(best)
print()


tour_guloso = grasp.nearest_neighbor_random(0,0)
print("Algoritmo Guloso", length(tour_guloso))
print()
tour_rand_guloso = grasp.nearest_neighbor_random(0, 0.5)
print("Algoritmo Guloso Randomizado", length(tour_rand_guloso))
print()
best, best_solution = grasp.two_opt(tour_rand_guloso)
print("Solucao Busca Local após guloso", best_solution)
