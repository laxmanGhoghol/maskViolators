import cv2
from face_detect import face_extraction
import joblib
from sklearn.decomposition import PCA
import numpy as np

filename = 'finalized_model.pkl'
model = joblib.load(open(filename, 'rb'))

filenamepca = 'finalized_pca.pkl'
pca = joblib.load(open(filenamepca, 'rb'))

def recognize(frame):
    face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face, (64, 64))
    face = np.array(face)
    face = np.reshape(face, (1, 64*64))
    face = pca.transform(face)
    id = model.predict(face)
    
    return id

