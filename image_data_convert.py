import cv2
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

image_dir = 'images'
data=[]
labels=[]
image_paths = os.listdir(image_dir)

for dirName in image_paths:
    dirPath = os.path.join(image_dir, dirName)
    images = os.listdir(dirPath)
    print(dirPath)
    print(images)
    for img in images:
        face = cv2.imread(os.path.join(dirPath, img))
        face = np.array(face)
        face = face.astype('float32')
        face /= 255
        data.append(face)
        labels.append(dirName)

data = np.array(data, dtype='float32')
labels = np.array(labels, dtype='str')

LE=LabelEncoder()
labels=LE.fit_transform(labels)

np.save('dataset/data.npy', data)
np.save('dataset/targe.npy', labels)