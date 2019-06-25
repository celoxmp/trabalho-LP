from Factory import Factory
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:19:13 2019

@author: Marcelo
"""
print("Resolução de problema caixeiro viajante com 38 cidades a serem visitadas.")
print("Será impressa a menor distancia que cada algoritmo encontrou.")
print()

factory = Factory()
print(factory.create_heuristic('Genetic Algorithm').calculate())
print(factory.create_heuristic('Grasp').calculate())
print(factory.create_heuristic('Two Opt').calculate())
print(factory.create_heuristic('Greedy').calculate())
print(factory.create_heuristic('Greedy Random').calculate())