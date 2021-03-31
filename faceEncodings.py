import cv2
import face_recognition as fr
import os
import sys
import numpy as np

def generate_dataset():
    img_path = 'dataset/img'
    images = []
    labels = []
    listpath = os.listdir(img_path)

    for lb in listpath:
        img = cv2.imread(os.path.join(img_path, lb))
        images.append(img)
        labels.append(os.path.splitext(lb)[0])
    
    images = np.array(images, dtype='object')
    np.save('dataset/labels', labels)
    
    encodeList = []
    for img in images:
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    
    encodeList = np.array(encodeList)
    np.save('dataset/encodeList', encodeList)
'''
def test():
    img_path = 'dataset/img'
    images = []
    labels = []
    listpath = os.listdir(img_path)

    for lb in listpath:
        img = cv2.imread(os.path.join(img_path, lb))
        images.append(img)
        labels.append(os.path.splitext(lb)[0])
    
    encodeList = []
    for img in images:
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList, labels
'''
def getencodes():
    labels = np.load('dataset/labels.npy')
    encodeList = np.load('dataset/encodeList.npy')
    return encodeList, labels

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if str(sys.argv[1]) == 'generate':
            generate_dataset()
    else:
        print('To generate dataset type: python faceEncodings.py generate')