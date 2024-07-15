import cv2
#通道顺序
img_OpenCV = cv2.imread('1.jpg')
#分成三个通道
b, g, r = cv2.split(img_OpenCV)
#合并通道（改变顺序为rgb)
img_matplotlib = cv2.merge([r, g, b])
from matplotlib import pyplot as plt
#matplotlib绘制顺序rgb
# plt.subplot(121)
# plt.imshow(img_OpenCV)#原图
# plt.subplot(122)
# plt.imshow(img_matplotlib)
# plt.show()
#opencv绘制顺序bgr
# cv2.imshow('bgr image', img_OpenCV)
# cv2.imshow('rgb image', img_matplotlib)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#转换
img_matplotlib = img_OpenCV[:, :, ::-1]

