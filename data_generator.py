import cv2
import os

video_stream = cv2.VideoCapture(0)

face_id = 0
os.system("mkdir train_images/{}".format(face_id))

for i in range(100):
    ret, frame = video_stream.read()
    # cv2.imshow("Test Frame", frame)
    cv2.imwrite("./train_images/{}/{}.jpg".format(face_id, i), frame)
