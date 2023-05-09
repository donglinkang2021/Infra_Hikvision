import cv2

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

# 捕获视频流
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取视频流")
        break
    
    # 在窗口中显示图像
    cv2.imshow(window_name, frame)

    # 按下'q'键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源和关闭窗口
cap.release()
cv2.destroyAllWindows() 
