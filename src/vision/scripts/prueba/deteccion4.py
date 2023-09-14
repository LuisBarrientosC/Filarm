#!/usr/bin/env python

import cv2

#decodigo.com

# https://github.com/opencv/opencv/tree/master/data/haarcascades
# leer el archivo cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Captura el video
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240);
cap.set(cv2.CAP_PROP_FPS, 10);

while True:
    # Lee el frame
    _, img = cap.read()
    # Se convierte a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detectando rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Se muestra en la ventana
    cv2.imshow('img', img)
    # Para si la tecla 'Esc' es presionada
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Se libera el objeto de captura

cap.release()