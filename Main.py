import face_recognition
import cv2
import numpy as np
import csv
import os
import glob
from datetime import datetime
# import xlsxwriter as xl

video_capture=cv2.VideoCapture(0)

# job_image=face_recognition.load_image_file('7.jpg')
# jops_encoding=face_recognition.face_encodings(job_image)[0]

nithin_image=face_recognition.load_image_file('7.jpg')
nithin_encoding=face_recognition.face_encodings (nithin_image)[0]

known_face_encding=[nithin_encoding]
known_face_names=["Nithin"]

student=known_face_names.copy()
face_location=[]
face_enconding=[]
face_names=[]
s=True

now= datetime.now()
current_date=now.strftime("%Y-%m-%d")

#f=open(current_date+'.csv','w+',newline='')
#lnwriter=csv.writer(f)
n=0
while True:
    # workbook=xl.Workbook("time.xlsx")
    # worksheet=workbook.add_worksheet('sheet1')
    __,frame=video_capture.read()
    small_frame= cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame= small_frame[:,:,::-1]
    if s:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encondings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encondings:
            matchs= face_recognition.compare_faces(known_face_encding,face_encoding)
            name=''
            face_distance=face_recognition.face_distance(known_face_encding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matchs[best_match_index]:
                name=known_face_names[best_match_index]
            face_names.append(name)
            
            if name in known_face_names:
                print(student)
                # worksheet.write(n,0,student[1])
                # #student.remove(name)
                # workbook.close()
                # current_time=now.strftime("%H-%M-%S")
                #lnwriter.writerow([name,current_time])
        
    cv2.imshow("attendance",(frame))
    if cv2.waitKey(1) & 0xFF==('q'):
        break
    n=n+1
video_capture.release()
cv2.destroyAllWindows()


