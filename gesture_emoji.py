import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Gesture name -> label (we'll swap these for emoji images later)
LABELS = {
    "Thumb_Up": "THUMBS UP",
    "Thumb_Down": "THUMBS DOWN",
    "Victory": "PEACE",
    "Open_Palm": "HELLO",
    "Closed_Fist": "FIST",
    "Pointing_Up": "POINT UP",
    "ILoveYou": "I LOVE YOU",
}

base = python.BaseOptions(model_asset_path="gesture_recognizer.task")
options = vision.GestureRecognizerOptions(base_options=base)
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Gesture Detector", cv2.WINDOW_NORMAL)
fullscreen = False

while True:
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = recognizer.recognize(image)

    text = "No hand"
    if result.gestures:
        name = result.gestures[0][0].category_name
        text = LABELS.get(name, name)

    cv2.putText(frame, text, (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                1.5, (0, 255, 0), 3)
    cv2.imshow("Gesture Detector", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("f"):
        fullscreen = not fullscreen
        mode = cv2.WINDOW_FULLSCREEN if fullscreen else cv2.WINDOW_NORMAL
        cv2.setWindowProperty("Gesture Detector", cv2.WND_PROP_FULLSCREEN, mode)

cap.release()
cv2.destroyAllWindows()