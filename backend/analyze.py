from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, precision_score
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
import numpy as np
import os
import cv2
from compute import compute_ratios
import csv


classTypes = {
    'it': 1,
    'business': 2,
    'graphics': 3,
    'language': 4,
}

f = open('data.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Confidence', 'Friendliness', 'Tolerance', 'Sense of humour', 'Generosity', 'Leadership', 'Ambitious', 'Sensitive', 'Class'])

for path, subdirs, files in os.walk('dataset'):
    for name in files:
        cName = path.split('/')[-1]
        fullPath = os.path.join(path, name)
        img = cv2.imread(fullPath)
        ratios = compute_ratios(img)
        if ratios is None:
            print('Skip')
            continue
        ratios.append(classTypes[cName])
        writer.writerow(ratios)
        

