import networkx as nx
from random import randint
import matplotlib.pyplot as plt

mendonza = ['Letos','Alberto','Rodrigo','Karla','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau']
chilangos = ['Carmen','Gabriel','Gaby','Javier']
familia = mendonza + vidal + boston + chilangos
familias = [mendonza, vidal, boston, chilangos]

G = nx.Graph()
G.add_nodes_from(familia)

for i in range(len(familias)):
    for j in range(i + 1, len(familias)):
        for persona1 in familias[i]:
            for persona2 in familias[j]:
                G.add_edge(persona1, persona2)

adjM = nx.adjacency_matrix(G)
adjM = adjM.todense()
print(adjM)

# Asignar colores
color_map = []
for persona in familia:
    if persona in mendonza:
        color_map.append('red')
    elif persona in vidal:
        color_map.append('blue')
    elif persona in boston:
        color_map.append('green')
    elif persona in chilangos:
        color_map.append('orange')


# Dibujar
fig, ax = plt.subplots(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=1000, ax=ax)
#plt.show()
