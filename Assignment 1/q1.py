import cv2
import numpy as np
import random
import math
import os
width = [1,3]
length = [7,15]
angles = [15,30,45,60,75,90,105,120,135,150,165,180]
colors = [(255,0,0),(0,0,255)]
imgdir = 1
for i in range(len(colors)):
    for j in range(len(angles)):
        for k in range(len(width)):
            for l in range(len(length)):
                x2 = int(length[l]*math.cos(angles[j]*(math.pi/180)))
                y2 = int(length[l]*math.sin(angles[j]*(math.pi/180)))
                no_imgs = 0
                path = os.getcwd()+"/" + "Data"+"/"+"Class" +str(imgdir)+"/"
                os.mkdir(path)
                while(no_imgs<1000):
                    x1=random.randint(0,28)
                    y1=random.randint(0,28)
                    x2 = int(length[l]*math.cos(angles[j]*(math.pi/180)))+x1
                    y2 = int(length[l]*math.sin(angles[j]*(math.pi/180)))+y1
                    if((x1<=(28-width[k]) and x2<=(28-width[k])) and (y1<=(28-width[k]) and y2<=(28-width[k])) and (x1>=width[j] and x2>=width[j] and y1>=width[j] and y2>=width[j])):
                        img = np.zeros((28,28,3), np.uint8)
                        cv2.line(img,(x1,y1),(x2,y2),colors[i],width[k])
                        img_name = str(l)+"_"+str(k)+"_"+str(j)+"_"+str(i)+"_"+str(no_imgs)+".jpg"
                        no_imgs +=1
                        cv2.imwrite(os.path.join(path,img_name),img)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                imgdir +=1        