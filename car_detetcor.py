# # -*- coding: utf-8 -*-
import time
import cv2
# print(cv2.__version__)

# cascade_src = 'cars.xml'
# video_src = 'v7.mp4'
# #video_src = 'dataset/video2.avi'

# cap = cv2.VideoCapture(video_src)
# car_cascade = cv2.CascadeClassifier(cascade_src)

# while True:
#     ret, img = cap.read()
#     if (type(img) == type(None)):
#         break
    
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     cars = car_cascade.detectMultiScale(gray, 1.1, 1)

#     for (x,y,w,h) in cars:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
#     cv2.imshow('video', img)
    
#     if cv2.waitKey(33) == 27:
#         break

# cv2.destroyAllWindows()




fire_cascade = cv2.CascadeClassifier('car.xml')
#fire_detection.xml file & this code should be in the same folder while running the code as no path is given

cap = cv2.VideoCapture("v7.mp4")



while 1:
    ret, img = cap.read()
    img=cv2.resize(img,(960,540))
    # cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, 1.2, 3)    
    #scale factor, which determines how much the image size is reduced at each image scale
    #minNeighbors, which determines how many neighbors each candidate rectangle should have to retain it. This is used to reduce false positives.
    
 
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        # if i==3:
        #     f_name="fire"+str(i)+".jpg"
        #     print("main")
        #     cv2.imwrite(f_name,img)
        #     url=upload_to_firestore("hackverse-5ecdd.appspot.com",f_name,f_name)
        #     details["image"]=url
        #     write_to_firestore("fire",details)
        #     print("done")

            
        #print(f_name)

        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]
        # edges = cv2.Canny(roi_gray, 100, 200)
        # roi_color[edges != 0] = (0, 255, 0)
        # print ('Fire is detected..!')
        # print (i)
        # i=i+1
        # ser1.write('p')
        time.sleep(0.2)
        
    cv2.imshow('fire_detector',img)
    # ser1.write('s')
    
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()