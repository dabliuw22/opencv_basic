# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import cv2

image = cv2.imread('/home/will/Imágenes/140062-1.png', cv2.IMREAD_GRAYSCALE)

# Calcular histograma
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Label de ejes
plt.xlabel('X')
plt.ylabel('Y')

# Graficar el resultado
plt.plot(histogram, color = 'gray')
# Mostrar grafica
plt.show()

image_two = cv2.imread('/home/will/Imágenes/joker.jpg')
# Crea un histograma sin necesidad de usar calcHist
plt.hist(image_two.ravel(), 256, [0, 256])
plt.show()

image_trhee = cv2.imread('/home/will/Imágenes/140062-1.png')
color = ('b', 'g', 'r')

for i, col in enumerate(color):
	histogram_two = cv2.calcHist([image_trhee], [i], None, [256], [0, 256])
	plt.plot(histogram_two, color = col)
	plt.xlim([0, 256])
plt.show()
