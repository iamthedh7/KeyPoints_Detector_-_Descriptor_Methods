import cv2
import numpy as np
import os
os.system('cls')

def detect_corner(img, threshold=100):
    """
    image_path: link to image
    blockSize: the size of neighbourhood considered for corner detection
    ksize: parameter of Sobel derivative
    k: Harris detector free parameter in the equation.
    """

    blockSize = 2
    ksize = 3
    k = 0.04

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dest = cv2.cornerHarris(gray, blockSize, ksize, k)
    cv2.normalize(dest, dest, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    # Drawing a circle around corners
    kp = 0
    for i in range(dest.shape[0]):
        for j in range(dest.shape[1]):
            if int(dest[i,j]) > threshold:
                cv2.circle(img, (j,i), 5, (255,0,0), 2)
                kp += 1

    return img, kp

while (True): 
    print('-- Enter a threshold value: ', end='')
    try:
        thresh = int(input())
        img = cv2.imread('images\\lyly_big.jpg')

        img_rotate1 = cv2.rotate(img, rotateCode = cv2.ROTATE_90_CLOCKWISE)
        out1, kp1 = detect_corner(img_rotate1, threshold=thresh)
        cv2.imwrite('result\\harris_threshold' + str(thresh) + '_rotate1.jpg', out1)
        cv2.imshow('result', out1)
        cv2.waitKey()
        cv2.destroyAllWindows()

        img_rotate2 = cv2.rotate(img, rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE)
        out2, kp2 = detect_corner(img_rotate2, threshold=thresh)
        cv2.imwrite('result\\harris_threshold' + str(thresh) + '_rotate2.jpg', out2)
        cv2.imshow('result', out2)
        cv2.waitKey()
        cv2.destroyAllWindows()

        print(kp1)
        print(kp2)
    except:
        break