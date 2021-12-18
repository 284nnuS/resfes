from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, confusion_matrix
import sys
import os
from compute import compute_ratios
import cv2
import pickle

bankdata = pd.read_csv("data.csv")

X = bankdata.drop('Class', axis=1)
Y = bankdata['Class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

img = cv2.imread('dataset/language/DA140042.jpg')

ratios = compute_ratios(img)
np_arr = np.array([ratios])
df = pd.DataFrame(np_arr, columns=['Confidence', 'Friendliness', 'Tolerance',
                'Sense of humour', 'Generosity', 'Leadership', 'Ambitious', 'Sensitive'])


clf = SVC(kernel = 'rbf', C=100, gamma = 0.001, probability = True).fit(X, Y)
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
p = precision_score(Y_test, Y_pred, average = 'micro')
print(p)
print(clf.predict_proba(df))
input("Press Enter to continue...")
pickle.dump(clf, open('new_model.pkl', 'wb'))
        
