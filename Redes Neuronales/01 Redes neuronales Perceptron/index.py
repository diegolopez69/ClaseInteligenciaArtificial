# Librerías
import numpy as np

def perceptron(W,X):
 # Multiplicar W*X elemento a elemento los vectores = w1*x1+w2*x2+w3*x3
 s= np.sum(W*X)
 print("La suma w1.x1+w2.x2+w3.x3 es: ",s)
 # Aplicar la función de activación (por ejemplo tanh) al resultado 's'
 pred = np.tanh(s)
 return pred 