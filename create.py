# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Crear imagenes vacias
image_color = np.zeros((512, 512, 3), np.uint8)
image_gray = np.zeros((512, 512), np.uint8)

cv2.imshow('Nueva imagen a color', image_color)
cv2.imshow('Nueva imagen a blanco y negro', image_gray)

# Crear lineas
cv2.line(image_color, (0, 0), (511, 511), (0, 255, 255), 5)

# Crear rectangulo
cv2.rectangle(image_color, (100, 100), (300, 250), (255, 255, 0), 2)

# Crear circulo
cv2.circle(image_color, (256, 256), 100, (255, 0, 255), -1)

# Crear poligonos
points = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image_color, [points], True, (0, 0, 255), 3)

cv2.putText(image_color, 'Hello world', (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 0), 3)

cv2.imshow('Nueva imagen', image_color)

cv2.waitKey(0)
cv2.destroyAllWindows()