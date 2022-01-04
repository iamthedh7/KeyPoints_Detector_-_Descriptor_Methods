import cv2
import numpy as np
import os
os.system('cls')

def detect_corner(image_path, threshold=100):
    """
    image_path: link to image
    blockSize: the size of neighbourhood considered for corner detection
    ksize: parameter of Sobel derivative
    k: Harris detector free parameter in the equation.
    """

    blockSize = 2
    ksize = 3
    k = 0.04

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    dest = cv2.cornerHarris(gray, blockSize, ksize, k)
    cv2.normalize(dest, dest, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    # Drawing a circle around corners
    for i in range(dest.shape[0]):
        for j in range(dest.shape[1]):
            if int(dest[i,j]) > threshold:
                cv2.circle(img, (j,i), 5, (255,0,0), 2)

    return img

while (True): 
    print('-- Enter a threshold value: ', end='')
    try:
        thresh = int(input())
        out = detect_corner('images\\langbac.jpg', threshold=thresh)
        cv2.imwrite('FloatingPoint_Descriptors\\result\\harris_threshold' + str(thresh) + '.jpg', out)
        cv2.imshow('result', out)
        cv2.waitKey()
        cv2.destroyAllWindows()
    except:
        break