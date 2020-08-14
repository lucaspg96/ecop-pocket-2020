import numpy as np
import cv2
import os
from time import sleep

import utils as ut

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    faces, gray_img = ut.face_detection(img)

    for face in faces:
        (x, y, w, h) = face

        print("Face identificada!\nPosicao: ({}, {})\tTamanho: ({}px, {}px)\n".format(
            x, y, w, h
        ))

        ut.draw_rect(img, face)
        ut.put_text(img, "Pessoa", x, y)

    resized_img = cv2.resize(img, (1000, 700))

    cv2.imshow('Video', resized_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
