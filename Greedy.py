from Greedy_random import Greedy_random
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:37:50 2019

@author: Marcelo
"""

class Greedy(Greedy_random):
    def calculate(self):
        return self.length(self.nearest_neighbor_random(0, 0))