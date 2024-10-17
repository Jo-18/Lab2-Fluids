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

# Iterar sobre cada línea de datos
for line in lines:
    # Dividir la línea en columnas usando una coma
    columns = line.strip().split(',')
    
    # Añadir cada valor a la lista correspondiente
    x.append(float(columns[0]))
    y.append(float(columns[1]))
    u.append(float(columns[2]))
    v.append(float(columns[3]))
    vector_type.append(int(columns[4]))
    shear_stress.append(float(columns[5]))

# Inicializar diccionarios para acumular sumas y contar ocurrencias
sum_u = {}
sum_v = {}
sum_shear_stress = {}
count = {}

# Iterar sobre las listas y acumular sumas y conteos
for i in range(len(y)):
    if y[i] not in sum_u:
        sum_u[y[i]] = 0
        sum_v[y[i]] = 0
        sum_shear_stress[y[i]] = 0
        count[y[i]] = 0
    sum_u[y[i]] += u[i]
    sum_v[y[i]] += v[i]
    sum_shear_stress[y[i]] += shear_stress[i]
    count[y[i]] += 1

# Inicializar listas para los promedios
promedios_u = []
promedios_v = []
promedio_ss = []
unique_y = []

# Calcular los promedios y guardarlos en las listas correspondientes
for key in sum_u:
    promedios_u.append(sum_u[key] / count[key])
    promedios_v.append(sum_v[key] / count[key])
    promedio_ss.append(sum_shear_stress[key] / count[key])
    unique_y.append(key)


# Crear una figura y un eje para el gráfico de y vs v
fig2, ax2 = plt.subplots()

# Graficar los datos filtrados
ax2.plot(unique_y, promedios_v, marker='o', linestyle='-', color='r')

# Añadir etiquetas a los ejes
ax2.set_xlabel('y [m]')
ax2.set_ylabel('v [m/s]')

# Añadir un título al gráfico
ax2.set_title('Average Velocity Profile in y-direction')

# Mostrar el gráfico
plt.show()

# Crear una figura y un eje para el gráfico de x vs u
fig3, ax3 = plt.subplots()

# Graficar los datos de x y u
ax3.plot(unique_y, promedio_ss, marker='o', linestyle='-', color='g')

# Añadir etiquetas a los ejes
ax3.set_xlabel('y [m]')
ax3.set_ylabel('Shear Stress [Pa]')

# Añadir un título al gráfico
ax3.set_title('Average Shear Stress Profile in y-direction')

# Mostrar el gráfico
plt.show()
