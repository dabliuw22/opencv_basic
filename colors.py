# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread('/home/will/Imágenes/fondo_gnome.jpg')
print(image.shape)
B, G, R = image[0, 2]
print(B, G, R)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
print(gray_image[0, 2])

cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv_image)
cv2.imshow('Hue', hsv_image[:, :, 0])
cv2.imshow('Saturation', hsv_image[:, :, 1])
cv2.imshow('Value', hsv_image[:, :, 2])
cv2.waitKey()

cv2.destroyAllWindows()