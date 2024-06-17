import cv2
import numpy as np

LOWER = np.array([145, 34, 22])
UPPER = np.array([152, 221, 255])


def get_contours(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

    #Filtering out colors
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER, UPPER)
    filtered = cv2.bitwise_and(img, img, mask=mask)
    blur = cv2.GaussianBlur(filtered, (5, 5), 0.5)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    #Create contours
    contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Create bounds
    bounds = [];
    h, w = img.shape[:2]
    for c in contours:
        left=w
        right=0
        top=h
        bottom=0;
        for p in c:
            p = p[0]
            x, y = p
            if x<left: left=x
            if x>right: right=x
            if y<top: top=y
            if y>bottom: bottom=y

        tl = [left, top]
        br = [right, bottom]
        bounds.append([tl, br])

    #cut out numbers
    nums = []
    for b in bounds:
        tl, br = b
        num = img[tl[1]:br[1], tl[0]:br[0]]
        nums.append(num)

    return nums

imgs = get_contours("../testImages/up03.webp")
num = 0
for im in imgs:
    cv2.imshow(str(num), im)
    num+=1

cv2.waitKey(0)


