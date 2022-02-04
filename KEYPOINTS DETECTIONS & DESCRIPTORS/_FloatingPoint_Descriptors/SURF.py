import cv2
import os
os.system('cls')

def detect_corner(img, Hessian_threshold_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    surf = cv2.SURF_create(Hessian_threshold_value)

    keypoint, des = surf.detectAndCompute(gray, None)

    img = cv2.drawKeypoints(gray, keypoint, img)

    return img, keypoint, des


while (True): 
    try:
        print("   Set the Hessian thresh so that the number of keypoints on the image is ok. It's better to have a value 300-500")
        print('-- Enter a Hessian threshold value: ', end='')
        
        thresh = int(input())

        img_big = cv2.imread('images\\book1.png')
        out1, kp1, des1 = detect_corner(img_big, thresh)
        cv2.imwrite('result\\SUFT.jpg', out1)
        cv2.imshow('result', out1)
        cv2.waitKey()
        cv2.destroyAllWindows()

        print(len(kp1))
    except:
        break
    


################## MATCHING ##################

"""img1 = cv2.imread('images\\book1.png')
img2 = cv2.imread('images\\book2.png')

print("   Set the Hessian thresh so that the number of keypoints on the image is ok. It's better to have a value 300-500")
print('-- Enter a Hessian threshold value: ', end='')
thresh = int(input())
out1, kp1, des1 = detect_corner(img1, thresh)
out2, kp2, des2 = detect_corner(img2, thresh)

#feature matching
bf = cv2.BFMatcher()

matches = bf.match(des1, des2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)
cv2.imwrite('result\\SIFT_matches_50.jpg', img3)"""