
import numpy as np
import cv2
import time
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage
from google.oauth2 import service_account
from firebase_admin import credentials, storage





cred = credentials.Certificate("hackverse-5ecdd-firebase-adminsdk-ftdmd-308179e4be.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'hackverse-5ecdd.appspot.com'})



def write_to_firestore(colection_name: str, details: dict):
    # app = firebase_admin.initialize_app(cred)
    
    firestore_client = firestore.client()
    doc_ref = firestore_client.collection(colection_name).document()
    doc_ref.set(
        details
    )
    print("Document written with ID: ")



def upload_to_firestore(bucket_name, source_file_name, destination_blob_name):
    # cred = credentials.Certificate("hackverse-5ecdd-firebase-adminsdk-ftdmd-308179e4be.json")
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    # print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    blob.make_public()
    print(blob.public_url)

    return(blob.public_url)



details={
    "tittle": "Fire accident 2",
    "description": "A big building was fire",
    "intensity": "7",
   
    "location": { "latitude": 13.009267, "longitude": 74.795371},
    "imageurl":
      "https://bsmedia.business-standard.com/_media/bs/img/article/2022-05/13/full/1652462127-1638.jpg?im=Resize,width=480",
    #datetime: getCurrentDate(),
    "policehelp": True,
    "firehelp": True,
    "ambulancehelp": False,
    "otherhelp": False,
    "status": "NEW",
  }



# print(details)


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
#fire_detection.xml file & this code should be in the same folder while running the code as no path is given

cap = cv2.VideoCapture(0)
i=0
flag=0
 
while 1:
    ret, img = cap.read()
    img=cv2.resize(img,(960,540))
    # cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)    
    #scale factor, which determines how much the image size is reduced at each image scale
    #minNeighbors, which determines how many neighbors each candidate rectangle should have to retain it. This is used to reduce false positives.
    
 
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        if i==3:
            f_name="fire"+str(i)+".jpg"
            print("main")
            cv2.imwrite(f_name,img)
            url=upload_to_firestore("hackverse-5ecdd.appspot.com",f_name,f_name)
            details["imageurl"]=url
            write_to_firestore("fire",details)
            print("done")

            
        #print(f_name)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        edges = cv2.Canny(roi_gray, 100, 200)
        roi_color[edges != 0] = (0, 255, 0)
        # print ('Fire is detected..!')
        # print (i)
        i=i+1

        # ser1.write('p')
        time.sleep(0.2)
        
    cv2.imshow('fire_detector',img)
    # ser1.write('s')
    
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
