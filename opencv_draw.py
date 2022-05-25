import cv2, numpy

cv2.namedWindow("plot")  # 建立視窗 # 注意cv2 的顏色是 BGR!!
image = cv2.imread("media\\background.jpg")

cv2.line(image, (50,50), (300,300), (255,0,0), 2) # 相片, 座標1, 座標2, 顏色, 寬度

cv2.rectangle(image, (500,20), (580,100), (0,255,0), 3)
cv2.rectangle(image, (100,300), (150,360), (0,0,255), -1)  # 如果寬度為負，代表實心矩形

cv2.circle(image, (500,300), 40, (255,255,0), -1) # 相片, 圓心座標, 半徑, 顏色, 寬度

# 多邊形，這裡示範三角形
pts = numpy.array([[300,300],[300,340],[350,320]], numpy.int32)
cv2.polylines(image, [pts], True, (0,255,255), 2) # [pts]放在list裡  # True 代表封閉多邊形 

cv2.putText(image,"Hello Kaly.jpg", (350,420), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
# (照片, 文字, 位置, 字體, 字體大小, 顏色, 文字大小)

cv2.imshow("plot", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()