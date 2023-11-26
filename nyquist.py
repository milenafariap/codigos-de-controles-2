import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Defina a função de transferência do sistema (por exemplo, G(s) = 1 / (s^2 + 3s + 2))
numerator = [1, 8, 15]
denominator = [1, -6, 8]  # (s+1)(s+2)
system = ctrl.TransferFunction(numerator, denominator)

# Plote o diagrama de Nyquist
plt.figure(figsize=(8, 6))
ctrl.nyquist(system, omega=np.logspace(-1, 2, 100), Plot=True)
plt.title('Diagrama de Nyquist')
plt.xlabel('Re(G(jω))')
plt.ylabel('Im(G(jω))')
plt.grid(True)
plt.show()



