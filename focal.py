import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('focal.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    print(w)
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    focal = 107 * 15 / 60
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(dst), (x, y-10), font, 1, (0, 0, 200), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
