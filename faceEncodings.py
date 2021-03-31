import cv2
import face_recognition as fr
import os
import sys
import numpy as np

def generate_dataset():
    img_path = 'dataset/img'
    images = []
    listpath = os.listdir(img_path)

    for lb in listpath:
        img = cv2.imread(os.path.join(img_path, lb))
        images.append(img)
    
    images = np.array(images, dtype='object')
    
    encodeList = []
    for img in images:
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    
    encodeList = np.array(encodeList)
    np.save('dataset/encodeList', encodeList)

def getencodes():
    encodeList = np.load('dataset/encodeList.npy')
    return encodeList

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if str(sys.argv[1]) == 'generate':
            print('Generating dataset...')
            generate_dataset()
            print("Completed...")
    else:
        print('To generate dataset type: python faceEncodings.py generate')