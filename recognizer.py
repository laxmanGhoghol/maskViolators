from faceEncodings import getencodes
import face_recognition as fr
import cv2
import os
import numpy as np

encodedfacesknown = getencodes()

def recognize(face):
    name = -1
    try:

        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        encodeface = fr.face_encodings(face)
        facedist = fr.face_distance(encodedfacesknown, encodeface[0])
        matches = fr.compare_faces(encodedfacesknown, encodeface[0])
        matchIndex = np.argmin(facedist)
        if matches[matchIndex]:
            name = matchIndex
    except:
        print("Error recognizing face...")
    if name == -1:
        return 0
    else:
        return name+1