import cv2

# khởi tạo camera
cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
frameThickness = 2
frameColor = (0, 255, 0)
frameTopLeft = (450,100)
frameBottomRight = (frameTopLeft[0] + 450, frameTopLeft[1] + 450)

# thiết lập thông số video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# khởi tạo cửa sổ hiển thị video
cv2.namedWindow('video')

# quay video
while True:
    ret, frame = cap.read()

    # vẽ khung để chụp khuôn mặt
    cv2.rectangle(frame , frameTopLeft , frameBottomRight , frameColor , frameThickness)

    # hiển thị video
    cv2.imshow('video', frame)
    out.write(frame)

    # chụp khuôn mặt khi nhấn phím c
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # lưu hình ảnh
        croppedFrame = frame[frameTopLeft[1]:frameBottomRight[1] , frameTopLeft[0]:frameBottomRight[0]]
        cv2.imwrite("dataset/face.png", croppedFrame)
		#cv2.putText(croppedFrame, "Da hoan thanh", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # thoát khỏi vòng lặp khi nhấn phím q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# giải phóng camera và lưu video
cap.release()
out.release()

# đóng cửa sổ video
cv2.destroyAllWindows()
