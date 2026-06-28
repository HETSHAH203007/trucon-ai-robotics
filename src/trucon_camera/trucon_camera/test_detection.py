import cv2

FACE_CASCADE_PATH = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'

frame = cv2.imread('/tmp/test_face.jpg')
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, 'Face', (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

print(f'Faces detected: {len(faces)}')
cv2.imwrite('/tmp/detection_result.png', frame)
print('Saved to /tmp/detection_result.png')
