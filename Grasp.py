import random
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:16:54 2019

@author: Marcelo
"""

class Grasp:
    def __init__(self, EntryData):
        self.data = EntryData().data
        self.n = EntryData().n
    
    def calculate_GRASP(self, num_iterations, alpha):
        best = 1000000
        for i in range(0,num_iterations):
            first_city = random.randint(0, self.n - 1)
            solution = self.nearest_neighbor_random(first_city, alpha)
            solution_improved, solution_value_improved = self.two_opt(solution)
            if(solution_value_improved < best):
                best_solution = solution_improved
                best = solution_value_improved
        return best, best_solution
    
    def calculate_GRASP_Plot(self, num_iterations, alpha):
        best = 1000000
        progress = []
        for i in range(0,num_iterations):
            first_city = random.randint(0, self.n - 1)
            solution = self.nearest_neighbor_random(first_city, alpha)
            solution_improved, solution_value_improved = self.two_opt(solution)
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
        return best,self.length(best)

    def cost_change(self, n1, n2, n3, n4):
        return self.data[n1,n3] + self.data[n2,n4] - self.data[n1,n2] - self.data[n3,n4]

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