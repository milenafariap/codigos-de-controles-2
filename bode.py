import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Defina a função de transferência do sistema (por exemplo, G(s) = 1 / (s^2 + 3s + 2))
numerator = [1]
denominator = [1, 3, 2]  # (s+1)(s+2)
system = ctrl.TransferFunction(numerator, denominator)

# Calcule a resposta em frequência do sistema
frequency = np.logspace(-1, 2, 1000)  # Frequências de 0.1 a 100 rad/s
magnitude, phase, omega = ctrl.bode(system, omega=frequency)

# Plote o gráfico de magnitude
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(omega, magnitude)
plt.title('Diagrama de Magnitude')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# Plote o gráfico de fase
plt.subplot(2, 1, 2)
plt.semilogx(omega, phase)
plt.title('Diagrama de Fase')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Fase (graus)')
plt.grid(True)

plt.tight_layout()
plt.show()
