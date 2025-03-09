import cv2

# Inisialisasi kamera
kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # Membaca frame dari kamera
    _, frame = kamera.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    # Titik pusat frame
    cx = int(width / 2)
    cy = int(height / 2)

    # Menandai titik pusat dengan lingkaran
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    # Mendapatkan nilai HSV dari titik pusat
    pixel_center = hsv_frame[cy, cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]

    # Menentukan warna berdasarkan nilai HSV
    color = "Tidak terdeteksi"
    if saturation < 50 and value > 200:
        color = "PUTIH"
    elif value < 50:
        color = "HITAM"
    elif hue < 5 or hue > 175:
        color = "MERAH"
    elif hue < 15:
        color = "ORANGE"
    elif hue < 25:
        color = "KUNING"
    elif hue < 85:
        color = "HIJAU"
    elif hue < 130:
        color = "BIRU"
    elif hue < 155:
        color = "UNGU"
    else:
        color = "MERAH"

    # Mendapatkan nilai BGR dari titik pusat
    pixel_center_bgr = frame[cy, cx]
    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])

    # Menentukan ukuran teks dan latar belakang
    text = f"Warna: {color}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5
    thickness = 5
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # Koordinat latar belakang teks
    padding = 10
    text_background = (
        cx - text_width // 2 - padding,
        cy + text_height + padding,
        cx + text_width // 2 + padding,
        cy - text_height - padding
    )

    # Menggambar latar belakang teks
    cv2.rectangle(frame, (text_background[0], text_background[1]), (text_background[2], text_background[3]), (0, 0, 0), -1)

    # Menampilkan teks
    cv2.putText(frame, text, (cx - text_width // 2, cy + text_height // 2), font, font_scale, (b, g, r), thickness)

    # Menampilkan frame
    cv2.imshow("Pengenalan Warna", frame)

    # Keluar dari loop jika tombol ESC ditekan
    key = cv2.waitKey(1)
    if key == 27:
        break

# Membersihkan resources
kamera.release()
cv2.destroyAllWindows()