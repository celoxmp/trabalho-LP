import pandas as pd
import numpy as np
import math
import random
import time

def distL2(x1_y1,x2_y2):
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

def mk_matrix(coord):
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
            D[i,j] = distL2((x1,y1), (x2,y2))
            D[j,i] = D[i,j]
    return D

def length(tour):
    """Calculate the length of a tour according to distance matrix 'D'."""
    z = D[tour[-1], tour[0]]    # edge from last to first city of the tour
    for i in range(1,len(tour)):
        z += D[tour[i], tour[i-1]]      # add length of edge from city i-1 to i
    return z

def nearest_random(last, unvisited, alpha):
    """
    Função recebe como entrada o vértice 'last', a lista de vértices não visitados 'unvisited' e o parâmetro alpha 'alpha'
    (heurística gulosa randomizada)
    e retorna o número do vizinho aleatório dentro dos alpha*len(unvisited) vizinhos mais próximos
    """

def nearest(last, unvisited):
    """
    Função recebe como entrada o vértice 'last' e a lista de vértices não visitados 'unvisited' e retorna o número
    do vértice mais próximo
    (mais perto)
    """


def nearest_neighbor_random(i, alpha):
    """
    Recebe a cidade inicial e retorna uma lista com o caminho percorrido - Heurística gulosa randomizada
    """

def nearest_neighbor(i):
    """
    Recebe a cidade inicial i e retorna uma lista com o caminho percorrido - Algoritmo guloso
    """
    caminho = []
    valor = 0
    for k in range(i,n):
        min1 = 0
        minPos = 0
        for j in range(0,n):
            if k != j and D[k,j] < min1 and j not in caminho:
                min1 = D[k,j]
                minPos = j
        if(min1 != 0):
            caminho.append(minPos)
            valor += min1
    return valor
                

def randtour():
    """
    Constrói uma lista (caminho) aleatoriamente - Heurística aleatória
    """

random.seed(time.clock())
file = pd.read_csv("tsp-instance.csv")
cities = file["city"].values
n = len(cities)
distances = np.zeros((n, n))
coord = []
for i in range(0, n):
    coord.append((file['x'][i], file['y'][i]))
D = mk_matrix(coord)
#print(np.matrix(D));

print(nearest_neighbor(0))
