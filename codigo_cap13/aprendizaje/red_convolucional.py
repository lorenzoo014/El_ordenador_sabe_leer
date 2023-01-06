from __future__ import print_function
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from aprendizaje import imagenTrabajo, cantidad_de_clases, imagenes_aprendizaje, imagenes_validacion, etiquetas_aprendizaje, etiquetas_validacion


def red_convolucional():
    # Red neuronal convolucional
    # 32 filtros de dimensiones 3x3 con una función de activación de tipo RELU
    # El filtro tiene en la entrada la imagen de trabajo
    redCNN = Sequential()
    redCNN.add(Conv2D(32, kernel_size=(3, 3),
                    activation='relu',
                    input_shape=imagenTrabajo))

    #Una segunda capa de 64 filtros de dimensión 3x3
    redCNN.add(Conv2D(64, (3, 3), activation='relu'))

    #Una función de pooling
    redCNN.add(MaxPooling2D(pool_size=(2, 2)))
    redCNN.add(Dropout(0.25))

    #Un aplanado
    redCNN.add(Flatten())

    #La red neuronal con 128 neuronas en la entrada
    #una función de activación de tipo ReLU
    redCNN.add(Dense(128, activation='relu'))
    redCNN.add(Dropout(0.5))

    #Una última capa de tipo softmax
    redCNN.add(Dense(cantidad_de_clases, activation='softmax'))

    #Compilación del modelo
    redCNN.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adadelta(),
                metrics=['accuracy'])


    # Aprendizaje con una fase de validación
    # en los conjuntos de prueba
    batch_size = 128
    epochs = 10

    redCNN.fit(imagenes_aprendizaje, etiquetas_aprendizaje,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1,
            validation_data=(imagenes_validacion, etiquetas_validacion))



    # Guardado del modelo
    redCNN.save('modelo/modelo_caso_practicov2.h5')

    # Evaluación de la precisión del modelo
    score = redCNN.evaluate(imagenes_validacion, etiquetas_validacion, verbose=0)
    print('Precisión en los datos datos de validación:', score[1])