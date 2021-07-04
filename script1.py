import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("elon.jpg")

res, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect the faces od different size in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    #to draw rectangle in face
    cv2.rectangle(img, (x,y), (x+w, y+h),(255, 255, 0),2)

cv2.imshow('img',img)
k = cv2.waitKey(0)
#Close the window
cap.release()
#Deallocate any associated memory usage
cv2.destroyAllWindows()
