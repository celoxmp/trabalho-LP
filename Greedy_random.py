import random
from Heuristic import Heuristic
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:37:50 2019

@author: Marcelo
"""

class Greedy_random(Heuristic):
    def __init__(self, EntryData):
        self.data = EntryData().data
        self.n = EntryData().n
        
    def calculate(self):
        print("Começando o cálculo com algoritmo Guloso Randômico: ")
        return self.length(self.nearest_neighbor_random(0, 0.5))
        
    def nearest_neighbor_random(self, i, alpha):
        """
        Recebe a cidade inicial e retorna uma lista com o caminho percorrido
        """
        unvisited = list(range(self.n))
        unvisited.remove(i)
        last = i
        tour = [i]
        while unvisited != []:
            next = self.nearest_random(last, unvisited, alpha)
            tour.append(next)
            unvisited.remove(next)
            last = next
        return tour
    
    def nearest_random(self, last, unvisited, alpha):
        """
        Função recebe como entrada o vértice 'last', a lista de vértices não visitados 'unvisited' e o parâmetro alpha 'alpha'
        (heurística gulosa randomizada)
        e retorna o número do vizinho aleatório dentro dos alpha*len(unvisited) vizinhos mais próximos
        """
        dist_last = []
        for i in unvisited[0:]:
            dist_last.append((i,self.data[last,i]))
        dist_last.sort(key=lambda x: x[1])
        pos_max = int(alpha*len(dist_last))
        pos = int(random.uniform(0,pos_max))
        return dist_last[pos][0]
    
    def length(self, tour):
        """Calculate the length of a tour according to distance matrix 'D'."""
        z = self.data[tour[-1], tour[0]]    # edge from last to first city of the tour
        for i in range(1,len(tour)):
            z += self.data[tour[i], tour[i-1]]      # add length of edge from city i-1 to i
        return z