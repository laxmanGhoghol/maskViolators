import cv2
import numpy as np
import os
from face_detect import face_extraction

cap = cv2.VideoCapture(0)
count = 1
name = ""
pdir = "images/"


#For getting correct user name
while True:
    print("Enter User Name: ")
    name = input()
    if not name.isalpha():
        print("Please enter only alphabetic character for your name!")
    else:
        dir_list = os.listdir(pdir)
        dir_found = False
        for dir in dir_list:
            if name == dir:
                print('Folder with same name/id exist. Try other user name. ')
                break
        if dir_found:
            break

#user name funtion end here

path = os.path.join(pdir, name)
os.mkdir(path)
print("Camera Recording started.")
list_str_looks = ['Look slightly left', 'Look slightly right', 'Smile lightly', 'Look Neutral', 'smile fully']
while True:
    _, frame = cap.read()
    faces, locs = face_extraction(frame)
    if not faces or not locs:
        print("Not detected face")
        continue
    face = faces[0]
    loc = locs[0]
    (startX, startY, endX, endY) = loc

    imgpath = pdir + name + "/" + str(count) + ".jpg" #path to save face
    face = cv2.resize(face, (64, 64)) #shrink face
    cv2.imwrite(imgpath, face) # save face
    print(f"Image {count} is saved.") 
    
    cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
    cv2.imshow("Collecting face data", frame)
 
    user_conf_str = "n"
    print(list_str_looks[(count % 5)])
    while user_conf_str != 'y':
        user_conf_str = input('Are you ready? (y/n)')
    
    count += 1 #increase saved face count

    if cv2.waitKey(1) == 13 or count >= 11: #stop if count is 10. we only need 10 pictures of each person
        break

cap.release()
cv2.destroyAllWindows()
print("########## Completed #############")
