import cv2
from PIL import Image

image_path = 'catdog.jpg'

image = cv2.imread(image_path)


cat_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalcatface_extended.xml')
dog_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt.xml')

cat_face = cat_face_cascade.detectMultiScale(image)
dog_face = dog_face_cascade.detectMultiScale(image)

print(cat_face, dog_face)


cat = Image.open(image_path)

cat = cat.convert("RGBA")


for (x, y, width, height) in cat_face:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255, 1), 3)

for (x, y, width, height) in dog_face:
    cv2.rectangle(image, (x, y), (x+width, y+height), (255, 0, 0, 1), 3)

cv2.imshow("Cat", image)

cv2.waitKey()