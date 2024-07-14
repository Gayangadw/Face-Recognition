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