import cv2
import time

cap =  cv2.VideoCapture(0)

while True:
    ret, fame = cap.read()
    
    fame_rezi = cv2.resize(fame,(320,240))
    cv2.imshow('camera', fame_rezi)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Đợi 1 ms, và kiểm tra xem có nhấn phím 'q' để thoát không
        break


cap.release()
cv2.destroyAllWindows()
