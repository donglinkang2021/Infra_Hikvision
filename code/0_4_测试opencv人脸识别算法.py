import cv2
import operator
import numpy as np

# Hikvision摄像头连接参数
IP_ADDRESS = "192.168.1.19"  # 摄像头IP地址
PORT = 554  # RTSP端口号
USERNAME = "admin"  # 登录用户名
PASSWORD = "abcd1234"  # 登录密码

# 创建VideoCapture对象，连接摄像头
video_url = f"rtsp://{USERNAME}:{PASSWORD}@{IP_ADDRESS}:{PORT}/Streaming/Channels/1"
cap = cv2.VideoCapture(0) # 0表示打开默认摄像头(笔记本电脑自带摄像头)

# 检查摄像头连接是否成功
if not cap.isOpened():
    print("无法连接摄像头")
else:
    print("成功连接摄像头")

# 设置窗口名称
window_name = 'Hikvision Camera'
# 创建一个自定义窗口
scale = 0.5
origin_width = 1920
origin_height = 1080
window_width = int(origin_width*scale)
window_height = int(origin_height*scale)
begin_x = int(origin_width/2 - window_width/2)
begin_y = int(origin_height/2 - window_height/2)
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, window_width, window_height)
cv2.moveWindow(window_name, begin_x, begin_y)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# 人脸识别分类器 这里是opencv2自带的分类器
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # 检测眼睛
        # roi_gray = gray[y:y+h,x:x+w]
        # roi_color = frame[y:y+h,x:x+w]
        # eyes = eyeCascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    
    cv2.imshow(window_name,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
