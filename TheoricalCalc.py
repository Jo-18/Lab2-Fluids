import numpy as np
import matplotlib.pyplot as plt

v_max = 1.35982 # m/s
R = 0.0265 # m
r = np.arange(0, 0.0265 + 0.00001, 0.00001).tolist() # m

# Crear la lista v_r para almacenar los valores de v
v_r = [v_max * (1 - (ri / R) ** 2) for ri in r]

# Crear el gráfico
plt.figure()
plt.plot(r, v_r, label='v(r)')

# Añadir etiquetas a los ejes
plt.xlabel('r (m)')
plt.ylabel('v_r (m/s)')

# Añadir un título al gráfico
plt.title('Velocity Profile in r-direction')

# Añadir una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()