import networkx as nx
from random import randint
import matplotlib.pyplot as plt

mendonza = ['Letos','Alberto','Rodrigo','Karla','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau']
chilangos = ['Carmen','Gabriel','Gaby','Javier']
familia = []
#for i in range(4):

G = nx.Graph()
G.add_nodes_from([mendonza, vidal, boston, chilangos])

fig, ax = plt.subplots(figsize=(1,1))
nx.draw(G, with_labels=True, ax=ax)
print(G)