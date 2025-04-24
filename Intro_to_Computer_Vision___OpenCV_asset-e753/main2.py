# grey scale image
import cv2
#Load image
image=cv2.imread('example.jpg')
#convert to grey scale
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#resize
resized_image=cv2.resize(gray_image,(224,224))
#Display resized grey scale image
cv2.imshow('Process Image',resized_image)
#Wait for a key press
key=cv2.waitKey(0)
#Check if "S" key was pressed(ASCII for "S" is 83)
if key==ord('s'):
    #Save the processed image when"S" is pressed
    cv2.imwrite('grayscale.jpg',resized_image)
    print("Image saved as grayscale.jpg")
else:
    print("Image not saved")
#Close the window
cv2.destroyAllWindows()
#Print processed image properties 
print(f"Processed Image Dimensions:{resized_image.shape}")      