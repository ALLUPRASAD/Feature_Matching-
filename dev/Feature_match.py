import cv2
import matplotlib.pyplot as plt
import numpy as np
def template(image_path,label_path,output_imgname):
    image=cv2.imread(image_path)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    label=cv2.imread(label_path)
    label=cv2.cvtColor(label,cv2.COLOR_BGR2RGB)
    res=cv2.matchTemplate(image,label,cv2.TM_CCOEFF_NORMED)
    plt.imshow(image)
    plt.show()
    plt.imshow(label)
    plt.show()
    plt.imshow(res)
    cv2.imwrite('inter.png',res)
    plt.show()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left=max_loc
    height,width=label.shape[0],label.shape[1]
    bottom_right=(top_left[0]+width,top_left[1]+height)
    top_left,bottom_right
    re=cv2.rectangle(image,top_left,bottom_right,(255,0,0),10)
    re=cv2.cvtColor(re,cv2.COLOR_BGR2RGB)
    cv2.imwrite(output_imgname,re)
    plt.imshow(re)
    plt.show()
image_path='b.jpg'
label_path='a.jpg'
output_imgname='result.png'
template(image_path,label_path,output_imgname)
