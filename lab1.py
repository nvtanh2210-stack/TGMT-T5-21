import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = np.random.randint(0, 256, (768, 1024), dtype=np.uint8) # tạo ảnh ngẫu nhiên 1024x768
#cv=imshow('random image', img)
#key = cv.waitkey(0)
#if key == ord('q'):
    #cv.destroyAllWindows()

bimg = np.ones((768,1024,3), dtype=np.uint8)
bimg[:, :, 0] = 133
bimg[:,:,1] = 128
bimg[:,:,2] = 177 #blue -> Green -> red
#cv.line(bimg, (0,0), (1024,768), (0,0,255), 5 ) #RGB

cv.circle(bimg, (512,384), 350, (0,255,0), 40)

cv.putText(bimg, "VI", (500,750), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 4)
cv.putText(bimg, "III", (750,400), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 4)
cv.putText(bimg, "XII", (750,400), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 4)
cv.putText(bimg, "IX", (750,400), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 4)
#color = (123,125,128)
cv.imshow("one image", bimg)
cv.waitKey(0)
cv.destroyAllWindows()