from graphviz import Digraph

def draw_prerequisite_graph():
    dot = Digraph(format="png")  # Formato de salida opcional (puedes cambiar a PDF, SVG, etc.)
    
    # Configurar el estilo general del grafo
    dot.attr(rankdir='TB', size='12')  # Disposición de arriba hacia abajo
    
    # Agregar nodos con forma de rectángulo
    courses = {
        "Fluidos": "Fluidos",
        "TermoQ": "Termodinámica Química",
        "Termodinámica": "Termodinámica",
        "Transferencia": "Transferencia de Calor",
        "Máquinas": "Máquinas Térmicas",
        "CFD": "CFD",
        "Gestión": "Gestión de Recursos Energéticos",
        "Aeronáutica": "Aeronáutica",
        "Lab": "Lab Procesos y Sistemas Energéticos"
    }
    
    for key, label in courses.items():
        dot.node(key, label, shape="rect", style="filled", fillcolor="lightblue", fontname="Arial", fontsize="12")

    # Definir conexiones como prerrequisitos
    edges = [
        ("Fluidos", "Termodinámica"),
        ("TermoQ", "Termodinámica"),
        ("Termodinámica", "Transferencia"),
        ("Transferencia", "Máquinas"),
        ("Transferencia", "CFD"),
        ("Máquinas", "Gestión"),
        ("CFD", "Aeronáutica"),
        ("Termodinámica", "Lab"),
    ]

    for edge in edges:
        dot.edge(*edge)

    # Mostrar y guardar el grafo
    dot.render("prerequisitos", view=True)  # Esto guardará y abrirá la imagen

# Llamar a la función para generar el diagrama
draw_prerequisite_graph()
