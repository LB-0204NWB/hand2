import cv2
import time

# Mở camera
cap = cv2.VideoCapture(0)

# Kiểm tra camera có mở thành công không
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

prev_time = 0  # Lưu thời gian của khung hình trước đó

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể nhận được khung hình từ camera. Thoát...")
        break

    # Tính FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time
    
    # Chuyển đổi giá trị fps thành chuỗi để hiển thị
    fps_text = f"FPS: {int(fps)}"

    # Hiển thị FPS trên khung hình
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Hiển thị khung hình
    cv2.imshow('Camera', frame)
    print(current_time)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
