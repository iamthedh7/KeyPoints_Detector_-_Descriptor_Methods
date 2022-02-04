import cv2
import os
os.system('cls')

def detect_corner(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    star = cv2.xfeatures2d.StarDetector_create()

    keypoint = star.detect(gray, None)

    img = cv2.drawKeypoints(gray, keypoint, img)

    keypoint2 = star.detect(gray, None)
    img2 = cv2.drawKeypoints(gray, keypoint2, img)

    return img, keypoint


img = cv2.imread('images\\lyly_big.jpg')
out1, kp1 = detect_corner(img)
cv2.imwrite('result\\STAR.jpg', out1)
cv2.imshow('result', out1)
cv2.waitKey()
cv2.destroyAllWindows()
print(len(kp1))
