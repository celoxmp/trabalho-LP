from EntryData import EntryData
from GA import GA
from Grasp import Grasp
from Two_opt import Two_opt
from Greedy import Greedy
from Greedy_random import Greedy_random
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:08:17 2019

@author: Marcelo
"""

class Factory:
    def create_heuristic(self, type):
        if type == 'Genetic Algorithm':
            return GA(EntryData)
        elif type == 'Two Opt':
            return Two_opt(EntryData)
        elif type == 'Grasp':
            return Grasp(EntryData)
        elif type == 'Greedy':
            return Greedy(EntryData)
        elif type == 'Greedy Random':
            return Greedy_random(EntryData)
        else:
            return Grasp(EntryData)
    
    