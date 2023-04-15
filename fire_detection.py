
import numpy as np
import cv2
import time


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
#fire_detection.xml file & this code should be in the same folder while running the code as no path is given



cap = cv2.VideoCapture("v4.mp4")
while 1:
    ret, img = cap.read()
    img=cv2.resize(img,(960,540))
    # cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    
    
    #scale factor, which determines how much the image size is reduced at each image scale
    #minNeighbors, which determines how many neighbors each candidate rectangle should have to retain it. This is used to reduce false positives.
    
    i=0
    
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        f_name="fire"+str(i)+".jpg"
        cv2.imwrite(f_name,img)

        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]
        # edges = cv2.Canny(roi_gray, 100, 200)
        # roi_color[edges != 0] = (0, 255, 0)
        print ('Fire is detected..!')
        # ser1.write('p')
        time.sleep(0.2)
        i+=1
        
    cv2.imshow('fire_detector',img)
    # ser1.write('s')
    
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
