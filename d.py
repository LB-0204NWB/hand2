import cv2
import time
import mediapipe as mp


cap = cv2.VideoCapture(0)

prev_time = 0

while True:
    bin, frame = cap.read()

    frame_resize = cv2.resize(frame,(320,240))
    
    current_time = time.time()
    fps = 1/ (current_time - prev_time)
    prev_time = current_time
    
    fps_text = f"FPS {int(fps)}"

    cv2.putText(frame_resize,fps_text,(30,30),cv2.FONT_HERSHEY_PLAIN,0.5,(100,100,0),2)

    cv2.imshow('hand',frame_resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()