# import cv2
# import mediapipe as mp
# import time
# import numpy as np
# import Hand_Tracking_Module as HTM
# # wcam, hcam = 640, 480

# # cap = cv2.VideoCapture(0)
# # cap.set(3,wcam)
# # cap.set(4,hcam)
# # ptime = 0
# # while True:


# #     success, img = cap.read()

# #     ctime = time.time()
# #     fps = 1/(ctime-ptime)
# #     ptime = ctime
# #     cv2.putText(img,f'fps: {int(fps)}',(40, 70), cv2.FONT_HERSHEY_COMPLEX,
# #                 1, (255,0,0),3)
# #     cv2.imshow("img", img)
# #     cv2.waitKey(1)
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)  # Mở camera

# Tạo một hình ảnh mặt nạ để vẽ
canvas = None

# Lưu vị trí cũ của điểm cuối của ngón tay trỏ
x_prev, y_prev = 0, 0

    ret, frame = cap.read()
    if not ret:
        continue

    # Nếu mặt nạ chưa được khởi tạo, thiết lập nó với kích thước của khung hình
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Chuyển đổi màu từ BGR sang RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Lấy tọa độ của điểm cuối ngón tay trỏ và ngón cái
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            x_index, y_index = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])
            x_thumb, y_thumb = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])

            # Kiểm tra ngón tay trỏ và ngón cái có đóng lại với nhau không (khoảng cách nhỏ để vẽ)
            if abs(x_index - x_thumb) < 50 and abs(y_index - y_thumb) < 50:
                if x_prev == 0 and y_prev == 0:
                    x_prev, y_prev = x_index, y_index
                cv2.line(canvas, (x_prev, y_prev), (x_index, y_index), (255, 0, 0), 10)
            x_prev, y_prev = x_index, y_index

            # Vẽ đường dẫn tay trên khung hình
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Kết hợp khung hình với mặt nạ canvas
    frame = cv2.addWeighted(frame, 0.9, canvas, 0.1, 0)

    cv2.imshow('Hand Tracking - Drawing', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

x_prev, y_prev = 0, 0  # Reset lại vị trí trước khi thoát
cap.release()
cv2.destroyAllWindows()
