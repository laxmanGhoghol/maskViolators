import cv2
from face_detect import face_extraction
from mask_detect import mask_detect
import numpy as np 
from recognizer import recognize
import sys

img_path = ''
if len(sys.argv) > 1:
    img_path = sys.argv[1]
else:
    exit(0)

frame = cv2.imread(img_path)
faces, locs = face_extraction(frame)
for face, loc in zip(faces, locs):
    pred = mask_detect(face)
    (mask,withoutMask) = pred[0]
    (startX, startY, endX, endY) = loc
    if mask < withoutMask:
        id = recognize(face)
        name = ''
        if id == 0:
            name = 'Unknown'
        else:
            name = id
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(frame, f'Not Safe: {name}', (startX+1, startY-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)        
    else:
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(frame, 'Safe', (startX+1, startY-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Name', frame)
key = cv2.waitKey(5000)
cv2.destroyAllWindows()