import cv2

img = cv2.imread('source/person_dog.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# load face features
face_cascade = cv2.CascadeClassifier('data/lbpcascade_profileface.xml')
face_rect = face_cascade.detectMultiScale(gray, 1.1, 3)

print(f'Number of Faces: {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
