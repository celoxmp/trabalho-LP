from igraph import Graph,plot

grafo1 = Graph(edges = [(0,1),(1,2),(2,3),(3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())


print(grafo1)
plot(grafo1, bbox = (300,300))


grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(3,2),(2,1),(1,0)], directed = True)
grafo2.vs['label'] = range(grafo2.vcount())
print(grafo2)
plot(grafo2, bbox = (300,300))


grafo3 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo3.vs['name'] = ['a','b','c','d']
grafo3.add_vertex(4)
print(grafo3)
plot(grafo3, bbox = (300,300))

print(grafo3.get_adjacency())