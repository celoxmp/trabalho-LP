import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from EntryData import EntryData

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:52:49 2019

@author: Marcelo
"""

class GA:
    def __init__(self, EntryData):
        entry = EntryData()
        self.data = entry.data
        self.n = entry.n
        self.list = entry.list
    
    def createRoute(self, cityList):
        route = random.sample(cityList, len(cityList))
        return route

    def initialPopulation(self, popSize, cityList):
        population = []
    
        for i in range(0, popSize):
            population.append(self.createRoute(cityList))
        return population
    
    def rankRoutes(self, population):
        fitnessResults = {}
        for i in range(0,len(population)):
            fitnessResults[i] = Fitness(population[i],self.data).routeFitness()
        return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
    
    
    def selection(self, popRanked, eliteSize):
        selectionResults = []
        df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
        df['cum_sum'] = df.Fitness.cumsum()
        df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()
    
        for i in range(0, eliteSize):
            selectionResults.append(popRanked[i][0])
        for i in range(0, len(popRanked) - eliteSize):
            pick = 100 * random.random()
            for i in range(0, len(popRanked)):
                if pick <= df.iat[i, 3]:
                    selectionResults.append(popRanked[i][0])
                    break
        return selectionResults
    
    def matingPool(self, population, selectionResults):
        matingpool = []
        for i in range(0, len(selectionResults)):
            index = selectionResults[i]
            matingpool.append(population[index])
        return matingpool
    
    
    def breed(self, parent1, parent2): #crossover
        child = []
        childP1 = []
        childP2 = []
    
        geneA = int(random.random() * len(parent1))
        geneB = int(random.random() * len(parent1))
    
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)
    
        for i in range(startGene, endGene):
            childP1.append(parent1[i])
    
        childP2 = [item for item in parent2 if item not in childP1]
    
        child = childP1 + childP2
        return child
    
    
    def breedPopulation(self, matingpool, eliteSize):
        children = []
        length = len(matingpool) - eliteSize
        pool = random.sample(matingpool, len(matingpool))
    
        for i in range(0, eliteSize):
            children.append(matingpool[i])
    
        for i in range(0, length):
            child = self.breed(pool[i], pool[len(matingpool) - i - 1])
            children.append(child)
        return children
    
    
    def mutate(self, individual, mutationRate):
        for swapped in range(len(individual)):
            if (random.random() < mutationRate):
                swapWith = int(random.random() * len(individual))
    
                city1 = individual[swapped]
                city2 = individual[swapWith]
    
                individual[swapped] = city2
                individual[swapWith] = city1
        return individual
    
    
    def mutatePopulation(self, population, mutationRate):
        mutatedPop = []
    
        for ind in range(0, len(population)):
            mutatedInd = self.mutate(population[ind], mutationRate)
            mutatedPop.append(mutatedInd)
        return mutatedPop
    
    def nextGeneration(self, currentGen, eliteSize, mutationRate):
        popRanked = self.rankRoutes(currentGen)
        selectionResults = self.selection(popRanked, eliteSize)
        matingpool = self.matingPool(currentGen, selectionResults)
        children = self.breedPopulation(matingpool, eliteSize)
        nextGeneration = self.mutatePopulation(children, mutationRate)
        return nextGeneration
    
    
    def geneticAlgorithm(self, popSize, eliteSize, mutationRate, generations):
        pop = self.initialPopulation(popSize, self.list)
        print("Initial distance: " + str(1 / self.rankRoutes(pop)[0][1]))
    
        for i in range(0, generations):
            pop = self.nextGeneration(pop, eliteSize, mutationRate)
    
        print("Final distance: " + str(1 / self.rankRoutes(pop)[0][1]))
        bestRouteIndex = self.rankRoutes(pop)[0][0]
        bestRoute = pop[bestRouteIndex]
        return bestRoute
    
    
    def geneticAlgorithmPlot(self, popSize, eliteSize, mutationRate, generations):
        pop = self.initialPopulation(self.list, popSize)
        progress = []
        progress.append(1 / self.rankRoutes(pop)[0][1])
    
        for i in range(0, generations):
            pop = self.nextGeneration(pop, eliteSize, mutationRate)
            progress.append(1 / self.rankRoutes(pop)[0][1])
    
        plt.plot(progress)
        plt.ylabel('Distance')
        plt.xlabel('Generation')
        plt.show()
        
class Fitness:
    def __init__(self, route, data):
        self.route = route
        self.distance = 0
        self.fitness = 0.0
        self.data = data

    def routeDistance(self):
        if self.distance == 0:
            self.distance = self.length(self.route)
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness
    
    def length(self, tour):
        """Calculate the length of a tour according to distance matrix 'D'."""
        z = self.data[tour[-1][2], tour[0][2]]    # edge from last to first city of the tour
        for i in range(1,len(tour)):
            z += self.data[tour[i][2], tour[i-1][2]]      # add length of edge from city i-1 to i
        return z
