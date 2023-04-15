
# import cv2
# import numpy as np
# import smtplib
# import playsound
# import threading

# Alarm_Status = False
# Email_Status = False
# Fire_Reported = 0

# def play_alarm_sound_function():
# 	while True:
# 		playsound.playsound('alarm-sound.mp3',True)
#         #  print("Alarm Sound")
# def send_mail_function():

#     recipientEmail = "Enter_Recipient_Email"
#     recipientEmail = recipientEmail.lower()

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login("Enter_Your_Email (System Email)", 'Enter_Your_Email_Password (System Email')
#         server.sendmail('Enter_Your_Email (System Email)', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
#         print("sent to {}".format(recipientEmail))
#         server.close()
#     except Exception as e:
#     	print(e)


# video = cv2.VideoCapture("v4.mp4") # If you want to use webcam use Index like 0,1.

# while True:
#     (grabbed, frame) = video.read()
#     if not grabbed:
#         break

#     frame = cv2.resize(frame, (960, 540))

#     blur = cv2.GaussianBlur(frame, (21, 21), 0)
#     hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#     lower = [18, 50, 50]
#     upper = [35, 255, 255]
#     lower = np.array(lower, dtype="uint8")
#     upper = np.array(upper, dtype="uint8")

#     mask = cv2.inRange(hsv, lower, upper)

#     output = cv2.bitwise_and(frame, hsv, mask=mask)

#     no_red = cv2.countNonZero(mask)

#     if int(no_red) > 15000:
#         Fire_Reported = Fire_Reported + 1

#     cv2.imshow("output", output)

#     if Fire_Reported >= 1:
#         if Alarm_Status == False:
#             threading.Thread(target=play_alarm_sound_function).start()
#             Alarm_Status = True

#         if Email_Status == False:
#             threading.Thread(target=send_mail_function).start()
#             Email_Status = True
    		 
#     # if Fire_Reported >= 1:
#     #     print("Fire Detected")


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
# video.release()





# import geocoder
# g = geocoder.ip('me')
# print(g.latlng)

# t = geocoder.freegeoip('99.240.181.199')
# print(t)




details={
    "tittle": "Fire accident",
    "description": "A big building got large fire",
    "intensity": "7",
   
    "location": { "latitude": 13.009267, "longitude": 74.795371},
    "image":
      "https://bsmedia.business-standard.com/_media/bs/img/article/2022-05/13/full/1652462127-1638.jpg?im=Resize,width=480",
    #datetime: getCurrentDate(),
    "policehelp": True,
    "firehelp": True,
    "ambulancehelp": False,
    "otherhelp": False,
    "imageurl": "",
    "status": "NEW",
  }



details["image"]="hello"
print(details)
