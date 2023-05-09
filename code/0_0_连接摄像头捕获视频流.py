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


# 捕获视频流
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取视频流")
        break
    
    # 设置窗口名称
    window_name = 'Hikvision Camera'
    # 创建一个自定义窗口
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    # 在窗口中显示图像
    cv2.imshow(window_name, frame)

    # 按下'q'键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break