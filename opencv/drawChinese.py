from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

frame = cv2.imread('./bg.jpg')

frame_cv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame_pil = Image.fromarray(frame_cv2)  #转为PIL的图片格式

draw = ImageDraw.Draw(frame_pil) 
font = ImageFont.truetype("FZYanSJW_Xian.ttf", 50, encoding="utf-8")
    # 第一个参数为字体，中文黑体
    # 第二个为字体大小
ImageDraw.Draw(frame_pil).text((100, 20), "谢小飞，新年快乐！！", (0, 0, 255), font)
frame_cv2 = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

cv2.imwrite('./new.jpg',frame_cv2)

