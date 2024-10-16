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