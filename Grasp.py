import random
import matplotlib.pyplot as plt
from Two_opt import Two_opt

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:16:54 2019

@author: Marcelo
"""

class Grasp:
    def __init__(self, EntryData):
        self.data = EntryData().data
        self.n = EntryData().n
        self.two_opt = Two_opt(EntryData)
        
    def calculate(self):
        best, best_solution = self.calculate_GRASP(1000, 0.5)
        return best;
    
    def calculate_GRASP(self, num_iterations, alpha):
        best = 1000000
        for i in range(0,num_iterations):
            first_city = random.randint(0, self.n - 1)
            solution = self.two_opt.greedy_random.nearest_neighbor_random(first_city, alpha)
            solution_improved, solution_value_improved = self.two_opt.two_opt(solution)
            if(solution_value_improved < best):
                best_solution = solution_improved
                best = solution_value_improved
        return best, best_solution
    
    def calculate_GRASP_Plot(self, num_iterations, alpha):
        best = 1000000
        progress = []
        for i in range(0,num_iterations):
            first_city = random.randint(0, self.n - 1)
            solution = self.two_opt.greedy_random.nearest_neighbor_random(first_city, alpha)
            solution_improved, solution_value_improved = self.two_opt.two_opt(solution)
            if(solution_value_improved < best):
                best_solution = solution_improved
                best = solution_value_improved
                #progress.append(best)
            progress.append(solution_value_improved)
        plt.plot(progress)
        plt.ylabel('Distance')
        plt.xlabel('Iterations')
        plt.show()
        print(best)
        #return best, best_solution