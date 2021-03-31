import face_recognition as fr
import os
import numpy as np
import cv2

img_path = 'dataset/img'
images = []
labels = []
listpath = os.listdir(img_path)
for lb in listpath:
    img = cv2.imread(os.path.join(img_path, lb))
    images.append(img)
    labels.append(os.path.splitext(lb)[0])


def findencodings(images):
    encodeList = []
    for img in images:
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListknown = findencodings(images)


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    img = cv2.resize(frame, (255, 255))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = fr.face_locations(img)
    print(faces)
    encodeFrame = fr.face_encodings(img, faces)
    print(encodeFrame)
    
    for encodeface, loc in zip(encodeFrame, faces):
        matches = fr.compare_faces(encodeListknown, encodeface)
        print(matches)
        facedist = fr.face_distance(encodeListknown, encodeface)
        print(facedist)
        matchIndex = np.argmin(facedist)
        if matches[matchIndex]:
            name = labels[matchIndex]
            print(name)
            y1, x2, y2, x1 = loc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Name', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 13:
        break


print('Exiting ...')
cap.release()
cv2.destroyAllWindows()