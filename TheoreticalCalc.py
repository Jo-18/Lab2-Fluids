import numpy as np
import matplotlib.pyplot as plt

v_max = 1.35982
R = 0.0265
h = 0.00981
r = np.arange(0, 0.0265 + 0.00001, 0.00001).tolist()

v_r = [v_max * (1 - (ri / R) ** 2) for ri in r]
dv_dr = np.gradient(v_r, r)
shear_stress = [-h * dv for dv in dv_dr]

plt.figure()
plt.plot(r, v_r, label='v(r)')
plt.xlabel('r (m)')
plt.ylabel('v_r (m/s)')
plt.title('Theoretical Velocity Profile')
plt.legend()
plt.show()


plt.figure()
plt.plot(r, shear_stress, label='shear_stress')
plt.xlabel('r (m)')
plt.ylabel('Shear Stress (Pa)')
plt.title('Theoretical Shear Stress Profile')
plt.legend()
plt.show()