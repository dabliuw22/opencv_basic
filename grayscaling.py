# -*- coding: utf-8 -*-
import cv2
import numpy

image = cv2.imread('/home/will/Imágenes/140062-1.png')
cv2.imshow('default', image)
cv2.waitKey()

# Convierte a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_image)
cv2.waitKey()

# Carga la imagen en escala de gris
two_gray_image = cv2.imread('/home/will/Imágenes/140062-1.png', 0)
cv2.imshow('gray_two', two_gray_image)
cv2.waitKey()
cv2.destroyAllWindows()