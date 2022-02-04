import cv2
import os
os.system('cls')

def detect_corner(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fast = cv2.FastFeatureDetector_create()

    keypoint = fast.detect(gray, None)

    img = cv2.drawKeypoints(gray, keypoint, img)

    """fast.setThreshold(20)
    fast.setType(20)""" # you can change more params here
    fast.setNonmaxSuppression(False)
    keypoint2 = fast.detect(gray, None)
    img2 = cv2.drawKeypoints(gray, keypoint2, img)

    return img, keypoint, img2, keypoint2


img = cv2.imread('images\\lyly_big.jpg')
## nonmaxSuppression
out1, kp1, _, _ = detect_corner(img)
cv2.imwrite('result\\FAST_nonmaxSuppression.jpg', out1)
cv2.imshow('result', out1)
cv2.waitKey()
cv2.destroyAllWindows()
print(len(kp1))
## without nonmaxSuppression
_, _, out2, kp2 = detect_corner(img)
cv2.imwrite('result\\FAST_without_nonmaxSuppression.jpg', out2)
cv2.imshow('result', out2)
cv2.waitKey()
cv2.destroyAllWindows()
print(len(kp2))


# Print all default params
fast = cv2.FastFeatureDetector_create()
print('DEFAULT PARAMS:')
print("+ threshold: {}".format(fast.getThreshold()))
print("+ nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
print("+ neighborhood: {}".format(fast.getType()))