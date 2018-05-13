# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread('/home/will/Imágenes/140062-1.png')

# Dividir la imagen en planos individuales
B, G, R = cv2.split(image)

# Crea un array de valor ceros (0) de shape[:2] elementos
zeros = np.zeros(image.shape[:2], dtype = 'uint8')

# Imagen formada por union de B, zeros y zeros
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
# Imagen formada por union de zeros, G y zeros
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# Imagen formada por union de zeros, zeros y R
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))

cv2.waitKey(0)
cv2.destroyAllWindows()