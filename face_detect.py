import os
import numpy as np
import cv2

prototxtPath = os.path.sep.join(['deploy.prototxt'])
weightsPath = os.path.sep.join(['res10_300x300_ssd_iter_140000.caffemodel'])
net = cv2.dnn.readNet(prototxtPath, weightsPath)

#function
def face_extraction(img):
    blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    (h, w) = img.shape[:2]
    faces = []
    locs = []

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
            face = img[startY: endY + 10, startX: endX + 10]
            faces.append(face)
            locs.append((startX, startY, endX, endY))
    
    return faces,locs
#end of function