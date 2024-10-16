import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo promedios.txt en modo lectura
with open('textoprueba.txt', 'r') as file:
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

# Ordenar las listas según los valores de y
sorted_indices = np.argsort(y)
x = [x[i] for i in sorted_indices]
y = [y[i] for i in sorted_indices]
u = [u[i] for i in sorted_indices]
v = [v[i] for i in sorted_indices]
vector_type = [vector_type[i] for i in sorted_indices]
shear_stress = [shear_stress[i] for i in sorted_indices]

# Calcular los promedios
promedio_u = np.mean(u)
promedio_v = np.mean(v)
promedio_shear_stress = np.mean(shear_stress)

# Imprimir los promedios
print('-------')
print(x)
print(y)
print(u)
print(v)
print(vector_type)
print(shear_stress)
print('-------')

# Crear una figura y un eje para el gráfico de x vs u
fig, ax = plt.subplots()

# Graficar los datos de x y u
ax.plot(x, u, marker='o', linestyle='-', color='b')

# Añadir etiquetas a los ejes
ax.set_xlabel('x [m]')
ax.set_ylabel('u [m/s]')

# Añadir un título al gráfico
ax.set_title('x vs u')

# Mostrar el gráfico
plt.show()