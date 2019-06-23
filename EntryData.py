import pandas as pd
import numpy as np
import math

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:54:30 2019

@author: Marcelo
"""

class EntryData:  #Singleton
    """def __new__(cls, *args, **kwargs):
         if not hasattr(cls, '_instance'):
             cls._instance = super(EntryData, cls).__new__(cls, *args, **kwargs)
         return cls._instance"""
    
    def __init__(self):
        self.data = self.readFile()
     
    def readFile(self):
        file = pd.read_csv("tsp-instance.csv")
        cities = file["city"].values
        n = len(cities)
        distances = np.zeros((n, n))
        coord = []
        coord2 = []
        for i in range(0, n):
            coord.append((file['x'][i], file['y'][i]))
            coord2.append((file['x'][i], file['y'][i], i))
        self.n = n
        self.list = coord2
        return self.mk_matrix(coord)
    
    def mk_matrix(self, coord):
        """Compute a distance matrix for a set of points.
    
        Uses function 'dist' to calculate distance between
        any two points.  Parameters:
        -coord -- list of tuples with coordinates of all points, [(x1,y1),...,(xn,yn)]
        -dist -- distance function
        """
        n = len(coord)
        D = {}      # dictionary to hold n times n matrix
        for i in range(n-1):
            for j in range(i+1,n):
                (x1,y1) = coord[i]
                (x2,y2) = coord[j]
                D[i,j] = self.distL2((x1,y1), (x2,y2))
                D[j,i] = D[i,j]
        return D
    
    def distL2(self, x1_y1,x2_y2):
        """Compute the L2-norm (Euclidean) distance between two points.
    
        The distance is rounded to the closest integer, for compatibility
        with the TSPLIB convention.
    
        The two points are located on coordinates (x1,y1) and (x2,y2),
        sent as parameters"""
        x1, y1 = x1_y1
        x2, y2 = x2_y2
        xdiff = x2 - x1
        ydiff = y2 - y1
        return math.sqrt(xdiff*xdiff + ydiff*ydiff)