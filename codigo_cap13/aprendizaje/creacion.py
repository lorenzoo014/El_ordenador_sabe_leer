from __future__ import print_function
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from aprendizaje import anchoImagen,largoImagen,Imagenes,Etiquetas

#Creación de los conjutnos de aprendizaje y de prueba
imagenes_aprendizaje, imagenes_validacion, etiquetas_aprendizaje, etiquetas_validacion = train_test_split(Imagenes, Etiquetas, test_size=0.25, random_state=42)

#Adición de un tercer valor a nuestras tablas de imágenes para que puedan ser utilizadas por la red neuronal, especialmente el parámetro input_shape de la función Conv2D
imagenes_aprendizaje = imagenes_aprendizaje.reshape(imagenes_aprendizaje.shape[0], anchoImagen, largoImagen, 1)
print(imagenes_aprendizaje.shape)

imagenes_validacion = imagenes_validacion.reshape(imagenes_validacion.shape[0], anchoImagen, largoImagen, 1)

#Creación de una variable que sirve de imagen de trabajo a la red neuronal
imagenTrabajo = (anchoImagen, largoImagen, 1)

#Adaptación a la escala
imagenes_aprendizaje = imagenes_aprendizaje.astype('float32')/255
imagenes_validacion = imagenes_validacion.astype('float32')/255

# Creación de las categorías en un sistema de codificación One-Hot
cantidad_de_clases = 26
etiquetas_aprendizaje = keras.utils.to_categorical(etiquetas_aprendizaje, cantidad_de_clases)
etiquetas_validacion = keras.utils.to_categorical(etiquetas_validacion, cantidad_de_clases)