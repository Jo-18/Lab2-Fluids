import numpy as np
import matplotlib.pyplot as plt

# Abrir el archivo en modo lectura
with open('PIVlab3.txt', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()

# Inicializar listas vacías para cada columna
x = []
y = []
u = []
v = []
vector_type = []

# Iterar sobre cada línea de datos, saltando las primeras 3 líneas
for line in lines[3:]:
    # Dividir la línea en columnas usando una coma
    columns = line.strip().split(',')
    
    # Añadir cada valor a la lista correspondiente
    x.append(float(columns[0]))
    y.append(float(columns[1]))
    u.append(float(columns[2]) if columns[2] != 'NaN' else None)
    v.append(float(columns[3]) if columns[3] != 'NaN' else None)
    vector_type.append(int(columns[4]))

# Filtrar las listas para eliminar las posiciones donde haya un None en 'u'
filtered_x = []
filtered_y = []
filtered_u = []
filtered_v = []
filtered_vector_type = []

for i in range(len(vector_type)):
    if vector_type[i] == 1 and y[i] < 0.007:
        filtered_x.append(x[i])
        filtered_y.append(y[i])
        filtered_u.append(u[i])
        filtered_v.append(v[i])
        filtered_vector_type.append(vector_type[i])

# Definir la viscosidad
h = 0.00981

# Inicializar listas vacías para du_dy y shear_stress
du_dy = []
shear_stress = []

# Calcular du_dy y shear_stress
for i in range(1, len(filtered_u) - 1):
    delta_y = filtered_y[i + 1] - filtered_y[i - 1]
    if delta_y != 0:
        du_dy_value = (filtered_u[i + 1] - filtered_u[i - 1]) / delta_y
    else:
        du_dy_value = 0
    du_dy.append(du_dy_value)
    shear_stress.append(h * du_dy_value)

# Crear gráfico de x vs u
fig, ax = plt.subplots()

# Graficar los datos filtrados
ax.plot(filtered_x, filtered_u, marker='o', linestyle='-', color='b')

# Añadir etiquetas a los ejes
ax.set_xlabel('x [m]')
ax.set_ylabel('u [m/s]')

# Añadir un título al gráfico
ax.set_title('Gráfico de x vs u')

# Mostrar el gráfico
plt.show()

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar los datos filtrados
ax.plot(filtered_y, filtered_v, marker='o', linestyle='-', color='b')

# Añadir etiquetas a los ejes
ax.set_xlabel('y [m]')
ax.set_ylabel('v [m/s]')

# Añadir un título al gráfico
ax.set_title('Gráfico de y vs v')

# Mostrar el gráfico
plt.show()



# Crear gráfico de filtered_y vs shear_stress
plt.plot(filtered_y[1:-1], shear_stress, marker='o', linestyle='-', color='r')
plt.xlabel('y [m]')
plt.ylabel('Shear Stress [Pa]')
plt.title('Gráfico de y vs Shear Stress')
plt.show()