import cv2

cv2.namedWindow("frame")
cap = cv2.VideoCapture(0)  # 0 第一台攝影機

while(cap.isOpened()): # 傳回true代表有抓到攝影機
    ret, img = cap.read()  # ret 布林值，是否有成功抓到照片
    if ret == True:
        cv2.imshow("frame", img)
        k = cv2.waitKey(10000)  # 等10秒
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("media\\catch.jpg", img)
            break
cap.release()
cv2.destroyWindow("frame")
