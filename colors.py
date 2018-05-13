# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread('/home/will/Imágenes/140062-1.png')
print(image.shape)
# Obtenemos los colores del pixel[0, 2]
B, G, R = image[0, 2]
print(B, G, R)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
print(gray_image[0, 2])

# Tamaño de la ventana igual al de la imagen
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
# Convierte a HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Mostrar imagen HSV
cv2.imshow('HSV', hsv_image)
# Mostrar imagen H
cv2.imshow('Hue', hsv_image[:, :, 0])
# Mostrar imagen S
cv2.imshow('Saturation', hsv_image[:, :, 1])
# Mostrar imagen V
cv2.imshow('Value', hsv_image[:, :, 2])

cv2.waitKey()

cv2.destroyAllWindows()