# importing libraries
import cv2
import numpy as np
import os
import face_recognition as face_rec
from datetime import datetime

# Functions

# finding the encodings for the images
def encd(image):
    encd_list = []  # empty list to store all encodings
    # loop to get encodings of all images
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # correcting colour of image just in case
        encd_img = face_rec.face_encodings(img)[0]
        encd_list.append(encd_img)
    return encd_list


# mark attendance
def st_attendance(name):
    with open('student_attendance.csv', 'r+') as m:
        myList = m.readlines()
        namelist = []
        for line in myList:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            m.writelines(f'\n{name}, {time}')


# STEP 1 : getting names of all images
path = 'images'      # folder where all images are stored
# creating empty lists for student images and names
st_img = []
st_name = []
comp_list = os.listdir(path)     # extracting names of all students
# print(comp_list)  # gets printed as name.jpeg

# using for loop to store all the images in name of each person
for name in comp_list:
    newImg = cv2.imread(f'{path}/{name}')
    st_img.append(newImg)
    st_name.append(os.path.splitext(name)[0])       # removing .jpeg from the image name

# STEP 2 : encoding images
encodings = encd(st_img)   # calling function to encode images
# print('complete')    # check post

# STEP 3 : matching the image with face in frame
# getting live feed from camera
vid = cv2.VideoCapture(0)

while True:
    # breaking live feed into frames to process each frame
    success, orig_frame = vid.read()
    new_frame = cv2.resize(orig_frame, (0, 0), None, 0.2, 0.2)         # resizing(making small) frame for faster running
    new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2RGB)             # correcting colour just in case
    all_faces = face_rec.face_locations(new_frame)                     # for detecting all faces in the frame(can be more than one)
    encd_faces = face_rec.face_encodings(new_frame, all_faces)         # encode all faces

    # comparing encodings obtained from live feed to the encodings obtained from original images
    for face_encodings, face_locatn in zip(encd_faces, all_faces):
        compare = face_rec.compare_faces(encodings, face_encodings)
        dist = face_rec.face_distance(encodings, face_encodings)        # finding distance(minimum)
        correct_face = np.argmin(dist)

        if compare[correct_face]:
            current_name = st_name[correct_face].upper()

            # creating bounding box around face
            y1, x2, y2, x1 = face_locatn
            y1, x2, y2, x1 = y1 * 5, x2 * 5, y2 * 5, x1 * 5
            cv2.rectangle(orig_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(orig_frame, (x1, y2 - 30), (x2, y2), (0, 0, 255), cv2.FILLED)  # bottom line
            cv2.putText(orig_frame, current_name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # name

            # STEP 4 : marking attendance
            st_attendance(current_name)        # calling function to print names and time in .csv file

    cv2.imshow('Webcam', orig_frame)
    cv2.waitKey(1)
