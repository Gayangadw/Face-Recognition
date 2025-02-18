import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime


image_paths = [
    'C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg',#gayanga
    'C:/Users/User/OneDrive/Pictures/Pictures/gayanga.jpg',#Gayanga
    'C:/Users/User/OneDrive/Pictures/Pictures/paniya.jpg'#paniya
]


images = []
classNames = []


for path in image_paths:
    curImg = cv2.imread(path)
    images.append(curImg)
    classNames.append(os.path.splitext(os.path.basename(path))[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList


encoded_face_train = findEncodings(images)


def markAttendance(name):
    directory = 'C:/Users/User/OneDrive/Documents'  
    filename = os.path.join(directory, 'Attendance.csv')
    
    
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.writelines('Name, Time, Date\n')
    
    with open(filename, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'\n{name}, {time}, {date}')


cap = cv2.VideoCapture(0)

try:
    while True:
        success, img = cap.read()
        if not success:
            break

        
        imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper().lower()
                y1, x2, y2, x1 = faceloc
                
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
        
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
