import cv2
img = cv2.imread('1.jpg')
#加载图像属性
dimensions = img.shape
print("shape为", dimensions, "\n")
total_number_of_elements= img.size
print('size为', dimensions, "\n")
image_dtype = img.dtype
print('dtype为', dimensions, "\n")
#查找x=40，y=6处的像素点
(b, g, r) = img[6, 40]
print(b,g,r, "\n")
#某个区域像素
top_left_corner = img[0:50, 0:50]  # 获取图像的左上角50x50像素区域
cv2.imshow('original image', top_left_corner)  # 显示图像
#灰度图像
gray_img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)#指定图像以灰度模式加载
dimensions = gray_img.shape
print('灰度的size为', dimensions, "\n")
cv2.imshow('huidu', gray_img)
i = gray_img[6, 40]
print(i, '\n')
cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()  # 销毁所有窗口