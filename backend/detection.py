import cv2

cascade_path = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)


def face_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (3, 3), 0)

    faces = face_cascade.detectMultiScale(
        gauss, scaleFactor=1.05, minNeighbors=6, minSize=(200, 200))

    if (len(faces) != 1):
        return None
    return faces[0]
