import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

# Tùy chỉnh cho các điểm quan trọng và đường nối
point_color = (44, 10, 15)  # Màu xanh lá
connection_color = (0, 250, 100)  # Màu đỏ
point_diameter = 2
line_thickness = 1

point_spec = mp.solutions.drawing_utils.DrawingSpec(color=point_color, thickness=point_diameter, circle_radius=point_diameter)
connection_spec = mp.solutions.drawing_utils.DrawingSpec(color=connection_color, thickness=line_thickness)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Chuyển đổi màu từ BGR sang RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Vẽ các điểm quan trọng của tay lên hình ảnh
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=point_spec,
                connection_drawing_spec=connection_spec)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):  # Nhấn ESC để thoát
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
