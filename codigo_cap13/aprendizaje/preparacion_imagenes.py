from __future__ import print_function
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

from mnist import MNIST


#Carga de las imágenes
emnist_data = MNIST(path='datas\\', return_type='numpy')
emnist_data.select_emnist('letters')
Imagenes, Etiquetas = emnist_data.load_training()


print("Cantidad de imágenes ="+str(len(Imagenes)))
print("Cantidad de etiquetas ="+str(len(Etiquetas)))



#Conversión de las imágenes y etiquetas en tabla numpy
import numpy as np
Imagenes = np.asarray(Imagenes)
Etiquetas = np.asarray(Etiquetas)


#Dimensión de las imégenes de trabajo y de aprendizaje
largoImagen = 28
anchoImagen = 28


#Las imágenes están en la forma de una tabla de 124800 líneas y 784 columnas
#Las transformamos en una tabla que contiene 124800 líneas que contiene una tabla de 28*28 columnas
print("Transformación de las tablas de imágenes...")
Imagenes = Imagenes.reshape(124800, anchoImagen, largoImagen)
Etiquetas= Etiquetas.reshape(124800, 1)

print("Visualización de la imagen N.° 70000...")
from matplotlib import pyplot as plt
plt.imshow(Imagenes[70000])
plt.show()

print(Etiquetas[70000])

#En informática, los índices de las listas deben empezar por cero...")
Etiquetas = Etiquetas-1


print("Etiqueta de la imagen N.° 70000...")
print(Etiquetas[70000])