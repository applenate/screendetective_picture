#遍历访问图片每个像素点，并修改相应的RGB
import cv2 as cv
import numpy as np

#从上到下4行色块：白 红 绿 蓝
#画布大小 1920*1080
def creat_image():
    img = np.zeros([1080, 1920, 3], np.uint8)   #创建纯黑色图片，将所有像素点的各通道数值赋0
    channels = img.shape[2]


    for row in range(1080):
        count = 1               #每行开始前，初始化
        lenth = 7
        delta = 0


        for col in range(1920):

            #判断填充颜色  [B,G,R]
            if row < 270:
                for c in range(channels):
                    img[row, col, c] += delta      #白色：每个通道值+delta值
                pass
            elif row < 540:
                img[row , col, 2] += delta    #红色 [0,0,1]
                pass
            elif row < 810:
                img[row , col, 1] += delta  #绿色 [0,1,0]
                pass
            elif row < 1080:
                img[row , col, 0] += delta  #蓝色 [1,0,0]

            #判断纵列阶梯
            count += 1               #判断下一个像素
            if count > lenth:
                if lenth == 7:
                    lenth = 8
                    pass

                elif lenth == 8:
                    lenth = 7

                delta += 1        #决定下一个阶梯的涂色色值
                count = 1      #开启新阶梯，重新计数



    print(img.shape)
    return img




img = creat_image()
cv.namedWindow("new_image")
cv.imshow("new_image",img)    #全部涂完，预览效果


cv.imwrite('pic_h.png',img,[int(cv.IMWRITE_PNG_COMPRESSION),0])  #png 0是最高质量，10是最低质量
cv.imwrite('pic_h.jpg',img,[int(cv.IMWRITE_JPEG_QUALITY),100]) #jpg 0是最低质量，100是最高质量

cv.waitKey(0)
cv.destroyAllWindows()

