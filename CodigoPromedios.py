import matplotlib.pyplot as plt

# Abrir el archivo promedios.txt en modo lectura
with open('promedios.txt', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()

# Inicializar listas vacías para cada columna
x = []
y = []
u = []
v = []
vector_type = []
shear_stress = []

# Iterar sobre cada línea de datos, saltando la primera línea
for line in lines[1:]:
    # Dividir la línea en columnas usando una coma
    columns = line.strip().split(',')
    
    # Añadir cada valor a la lista correspondiente
    x.append(float(columns[0]))
    y.append(float(columns[1]))
    u.append(float(columns[2]))
    v.append(float(columns[3]))
    vector_type.append(int(columns[4]))
    shear_stress.append(float(columns[5]))

# Imprimir las listas para verificar los resultados
print("x:", x)
print("y:", y)
print("u:", u)
print("v:", v)
print("vector_type:", vector_type)
print("shear_stress:", shear_stress)

# Crear una figura y un eje para el gráfico de x vs u
fig1, ax1 = plt.subplots()

# Graficar los datos filtrados
ax1.plot(x, u, marker='o', linestyle='-', color='b')

# Añadir etiquetas a los ejes
ax1.set_xlabel('x [m]')
ax1.set_ylabel('u [m/s]')
plt.show()

# Crear una figura y un eje para el gráfico de y vs v
fig2, ax2 = plt.subplots()

# Graficar los datos filtrados
ax2.plot(y, v, marker='o', linestyle='-', color='r')

# Añadir etiquetas a los ejes
ax2.set_xlabel('y [m]')
ax2.set_ylabel('v [m/s]')

# Añadir un título al gráfico
ax2.set_title('Velocity Profile in y-direction')

# Mostrar el gráfico
plt.show()

# Crear una figura y un eje para el gráfico de x vs u
fig3, ax3 = plt.subplots()

# Graficar los datos de x y u
ax3.plot(y, v, marker='o', linestyle='-', color='g')

# Añadir etiquetas a los ejes
ax3.set_xlabel('x [m]')
ax3.set_ylabel('u [m/s]')

# Añadir un título al gráfico
ax3.set_title('x vs u')

# Mostrar el gráfico
plt.show()