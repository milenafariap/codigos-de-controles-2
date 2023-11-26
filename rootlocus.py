import control as ctrl
import matplotlib.pyplot as plt

# Define a função de transferência
numerator = [1]
denominator = [1, 3, 2]  # (s+1)(s+2)
system = ctrl.TransferFunction(numerator, denominator)

# Calcula e plota o root locus
rlocus_data = ctrl.root_locus(system, kvect=None, xlim=None, ylim=None, plotstr='-', Plot=True, PrintGain=True, grid=True)
plt.show()
