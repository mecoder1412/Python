import cv2
#Load pre-trained Haar Cascade Classifier for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#initialize video capyure(web cam)
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error:Could not open webcam.")
    exit()
while True:
    #Capture frame-by-frame
    ret,frame=cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    #Convert image into gray scale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    #Detect faces in the gray scale image
    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) 
    #Draw rectangle around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0), 2)
    #Display the count of faces
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,f'People Count:{len(faces)}',(10, 30), font, 1, (255,0,0), 2, cv2.LINE_AA)
    #Display the frame with face detection and people count
    cv2.imshow('Face Tracking and Counting', frame)  
    #exit the loop when the'q' key is pressed
    if cv2.waitKey(1) & 0xFF==ord('s'):
    #Save the processed image when"S" is pressed
     cv2.imwrite('image.jpg',frame)
     print("Image saved as grayscale.jpg")
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
#Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()    