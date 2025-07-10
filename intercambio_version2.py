import networkx as nx
import random
import matplotlib.pyplot as plt

mendonza = ['Letos','Norbert','Rodrigo','Karla']
chavos = ['Alberto','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau']
chilangos = ['Carmen','Gabriel','Gaby','Javier']
familia = mendonza + chavos + vidal + boston + chilangos
familias = [mendonza, chavos, vidal, boston, chilangos]

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
    elif persona in chavos:
        color_map.append('purple')
    elif persona in vidal:
        color_map.append('blue')
    elif persona in boston:
        color_map.append('green')
    elif persona in chilangos:
        color_map.append('orange')

disponibles_para_dar = familia.copy()
asignaciones = {}
ya_recibieron = set()

while disponibles_para_dar:
    persona1 = random.choice(disponibles_para_dar)
    vecinos_validos = list(G.neighbors(persona1))
    vecinos_validos = [v for v in vecinos_validos if v not in ya_recibieron]

    if not vecinos_validos:
        print(f"⚠️ No hay a quién regalar para {persona1}, reinicia la rifa")
        break  # o podrías reiniciar desde cero aquí

    persona2 = random.choice(vecinos_validos)

    asignaciones[persona1] = persona2
    ya_recibieron.add(persona2)
    disponibles_para_dar.remove(persona1)

# Mostrar resultados
print("Resultados del intercambio:")
for quien, a_quien in asignaciones.items():
    print(f"{quien} le regala a {a_quien}")

# Dibujar
fig, ax = plt.subplots(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=1000, ax=ax)
#plt.show()
