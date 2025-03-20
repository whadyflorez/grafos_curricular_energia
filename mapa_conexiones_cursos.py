import networkx as nx
import matplotlib.pyplot as plt

def draw_graph():
    # Crear el grafo dirigido
    G = nx.DiGraph()
    
    # Definir los nodos (cursos)
    nodes = [
        "Fluidos", "Termodinámica", "Transferencia de Calor", "Gestión de Recursos Energéticos", 
        "Máquinas Térmicas", "CFD", "Aeronáutica", "Termodinámica Química", "Lab Procesos y Sistemas Energéticos"
    ]
    G.add_nodes_from(nodes)
    
    # Definir las conexiones entre los cursos
    edges = [
        ("Fluidos", "Termodinámica"),
        ("Termodinámica", "Transferencia de Calor"),
        ("Transferencia de Calor", "Gestión de Recursos Energéticos"), ("Gestión de Recursos Energéticos", "Transferencia de Calor"),
        ("Termodinámica", "Máquinas Térmicas"),
        ("Fluidos", "CFD"), ("CFD", "Fluidos"),
        ("Transferencia de Calor", "CFD"), ("CFD", "Transferencia de Calor"),
        ("Termodinámica", "Aeronáutica"), ("Fluidos", "Aeronáutica"),
        ("Transferencia de Calor", "Aeronáutica"),
        ("Termodinámica Química", "Termodinámica"),
        ("Termodinámica", "Lab Procesos y Sistemas Energéticos"),
        ("Fluidos", "Lab Procesos y Sistemas Energéticos"),
    ]
    G.add_edges_from(edges)
    
    # Dibujar el grafo
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42, k=1.5)  # Aumentar k para mayor separación de nodos
    
    # Dibujar nodos y etiquetas
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold", arrows=True)
    
    # Dibujar flechas con curvatura para bidireccionalidad
    edge_labels = {edge: "↔" if (edge[1], edge[0]) in edges else "→" for edge in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle="->", connectionstyle="arc3,rad=0.2")
    
    plt.title("Interrelaciones entre cursos del área de Térmicas y Fluidos")
    plt.show()

# Llamar la función para dibujar el grafo
draw_graph()
