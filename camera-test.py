import cv2

cap = cv2.VideoCapture(0)  # 0 = default laptop camera

while True:
    ok, frame = cap.read()
    if not ok:
        print("Cannot read from camera")
        break
    frame = cv2.flip(frame, 2)  # mirror view
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press q to quit
        break

cap.release()
cv2.destroyAllWindows()