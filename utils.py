import numpy as np
import cv2
import os

face_haar = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


def face_detection(img):
    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_haar.detectMultiScale(img,
                                       scaleFactor=1.3,
                                       minNeighbors=3)
    return faces, gray_scale_img


def load_training_data(directory):
    faces = []
    faces_ids = []

    for path, subdirnames, filenames in os.walk(directory):
        for file in filenames:
            if file.startswith("."):
                print("Skipping system file: "+file)
                continue

            face_id = os.path.basename(path)
            img_path = os.path.join(path, file)

            img = cv2.imread(img_path)
            if img is None:
                print("File not load properly: {} . Skipping...".format(img_path))
                continue

            # TODO: identificar a face da foto
            # DICA: usar a funcao face_detection

    return faces, np.array(faces_ids)


def train_classifier(faces, ids):
    # TODO: treinar um modelo LBPHFaceRecognizer
    model = None
    return model


def draw_rect(img, rect):
    (x, y, w, h) = rect
    return cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)


def put_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_DUPLEX,
                1, (255, 255, 255), 1)

# (faces, ids) = load_training_data("train_images/captures")

# print(len(faces), len(ids))
