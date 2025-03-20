import networkx as nx
import matplotlib.pyplot as plt

def draw_graph():
    # Crear el grafo dirigido
    G = nx.DiGraph()
    
    # Definir los nodos (cursos)
    nodes = [
        "Fluidos", "Termodinámica", "Transferencia de Calor", "Máquinas Térmicas", "Gestión de Recursos Energéticos", 
        "CFD", "Aeronáutica", "Termodinámica Química", "Lab Procesos y Sistemas Energéticos"
    ]
    G.add_nodes_from(nodes)
    
    # Definir las conexiones como prerrequisitos
    edges = [
        ("Fluidos", "Termodinámica"),
        ("Termodinámica", "Transferencia de Calor"),
        ("Transferencia de Calor", "Máquinas Térmicas"),
        ("Máquinas Térmicas", "Gestión de Recursos Energéticos"),
        ("Fluidos", "CFD"),
        ("CFD", "Aeronáutica"),
        ("Termodinámica Química", "Termodinámica"),
        ("Termodinámica", "Lab Procesos y Sistemas Energéticos"),
    ]
    G.add_edges_from(edges)
    
    # Dibujar el grafo
    plt.figure(figsize=(12, 6))
    pos = nx.shell_layout(G)  # Disposición más secuencial
    
    # Dibujar nodos y etiquetas
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold", arrows=True)
    
    # Dibujar flechas indicando prerrequisitos
    edge_labels = {edge: "→" for edge in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    plt.title("Estructura secuencial de prerrequisitos en cursos del área de Térmicas y Fluidos")
    plt.show()

# Llamar la función para dibujar el grafo
draw_graph()
