import cv2
import numpy as np
import os
from dbconn import insertUser, getLastId

name = ""
datapath = "dataset/img"
cap = cv2.VideoCapture(0)

while True:

    print("Enter User Name: ")
    name = input()
    if len(name) < 4 or len(name) > 30 or not name.isalnum():
        print("Please enter valid user name. user-name must not contain special chararcters. Max 30 chararcters and Min 4.")
    else:
        break
count = getLastId()[0] + 1
while True:
    _, frame = cap.read()
    cv2.imshow("Image", frame)
    choice = input('Save this image? (y/n)')
    key = cv2.waitKey(1) & 0xFF
    if choice == 'y':
        imgpath = datapath + "/" + str(count) + ".jpg" #path to save face
        cv2.imwrite(imgpath, frame)
        print(f"Image {count} is saved.")
        break
    else:
        print('Taking New image...')

print('Inserting in database')
insertUser(name, count)
cap.release()
cv2.destroyAllWindows()

