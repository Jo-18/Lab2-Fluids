import numpy as np
import matplotlib.pyplot as plt

# Abrir el archivo en modo lectura
with open('PIVlab9.txt', 'r') as file:
    lines = file.readlines()

x = []
y = []
u = []
v = []
vector_type = []

# Iterar sobre cada línea de datos, saltando las primeras 3 líneas
for line in lines[3:]:
    columns = line.strip().split(',')

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

for i in range(len(u)):
    if u[i] is not None:
        filtered_x.append(x[i])
        filtered_y.append(y[i])
        filtered_u.append(u[i])
        filtered_v.append(-v[i])
        filtered_vector_type.append(vector_type[i])

first_value_x = filtered_x[0]

# Filtrar las listas para mantener solo los valores donde x es igual al primer valor
final_x = []
final_y = []
final_u = []
final_v = []
final_vector_type = []

for i in range(len(filtered_x)):
    if filtered_x[i] == first_value_x:
        final_x.append(filtered_x[i])
        final_y.append(filtered_y[i])
        final_u.append(filtered_u[i])
        final_v.append(filtered_v[i])
        final_vector_type.append(filtered_vector_type[i])


# Calculo de Shear Stress
du_dy = np.gradient(final_u, final_y)
h = 0.00981
shear_stress = [du_dy_i * h for du_dy_i in du_dy]

# Guardar los resultados en un archivo txt
with open('promedios.txt', 'a') as file:
    for i in range(len(final_x)):
        file.write(f"{final_x[i]}, {final_y[i]}, {final_u[i]}, {final_v[i]}, {final_vector_type[i]}, {shear_stress[i]}\n")

fig2, ax2 = plt.subplots()
ax2.plot(final_y, final_v, marker='o', linestyle='-', color='r')
ax2.set_xlabel('y [m]')
ax2.set_ylabel('v [m/s]')
ax2.set_title('Velocity Profile in y-direction')
plt.show()


fig3, ax3 = plt.subplots()
ax3.plot(final_y, shear_stress, marker='o', linestyle='-', color='g')
ax3.set_xlabel('y [m]')
ax3.set_ylabel('Shear Stress [Pa]')
ax3.set_title('Shear Stress Profile')
plt.show()