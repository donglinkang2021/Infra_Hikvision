
# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
MOTTO >>> STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

@ By: CaixyPromise
@ Date: 2021-10-17

"""
import cv2
from HandTrackingModule import HandDetector

class Main:
    def __init__(self):
        self.camera = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 以视频流传入
        self.camera.set(3, 1280) # 设置分辨率
        self.camera.set(4, 720)
        
    def Gesture_recognition(self):
        while True:
            self.detector = HandDetector()
            frame, img = self.camera.read()
            img = self.detector.findHands(img) # 找到你的手部
            lmList, bbox = self.detector.findPosition(img) # 获取你手部的方位
             
            cv2.imshow("camera", img)
            if cv2.getWindowProperty('camera', cv2.WND_PROP_VISIBLE) < 1:
                break
            # 通过关闭按钮退出程序
            cv2.waitKey(1)   
            # if cv2.waitKey(1) & 0xFF == ord("q"):
            #     break # 按下q退出
