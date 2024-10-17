import numpy as np
import matplotlib.pyplot as plt

v_max = 1.35982 # m/s
R = 0.0265 # m
h = 0.00981 # constante
r = np.arange(0, 0.0265 + 0.00001, 0.00001).tolist() # m

# Crear la lista v_r para almacenar los valores de v
v_r = [v_max * (1 - (ri / R) ** 2) for ri in r]

# Calcular la derivada de v_r con respecto a r usando diferencias finitas
dv_dr = np.gradient(v_r, r)

# Calcular la lista shear_stress
shear_stress = [-h * dv for dv in dv_dr]

# Crear el gráfico para el perfil de velocidad
plt.figure()
plt.plot(r, v_r, label='v(r)')

# Añadir etiquetas a los ejes
plt.xlabel('r (m)')
plt.ylabel('v_r (m/s)')

# Añadir un título al gráfico
plt.title('Theoretical Velocity Profile')

# Añadir una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

# Crear el gráfico para el esfuerzo cortante
plt.figure()
plt.plot(r, shear_stress, label='shear_stress')

# Añadir etiquetas a los ejes
plt.xlabel('r (m)')
plt.ylabel('Shear Stress (Pa)')

# Añadir un título al gráfico
plt.title('Theoretical Shear Stress Profile')

# Añadir una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()