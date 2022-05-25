# -*- coding: utf-8 -*-
"""
Created on Thu May 12 00:12:22 2022

@author: User
"""

import cv2

cv2.namedWindow('showimg1')
cv2.namedWindow('showimg2') # 建立視窗

img1 = cv2.imread('media\\img01.jpg', 1) # 1 為預設，彩色模式讀取
img2 = cv2.imread('media\\img01.jpg', 0) # 0 為灰階模式讀取 # -1 原始照片讀取

cv2.imshow('showimg1', img1)
cv2.imshow('showimg2', img2)

cv2.waitKey(0)  #  0 毫秒後關閉視窗(案任意鍵關閉視窗)

cv2.destroyAllWindows() # 關閉所有的視窗

# ------------------------------------------------------

cv2.namedWindow("ShowImage")
image = cv2.imread("media\\img01.jpg", 0)
cv2.imshow("ShowImage", image)
cv2.imwrite("media\\img01copy1.jpg", image)   # 儲存檔案，預設jpg，品質的參數為95
cv2.imwrite("media\\img01copy2.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 9])  # 用PNG 儲存，壓縮比為9
# [ ] 可以儲存不同檔案格式的照片 # python特訓的程式碼是舊的

cv2.waitKey(0)
cv2.destroyWindow("ShowImage")
