import matplotlib.pyplot as plt
import numpy as np
import cv2
import math


# =========================


# =========================
# 3. ẢNH 1024x768 PIXEL NGẪU NHIÊN
# =========================
width = 1024
height = 768

random_img = np.ones((height, width, 3), dtype=np.uint8) * 255

# =========================
# 4. VẼ ĐƯỜNG CHÉO MÀU ĐỎ
# =========================
cv2.line(random_img, (0, 0), (width, height), (0, 0, 255), 3)

# =========================
# 5. VẼ CHỮ SỐ LA MÃ I → XII (DẠNG ĐỒNG HỒ)
# =========================
roman_numbers = ["XII", "I", "II", "III", "IV", "V",
                 "VI", "VII", "VIII", "IX", "X", "XI"]

center_x = width // 2
center_y = height // 2
radius = 300
border_radius = radius + 40

cv2.circle(random_img, (center_x, center_y), border_radius, (255,255,255), 4)

for i, text in enumerate(roman_numbers):
    angle = math.radians(i * 30 - 90)
    x = int(center_x + radius * math.cos(angle))
    y = int(center_y + radius * math.sin(angle))

for i, text in enumerate(roman_numbers):
    angle = math.radians(i * 30 - 90)
    x = int(center_x + radius * math.cos(angle))
    y = int(center_y + radius * math.sin(angle))

    cv2.putText(
    random_img,
    text,
    (x - 20, y + 10),
    cv2.FONT_HERSHEY_SIMPLEX,
   0.8,
    (0, 0, 10),   # chữ đen
    2,
    cv2.LINE_AA
    )



# =========================
# 6. HIỂN THỊ & LƯU ẢNH
# =========================
cv2.imshow('Clock Roman Image', random_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('dong_ho_la_ma_opencv.png', random_img)
