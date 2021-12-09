import numpy as np
import dlib
from sklearn.cluster import KMeans
from alignment import face_alignment
import pandas as pd
import pickle

shape_predictor = dlib.shape_predictor(
    "models/shape_predictor_68_face_landmarks.dat")

face_rectangle = dlib.rectangle(
    0, 0, 400, 400)


def get_top_forehead(face_img):
    forehead = face_img[0:100, 0:400]
    rows, cols, bands = forehead.shape
    X = forehead.reshape(rows*cols, bands)
    res = KMeans(n_clusters=2, init='k-means++', max_iter=300,
                 n_init=10, random_state=0).fit_predict(X)
    val = res[int(rows - 1) * cols + int(cols / 2)]

    for i in range(int(rows) - 1, 0, -1):
        if res[i * cols + int(cols / 2)] != val:
            return i
    return 0


def mean(arr):
    return sum(arr) / len(arr)


def compute_ratios(img):
    if img is None:
        return None
    face_img = face_alignment(img)
    if face_img is None:
        return None
    landmarks = np.matrix(
        [[p.x, p.y] for p in shape_predictor(face_img, face_rectangle).parts()])

    facial_width = landmarks[26, 0] - landmarks[17, 0]
    facial_height = landmarks[8, 1] - get_top_forehead(face_img)
    eye_eyeblow = min(landmarks[37, 1], landmarks[38, 1],
                      landmarks[43, 1], landmarks[44, 1]) - min(landmarks[18, 1], landmarks[19, 1], landmarks[20, 1],
                                                                landmarks[23, 1], landmarks[24, 1], landmarks[25, 1])
    eye_height = max(landmarks[40, 1], landmarks[41, 1],
                     landmarks[46, 1], landmarks[47, 1]) - min(landmarks[37, 1], landmarks[38, 1],
                                                               landmarks[43, 1], landmarks[44, 1])
    sum_eye_width = landmarks[39, 0] - landmarks[36,
                                                 0] + landmarks[45, 0] - landmarks[42, 0]
    eye_distance = landmarks[42, 0] - landmarks[39, 0]
    philtum = landmarks[52, 0] - landmarks[50, 0]

    upper_lip = mean([landmarks[61, 1], landmarks[62, 1],
                      landmarks[63, 1]]) - mean([landmarks[49, 1], landmarks[50, 1],
                                                 landmarks[52, 1], landmarks[53, 1]])

    lower_lip = mean([landmarks[56, 1], landmarks[57, 1],
                      landmarks[58, 1]]) - mean([landmarks[65, 1], landmarks[66, 1],
                                                 landmarks[67, 1]])
    cheek_cheek = landmarks[16, 0] - landmarks[0, 0]
    brow_upper_lip = landmarks[51, 1] - landmarks[27, 1]
    nose_width = landmarks[35, 0] - landmarks[31, 0]
    nose_height = landmarks[33, 1] - landmarks[27, 1]

    confidence = facial_width / facial_height
    friendliness = eye_eyeblow / eye_height
    patience = sum_eye_width / eye_distance
    sense_of_humour = philtum
    generosity = upper_lip + lower_lip
    leadership = cheek_cheek / brow_upper_lip
    ambitious = nose_width
    sensitive = nose_height

    return [confidence, friendliness, patience, sense_of_humour, generosity, leadership, ambitious, sensitive]


svc = pickle.load(open('model.pkl', 'rb'))


def predict(img):
    ratios = compute_ratios(img)
    if ratios is None:
        return None
    np_arr = np.array([ratios])
    df = pd.DataFrame(np_arr, columns=['Confidence', 'Friendliness', 'Tolerance',
                      'Sense of humour', 'Generosity', 'Leadership', 'Ambitious', 'Sensitive'])
    print(ratios)
    return svc.predict_proba(df)[0]
