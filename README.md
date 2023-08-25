# Face_Recognition_Attendance_System
## Description
This is a Face Recognition Attendance Web based application which detects and recognizes faces by comparing the encodings to the encodings of the input images and systematically prints the names and time of detection on the click of a button!

## Problem Statement
Attendance is an important part of daily classroom evaluation. At the beginning and ending of
class, it is usually checked by the teacher, but it may appear that a teacher may miss someone or some students answer multiple times or it may so be that the student is required to manually sign the sheet every time they attend a class. This includes more time being consumed by the students to find their name on the sheet, some students may sign another student’s name,by mistake or on purpose  or sometimes the sheet may get lost.
Face recognition-based attendance system is a problem of recognizing face for taking attendance by using face recognition technology based on highdefinition monitor video and other information technology.

## Working Of Model
The face recognition
system generally involves two stages:
* Face Detection – where the input image is searched to find any face, then image processing cleans up the facial image for easier recognition.
* Face Recognition – where the detected and processed face is compared to the database of known faces to decide who that person is.

Face recognition systems use computer algorithms to pick out specific, distinctive details about a person’s face. These details, such as distance between the eyes or shape of the chin, are then converted into a mathematical representation and compared to data on other faces collected in a face recognition database. The data about a particular face is often called a face template and is distinct from a photograph because it’s designed to only include certain details that can be used to distinguish one face from another.

![face points](https://user-images.githubusercontent.com/98026175/170861875-ddb7ab8a-4c16-4b34-8629-175eb2ee283f.jpeg)

![Face-recognition-structure-3-21](https://user-images.githubusercontent.com/98026175/170862407-6e1a6839-a17d-4018-a573-35625531ef5c.png)

![iowa_dot](https://user-images.githubusercontent.com/98026175/170862439-09b5f363-6d69-46f2-80b8-b26329864ddf.jpeg)

- STEP 1: importing libraries
- STEP 2: getting names of all images (filename)
- STEP 3: function for encoding images stored in folder
- STEP 4: getting live feed from camera and breaking it into smaller frames,then getting encodings for the faces visible on camera
- STEP 5: comparing encodings obtained from live feed to the encodings obtained from original images
- STEP 6: function to mark attendance in csv file

## UI of Web Application
![Screenshot 2022-05-29 at 11 42 12 AM](https://user-images.githubusercontent.com/98026175/170864455-d1ca33f4-5424-44f3-b359-297fc560c0b0.png)

![Screenshot 2022-05-29 at 11 57 46 AM](https://user-images.githubusercontent.com/98026175/170864486-ae15897b-c583-431e-a562-483bb7f0a988.png)

![Screenshot 2022-05-29 at 11 46 00 AM](https://user-images.githubusercontent.com/98026175/170865983-bb2b3b9c-e74f-4b50-bdd4-4712477292ba.png)

## Prerequisites
Libraries/Packages:

- OpenCV-python
- numpy
- face_recognition (requires installing dlib and cmake libraries)
- streamlit
- requests
- pandas
- pyttsx3 (text to speech)
- streamlit_lottie


All of these external libraries and packages are required in order to run my code. 
OpenCV will mainly be used for their face cascade, face detector and video capture.
face_recognition will be used for taking face encodings and face locations.
Streamlit library has been used for building the web page.


## Data Set

Considering a hypothetical situation where a few random celebrities are taking the same class!
I chose the images of a few famous celebrities and complied them into the images folder.

## Testing

![Screenshot 2022-05-29 at 4 22 26 PM](https://user-images.githubusercontent.com/98026175/170864496-78fe9b98-4619-4e3e-9a12-bc92e03f03d9.png)

![Screenshot 2022-05-29 at 4 40 36 PM](https://user-images.githubusercontent.com/98026175/170865038-fb59ce4b-46d8-4f15-94d1-7b279f15f8a2.png)

![Screenshot 2022-05-29 at 4 20 58 PM](https://user-images.githubusercontent.com/98026175/170864508-0f05399b-ea33-4426-be1e-ad9ad13384ce.png)

![Screenshot 2022-05-29 at 4 18 14 PM](https://user-images.githubusercontent.com/98026175/170864530-63a0fb0c-b610-43a9-9071-c04880dfe5a2.png)


**On the click of a button the attendance gets displayed**

![Screenshot 2022-05-29 at 4 24 01 PM](https://user-images.githubusercontent.com/98026175/170864591-7b6fff63-abc7-4375-96b2-8ed3b065d8d8.png)

Unfortunately I can't bring them to test my project,So I tested the code by showing images of the person through my live feed

## Executing Program
The following statement can be typed in the terminal for the web app to run on local host

`Facial_Recognition_System % streamlit run design.py`

##Demo Video
https://drive.google.com/file/d/14J_7qOjC1gZJ-6EBy58pnmkDJ1Omzq75/view?usp=sharing

## Acknowledgement
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

https://www.eff.org/pages/face-recognition#:~:text=Face%20recognition%20systems%20use%20computer,in%20a%20face%20recognition%20database.

