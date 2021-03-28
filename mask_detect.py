from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

model=load_model('mobilenet_v2.model')

def mask_detect(frame):
    face=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    face=cv2.resize(face,(224,224))
    face = np.reshape(face, (1, 224, 224, 3))
    #face=img_to_array(face)
    #face=preprocess_input(face)
    
    return model.predict(face)