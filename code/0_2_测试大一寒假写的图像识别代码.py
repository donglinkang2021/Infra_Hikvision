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
cap = cv2.VideoCapture(video_url)

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


kernel = np.ones((11, 11), np.uint8)
while (1):
    # 读取帧
    isFrame, frame = cap.read()
    h, w, _ = frame.shape
    # 转换颜色空间 BGR 到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 定义HSV中红色的范围
    lower_red = np.array([139, 13, 87])
    upper_red = np.array([155, 138, 255])
    # 设置HSV的阈值使得只取得所检测到的红色（粉红色，紫色？？？）
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # 将掩膜和图像逐像素相加
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)
    # 降噪
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # cv2.imshow('opening',opening)
    # 2.寻找轮廓
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_LIST, 2)
    num_cnt = len(contours)
    # 3.绘制轮廓
    img_draw = frame.copy()
    cv2.drawContours(img_draw, contours, -1, (0, 0, 255), 2)
    # 显示全部轮廓
    # cv2.imshow('findContours', img_draw)
    # 给最大轮廓划圈，圆心确定为中心点（但是误差还挺大的）
    list_radius = []
    for i in range(num_cnt):
        cnt = contours[i]
        t = (cv2.minEnclosingCircle(cnt))
        list_radius.append(t)
    list_radius.sort(key=operator.itemgetter(1))
    if list_radius == []:
        (x, y), radius = ((w / 2, h / 2), 10)
    else:
        (x, y), radius = list_radius[num_cnt - 1]
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img_draw, center, 1, color=(0, 0, 255), thickness=3)
    cv2.circle(img_draw, center, radius, (0, 255, 0), 2)
    cv2.imshow(window_name, img_draw)
    # 按下'q'键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
