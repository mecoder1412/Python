import cv2
#Load cascade classifier for face detecting
fc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#Start video capture from defualt webcam(0)
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camerea.")
    exit()
while True:
    #Capture frame by frame
    ret, frame=cap.read()
    #if frame is read correctly, ret will be true
    if not ret:
        print("Error: Failed to capture image") 
        break
    #Convert frame to gray scale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    #Detect faces in the grayscale image
    faces=fc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30,30))
    #Draw rectangle around faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (200,200),(255,0,0),2)#Blue rectangle with thickness of 2
    #Display the result frame
    cv2.imshow('Face Detection-Press q to Quit',frame)
    #Break the loopwhen the'q' is pressed
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
#Release the capture and close any open windows
cap.release()        
cv2.destroyAllWindows()