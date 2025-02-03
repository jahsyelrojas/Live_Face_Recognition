import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_POP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_POP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_img = cv2.imread('reference.jpg')

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())["verified"]:
            face_match = True
        else:
            face_match = False
        
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()
    
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
            
        counter +=1
        if face_match:
            cv2.putText(frame, "MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
            
        else:
            cv2.putText(frame, "NO MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)
            
        cv2.imshow('video', frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
cv2.destroyAllWindows() 

    # The code above is a simple Python script that captures the video from the webcam and compares the face in the video with the reference image. 
    # The code uses the  DeepFace library to compare the faces. 
    # The code reads the reference image from the file system using the  cv2.imread()  function. 
    # The code then captures the video from the webcam using the  cv2.VideoCapture()  function. 
    # The code then reads the video frame by frame using the  cap.read()  function. 
    # The code then compares the face in the video frame with the reference image using the  DeepFace.verify()  function. 
    # The code then displays the video frame using the  cv2.imshow()  function. 
    # The code then waits for the user to press the “q” key to exit the program. 
    # The code then closes the video capture using the  cap.release()  function. 
    # The code then closes all the windows using the  cv2.destroyAllWindows()  function. 
    # The code above is a simple Python script that captures the video from the webcam and compares the face