import numpy as np
import cv2
import time
import math

img = np.zeros((700, 1200, 3), dtype = "uint8")
font = cv2.FONT_HERSHEY_SIMPLEX

v = 10
kat1 = 0; kat2 = 0; kat3 = 0
xP = 600; yP = 300

i = 0

x1 = 220;y1 = 300;
x2 = 300;y2 = 200;
x3 = 500;y3 = 450;


while(True):
    kat1 += 0.1; x1_v = v*math.cos(kat1); y1_v = v*math.sin(kat1); x1 += x1_v; y1 += y1_v
    kat2 += 0.2; x2_v = v*math.cos(kat2); y2_v = v*math.sin(kat2); x2 += x2_v; y2 += y2_v
    kat3 += 0.5; x3_v = v*math.cos(kat3); y3_v = v*math.sin(kat3); x3 += x3_v; y3 += y3_v

    #BOISKO
    cv2.rectangle(img,(100,50),(1100,550),(0,255,0),-1)
    cv2.rectangle(img,(100,250),(80,350),(0,0,255),3)
    cv2.rectangle(img,(1100,250),(1120,350),(0,0,255),3)
    cv2.line(img,(100,50),(1100,50),(255,255,255),3)
    cv2.line(img,(100,550),(1100,550),(255,255,255),3)
    cv2.line(img,(100,50),(100,550),(255,255,255),3)
    cv2.line(img,(1100,50),(1100,550),(255,255,255),3)
    cv2.line(img,(600,50),(600,550),(255,255,255),3)
    cv2.circle(img,(600,300), 50, (255,255,255), 3)

    #PIŁKARZ 1
    cv2.circle(img,(int(x1),int(y1)), 15, (0,255,255), -1)
    cv2.arrowedLine(img, (int(x1),int(y1)), (int(x1+3*x1_v),int(y1+3*y1_v)), (0,150,150), 4)
    cv2.putText(img,'1',(int(x1-10),int(y1+10)), font, 1,(0,0,0),2,cv2.LINE_AA)

    #PIŁKARZ 2
    cv2.circle(img,(int(x2),int(y2)), 15, (0,255,255), -1)
    cv2.arrowedLine(img, (int(x2), int(y2)), (int(x2 + 3*x2_v), int(y2 + 3*y2_v)), (0, 150, 150), 4)
    cv2.putText(img,'2',(int(x2-10),int(y2+10)), font, 1,(0,0,0),2,cv2.LINE_AA)

    #PIŁKARZ 3
    cv2.circle(img,(int(x3),int(y3)), 15, (0,255,255), -1)
    cv2.arrowedLine(img, (int(x3), int(y3)), (int(x3 + 3*x3_v), int(y3 + 3*y3_v)), (0, 150, 150), 4)
    cv2.putText(img,'3',(int(x3-10),int(y3+10)), font, 1,(0,0,0),2,cv2.LINE_AA)

    #PIŁKA
    cv2.circle(img, (xP, yP), 10, (255, 0, 0), -1)

    if(i<=20):
        xP += 20 - i
        i+= 1

    time.sleep(0.05)

    cv2.imshow('boicho', img)
    if (cv2.waitKey(1) & 0xFF == ord('x')):
        break

cv2.destroyAllWindows()
