import cv2
from face_recog import recognize
from face_detect import face_extraction
from mask_detect import mask_detect
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    
    faces, locs = face_extraction(frame)
    for face, loc in zip(faces, locs):
        pred = mask_detect(face)
        (mask,withoutMask) = pred[0]
        print('mask') if mask > withoutMask else print('Without Mask')
        (startX, startY, endX, endY) = loc

        if mask < withoutMask:
            id = recognize(face)
            cv2.putText(frame, f'Not safe: {id}', (startX+1, startY-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, 'Safe', (startX+1, startY-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    

    cv2.imshow('Name', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 13:
        break


print('Exiting ...')
cam.release()
cv2.destroyAllWindows()