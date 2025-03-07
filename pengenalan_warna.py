import cv2
from numpy import pi

kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True :
    _, frame = kamera.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    cv2.circle(frame, (cx,cy), 5, (25,25,25), 0)

    pixel_center = hsv_frame[cy, cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]

    color = "Tidak terdeteksi"
    if hue == 0 | saturation == 0 :
        color = "PUTIH"
    elif hue < 10 :
        color = "ABU-ABU"
    elif hue < 15 :
        color = "MERAH"
    elif hue < 25 :
        color = "ORANGE"
    elif hue < 30 :
        color = "KUNING"
    elif hue < 50 :
        color = "HITAM"
    elif hue < 130 :
        color = "BIRU"
    elif hue < 155 :
        color = "UNGU"
    else :
        color = "MERAH"

    pixel_center_bgr = frame[cy,cx]

    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])

    print(pixel_center)
    cv2.putText(frame, color, (cx - 100, cy - 150), 0, 1.5, (b,g,r), 5)

    cv2.imshow("Pengenalan Warna", frame)
    key = cv2.waitKey(1)
    if key == 27 :
        break

kamera.release()
cv2.destroyAllWindows()