import pandas as pd
import numpy as np
import math
import random
import time

def mk_closest():
    """Compute a sorted list of the distances for each of the nodes.

    For each node, the entry is in the form [(d1,i1), (d2,i2), ...]
    where each tuple is a pair (distance,node).
    """
    C = []
    for i in range(n):
        dlist = [(D[i,j], j) for j in range(n) if j != i]
        dlist.sort()
        C.append(dlist)
    return C

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
    dist_last = []
    for i in unvisited[0:]:
        dist_last.append((i,D[last,i]))
    dist_last.sort(key=lambda x: x[1])
    pos_max = int(alpha*len(dist_last))
    pos = int(random.uniform(0,pos_max))
    return dist_last[pos][0]

def nearest(last, unvisited):
    """
    Função recebe como entrada o vértice 'last' e a lista de vértices não visitados 'unvisited' e retorna o número
    do vértice mais próximo
    (mais perto)
    """
    near = unvisited[0]
    dist_last = []
    for i in unvisited[0:]:
        dist_last.append((i,D[last,i]))
    dist_last.sort(key=lambda x: x[1])
    return dist_last[0][0]

def nearest_neighbor_random(i, alpha):
    """
    Recebe a cidade inicial e retorna uma lista com o caminho percorrido
    """
    unvisited = list(range(n))
    unvisited.remove(i)
    last = i
    tour = [i]
    while unvisited != []:
        next = nearest_random(last, unvisited, alpha)
        tour.append(next)
        unvisited.remove(next)
        last = next
    return tour

def nearest_neighbor(i):
    """
    Recebe a cidade inicial e retorna uma lista com o caminho percorrido
    """
    unvisited = list(range(n))
    unvisited.remove(i)
    last = i
    tour = [i]
    while unvisited != []:
        next = nearest(last, unvisited)
        tour.append(next)
        unvisited.remove(next)
        last = next
    return tour

def randtour():
    """
    Constrói uma lista (caminho) aleatoriamente
    """
    sol = list(range(n))
    random.shuffle(sol)
    return sol


def cost_change(n1, n2, n3, n4):
    return D[n1,n3] + D[n2,n4] - D[n1,n2] - D[n3,n4]


def two_opt(route):
    best = route
    improved = True
    k=0
    c=0
    while improved:
        improved = False
        for i in range(1, (len(route) - 2)):
            for j in range((i + 1), len(route)):
                if j - i == 1: continue
                if cost_change(best[i-1],best[i],best[j-1],best[j]) < 0:
                    best[i:j] = best[j-1:i-1:-1]
                    improved = True     
                    c+=1
        route = best;
        k+=1
    return best,length(best),k,c


random.seed(time.clock())
file = pd.read_csv("tsp-instance.csv")
cities = file["city"].values
n = len(cities)
distances = np.zeros((n, n))
coord = []
for i in range(0, n):
    coord.append((file['x'][i], file['y'][i]))
D = mk_matrix(coord)

alpha = 0.4
tour_rand = randtour()
print("Aleatoria", length(tour_rand))
tour_guloso = nearest_neighbor(0)
print("Algoritmo Guloso", length(tour_guloso))
tour_rand_guloso = nearest_neighbor_random(0, alpha)
print("Algoritmo Guloso Randomizado", length(tour_rand_guloso))
a,b,c,d = two_opt(tour_rand_guloso)
print("Solucao Busca Local", b)
print("Iterações:", d)