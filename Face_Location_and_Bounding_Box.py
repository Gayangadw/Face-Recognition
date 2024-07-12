import cv2
import face_recognition

imgphoto_bgr = face_recognition.load_image_file('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')
imgphoto_rgb = cv2.cvtColor(imgphoto_bgr,cv2.COLOR_BGR2RGB)
# cv2.imshow('bgr', imgphoto_bgr)
# cv2.imshow('rgb', imgphoto_rgb)
# cv2.waitKey(0)



imgphoto =face_recognition.load_image_file('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')
imgphoto = cv2.cvtColor(imgphoto,cv2.COLOR_BGR2RGB)
#----------Finding face Location for drawing bounding boxes-------
face = face_recognition.face_locations(imgphoto_rgb)[0]
copy = imgphoto.copy()
#-------------------Drawing the Rectangle-------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
cv2.imshow('copy', copy)
cv2.imshow('elon',imgphoto)
cv2.waitKey(0)