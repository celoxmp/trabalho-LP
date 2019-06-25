from Greedy_random import Greedy_random
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:29:28 2019

@author: Marcelo
"""

class Two_opt: # Busca Local de k=2 (muda entre 2 posições)
    def __init__(self, EntryData):
        self.data = EntryData().data
        self.n = EntryData().n
        self.greedy_random = Greedy_random(EntryData)
        
    def calculate(self):
        parcial_solution = self.greedy_random.nearest_neighbor_random(0, 0.5)
        best, best_solution = self.two_opt(parcial_solution)
        return best_solution;
        
    def two_opt(self, route):
        best = route
        improved = True
        counter = 0
        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route)):
                    if j - i == 1: continue
                    if self.cost_change(best[i - 1], best[i], best[j - 1], best[j]) < 0:
                        best[i:j] = best[j - 1:i - 1:-1]
                        improved = True
                        counter = counter + 1
            route = best
        return best,self.greedy_random.length(best)

    def cost_change(self, n1, n2, n3, n4):
        return self.data[n1,n3] + self.data[n2,n4] - self.data[n1,n2] - self.data[n3,n4]