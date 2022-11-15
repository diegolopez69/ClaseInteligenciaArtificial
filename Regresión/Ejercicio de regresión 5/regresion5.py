from socketserver import DatagramRequestHandler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_excel('IBEX35_Sept2018.xls')
dia = data["Dia"]
apertura = data["Apertura"]
print(dia)
print("-------------------------------")
print(apertura)


# Dibujar la gráfica teórica f(x)
degree = 8
plt.title("Gráfica con los datos del IBEX35")
plt.scatter(dia, apertura, color='gray', s=30, marker='H', label="Puntos de entrenamiento")


# Ajuste del polinomio de grado 'degree' a los datos de entrenamiento de los ejes
coeffs = np.polyfit(dia, apertura, deg=degree)
# Determinar y escribir la forma del polinomio
p = np.poly1d(np.polyfit(dia, apertura, deg=degree), variable='X')


y_pred = np.polyval(np.poly1d(coeffs), dia)
print("Error cuadrático medio (ECM): ", 1/20*(sum((apertura-y_pred)**2)))


# Dibujar la gráfica del polinomio
# Calcular la y de la gráfica 'y_plot'
y_plot = np.polyval(np.poly1d(coeffs), dia)

# Dibujar la gráfica
plt.plot(dia, y_plot, color="purple", linewidth=2, label="grado %d" % degree)

# Leyenda del gráfico
plt.legend(loc='lower right')
# Dibujar el gráfico
plt.show()
