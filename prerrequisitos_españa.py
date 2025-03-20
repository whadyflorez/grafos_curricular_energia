import graphviz

# Crear el gráfico de prerrequisitos
dot = graphviz.Digraph(format='png', engine='dot')

# Nivel 1: Formación Básica
dot.node('FB1', 'Matemáticas\n(Álgebra, Cálculo I, Cálculo II)')
dot.node('FB2', 'Física\n(Física I, Física II)')
dot.node('FB3', 'Química')
dot.node('FB4', 'Informática para la Ingeniería')
dot.node('FB5', 'Expresión Gráfica')
dot.node('FB6', 'Empresa:\nIntroducción a la Gestión Empresarial')

# Nivel 2: Comunes a la Rama Industrial
dot.node('RI1', 'Termodinámica y\nTransmisión de Calor')
dot.node('RI2', 'Mecánica de Fluidos')
dot.node('RI3', 'Ciencia y Tecnología\nde los Materiales')
dot.node('RI4', 'Resistencia de Materiales')
dot.node('RI5', 'Fundamentos de Electrotecnia')
dot.node('RI6', 'Teoría de Máquinas y Mecanismos')

# Nivel 3: Tecnología Específica
dot.node('TE1', 'Ingeniería Térmica I')
dot.node('TE2', 'Máquinas de Fluidos')
dot.node('TE3', 'Ingeniería de Materiales')
dot.node('TE4', 'Diseño de Máquinas I')
dot.node('TE5', 'Teoría de Estructuras y\nConstrucciones Industriales')

# Nivel 4: Intensificación
dot.node('IN1', 'Motores y Máquinas Térmicas')
dot.node('IN2', 'Diseño Mecánico Asistido')
dot.node('IN3', 'Ingeniería del Transporte')
dot.node('IN4', 'Vehículos Híbridos y Eléctricos')

# Conexiones de prerrequisitos
dot.edge('FB1', 'RI1')  # Matemáticas -> Termodinámica
dot.edge('FB2', 'RI1')  # Física -> Termodinámica
dot.edge('FB2', 'RI2')  # Física -> Mecánica de Fluidos
dot.edge('FB3', 'RI3')  # Química -> Ciencia y Tecnología de los Materiales
dot.edge('FB1', 'RI4')  # Matemáticas -> Resistencia de Materiales
dot.edge('FB2', 'RI4')  # Física -> Resistencia de Materiales
dot.edge('FB1', 'RI6')  # Matemáticas -> Teoría de Máquinas
dot.edge('FB5', 'RI6')  # Expresión Gráfica -> Teoría de Máquinas

dot.edge('RI1', 'TE1')  # Termodinámica -> Ingeniería Térmica
dot.edge('RI2', 'TE2')  # Mecánica de Fluidos -> Máquinas de Fluidos
dot.edge('RI3', 'TE3')  # Ciencia y Tecnología de los Materiales -> Ingeniería de Materiales
dot.edge('RI4', 'TE5')  # Resistencia de Materiales -> Teoría de Estructuras
dot.edge('RI6', 'TE4')  # Teoría de Máquinas -> Diseño de Máquinas

dot.edge('TE1', 'IN1')  # Ingeniería Térmica -> Motores y Máquinas Térmicas
dot.edge('TE4', 'IN2')  # Diseño de Máquinas -> Diseño Mecánico Asistido
dot.edge('TE2', 'IN3')  # Máquinas de Fluidos -> Ingeniería del Transporte
dot.edge('IN3', 'IN4')  # Ingeniería del Transporte -> Vehículos Híbridos y Eléctricos

# Guardar y mostrar el gráfico
dot.render('prerequisitos_ingenieria_mecanica', view=True)
