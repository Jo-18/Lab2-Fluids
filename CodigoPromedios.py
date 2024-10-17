import matplotlib.pyplot as plt

# Abrir el archivo promedios.txt en modo lectura
with open('promedios.txt', 'r') as file:
    lines = file.readlines()

x = []
y = []
u = []
v = []
vector_type = []
shear_stress = []

# Iterar sobre cada línea de datos
for line in lines:
    columns = line.strip().split(',')
    x.append(float(columns[0]))
    y.append(float(columns[1]))
    u.append(float(columns[2]))
    v.append(float(columns[3]))
    vector_type.append(int(columns[4]))
    shear_stress.append(float(columns[5]))

sum_u = {}
sum_v = {}
sum_shear_stress = {}
count = {}

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

promedios_u = []
promedios_v = []
promedio_ss = []
unique_y = []

for key in sum_u:
    promedios_u.append(sum_u[key] / count[key])
    promedios_v.append(sum_v[key] / count[key])
    promedio_ss.append(sum_shear_stress[key] / count[key])
    unique_y.append(key)


fig2, ax2 = plt.subplots()
ax2.plot(unique_y, promedios_v, marker='o', linestyle='-', color='r')
ax2.set_xlabel('y [m]')
ax2.set_ylabel('v [m/s]')
ax2.set_title('Average Velocity Profile in y-direction')
plt.show()

fig3, ax3 = plt.subplots()
ax3.plot(unique_y, promedio_ss, marker='o', linestyle='-', color='g')
ax3.set_xlabel('y [m]')
ax3.set_ylabel('Shear Stress [Pa]')
ax3.set_title('Average Shear Stress Profile in y-direction')
plt.show()
