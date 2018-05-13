# -*- coding: utf-8 -*-

import cv2
import numpy

# Carga una imagen, se debe specificar el path.
image = cv2.imread("/home/will/Imágenes/140062-1.png")
# Crea una ventana con name 'frame' y muestra la imagen.
cv2.imshow('frame', image)
# Nos permite ingresar información cuando una ventana de imagen está abierta.
# Al dejarlo vacío, solo espera que se presione cualquier tecla antes de continuar.
# Al colocar números (excepto 0), podemos especificar un retraso por cuánto 
# tiempo mantiene la ventana abierta.
cv2.waitKey(10000)
# Esto cierra todas las ventanas abiertas.
# Si no lo coloca, su programa se bloqueará.
cv2.destroyAllWindows()
# Devuelve una tupla con height, width y el último valor significa que hay otros X 
# componentes (RGB) que componen esta imagen.
print(image.shape)