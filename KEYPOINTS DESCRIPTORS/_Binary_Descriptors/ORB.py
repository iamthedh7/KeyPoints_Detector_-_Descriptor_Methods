import cv2
import os
os.system('cls')

def detect_corner(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()

    kp = orb.detect(gray, None)

    keypoint, des = orb.compute(gray, kp)

    img = cv2.drawKeypoints(gray, keypoint, img)

    return img, keypoint, des


img_big = cv2.imread('images\\book2.png')
out1, kp1, des1 = detect_corner(img_big)
cv2.imwrite('result\\ORB.jpg', out1)
cv2.imshow('result', out1)
cv2.waitKey()
cv2.destroyAllWindows()

print(len(kp1))

################## MATCHING ##################

"""img1 = cv2.imread('images\\book1.png')
img2 = cv2.imread('images\\book2.png')

out1, kp1, des1 = detect_corner(img1)
out2, kp2, des2 = detect_corner(img2)

#feature matching
bf = cv2.BFMatcher()

matches = bf.match(des1, des2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)
cv2.imwrite('result\\ORB_matches_50.jpg', img3)"""