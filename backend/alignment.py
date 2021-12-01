import dlib
import cv2
import numpy as np
import math
from detection import face_detection


model_path = "./models/shape_predictor_5_face_landmarks.dat"

shape_predictor = dlib.shape_predictor(model_path)


def face_alignment(image, sizex=400, sizey=400):
    face = face_detection(image)
    if face is None:
        return None

    (x, y, w, h) = face

    face_rectangle = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))
    landmarks5 = np.matrix(
        [[p.x, p.y] for p in shape_predictor(image, face_rectangle).parts()])

    center = (float(landmarks5[4, 0]), float(landmarks5[4, 1]))
    angle = math.degrees(math.atan2(landmarks5[1, 1] - landmarks5[3, 1],
                                    landmarks5[1, 0] - landmarks5[3, 0]))

    if angle != 0.0:
        rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        # Rotated image
        image = cv2.warpAffine(
            image, rot_matrix, image.shape[1::-1], flags=cv2.INTER_LINEAR)

        face = face_detection(image)
        if face is None:
            return None

        (x, y, w, h) = face

        face_rectangle = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))

    face_img = image[y:y+h, x:x+w].copy()
    face_img = cv2.resize(face_img, (sizex, sizey),
                          interpolation=cv2.INTER_AREA)
    return face_img
