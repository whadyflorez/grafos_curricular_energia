import networkx as nx
import matplotlib.pyplot as plt

def draw_graph():
    # Crear el grafo dirigido
    G = nx.DiGraph()
    
    # Definir los nodos organizados por niveles
    level_1 = ["Fluidos", "Termodinámica Química"]
    level_2 = ["Termodinámica"]
    level_3 = ["Transferencia de Calor"]
    level_4 = ["Máquinas Térmicas", "CFD"]
    level_5 = ["Gestión de Recursos Energéticos", "Aeronáutica"]
    level_6 = ["Lab Procesos y Sistemas Energéticos"]
    
    nodes = level_1 + level_2 + level_3 + level_4 + level_5 + level_6
    G.add_nodes_from(nodes)
    
    # Definir las conexiones como prerrequisitos
    edges = [
        ("Fluidos", "Termodinámica"),
        ("Termodinámica Química", "Termodinámica"),
        ("Termodinámica", "Transferencia de Calor"),
        ("Transferencia de Calor", "Máquinas Térmicas"),
        ("Transferencia de Calor", "CFD"),
        ("Máquinas Térmicas", "Gestión de Recursos Energéticos"),
        ("CFD", "Aeronáutica"),
        ("Termodinámica", "Lab Procesos y Sistemas Energéticos"),
    ]
    G.add_edges_from(edges)
    
    # Definir posiciones de los nodos por niveles
    pos = {}
    spacing_x = 2.5  # Espaciado horizontal entre nodos en un mismo nivel
    spacing_y = 2.0  # Espaciado vertical entre niveles
    
    levels = [level_1, level_2, level_3, level_4, level_5, level_6]
    for i, level in enumerate(levels):
        x_start = -((len(level) - 1) * spacing_x) / 2  # Centrar los nodos
        for j, node in enumerate(level):
            pos[node] = (x_start + j * spacing_x, -i * spacing_y)
    
    # Dibujar el grafo
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=3500, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold", arrows=True)
    
    # Dibujar flechas indicando prerrequisitos
    edge_labels = {edge: "→" for edge in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    plt.title("Estructura de prerrequisitos en cursos del área de Térmicas y Fluidos")
    plt.show()

# Llamar la función para dibujar el grafo
draw_graph()
