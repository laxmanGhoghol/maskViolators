import cv2
from face_detect import face_extraction
from mask_detect import mask_detect
import numpy as np 
from recognizer import recognize
from dbconn import insertInViolator,getUserName
cam = cv2.VideoCapture(0)

print('Starting application...')
while True:
    _, frame = cam.read()
    
    faces, locs = face_extraction(frame)
    for face, loc in zip(faces, locs):
        pred = mask_detect(face)
        (mask,withoutMask) = pred[0]
        (startX, startY, endX, endY) = loc

        if mask < withoutMask:
            id = recognize(face)
            name = ""
            if id != 0:
                name = getUserName(id)[0]
                print('Inserting data...')
                insertInViolator(id)
            else:
                name = "Unknown"
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(frame, f'Not Safe: {name}', (startX+1, startY-2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)        
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