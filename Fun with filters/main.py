import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    #Apply specific color filter to image
    #Create a copy of the image to avoid modifying the original
    filtered_image=image.copy()
    if filter_type=="red_tint":
        #Remove green and blue for red tint
        filtered_image[:, :, 1]=0#Green channel to 0
        filtered_image[:, :, 0]=0#Blue channel to 0
    elif filter_type=="blue_tint":
        #Remove red and green for blue tint
        filtered_image[:, :, 1]=0#Green channel to 0
        filtered_image[:, :, 2]=0#Red channel to 0 
    elif filter_type=="green_tint":
        #Remove red and blue for red tint
        filtered_image[:, :, 2]=0#red channel to 0
        filtered_image[:, :, 0]=0#Blue channel to 0 
    elif filter_type=="increase_red":
        #increase the intensity of the red channel
        filtered_image[:, :, 2]=cv2.add(filtered_image[:, :, 2],50)#Increase red channel
    elif filter_type=="decrease_blue":
        #decrease the intensity of the blue channel
        filtered_image[:, :, 0]=cv2.subtract(filtered_image[:, :, 0],50)#Decrease blue channel
    elif filter_type=="canny edge":
            # Canny Edge Detection
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))
            edges = cv2.Canny(filtered_image, lower_thresh, upper_thresh)     
            return filtered_image
#Load the image
image_path='example.jpg'#Provide your image path
image=cv2.imread(image_path)  
if image is None:
    print("Error: Image not found!")
else:
    filter_type="original"#Default filter type
    print("Press the following keys to apply filters:") 
    print("r-Red Tint")  
    print("b-Blue Tint")
    print("g-Green Tint") 
    print("i-Increased Red intensity")
    print("d-Decreased Blue intensity")
    print("c-Canny Edge Detection") 
    print("q-Quit") 
    while True:
        #Apply the selected filter
        filtered_image=apply_color_filter(image,filter_type)
        #display the filtered image
        cv2.imshow("Filtered Image", filtered_image)
        #Wait for Key press
        key=cv2.waitKey(0) & 0xFF
        #Map key presses to filters
        if key==ord('r'):
            filter_type="red_tint" 
        elif key==ord('b'):
            filter_type="blue_tint" 
        elif key==ord('g'):
            filter_type="green_tint"
        elif key==ord('i'):
            filter_type="increase_red"
        elif key==ord('d'):
            filter_type="decrease_blue"
        elif key==ord('c'):
            filter_type="canny edge"     
        elif key==ord('q'):
            print("Exiting...")   
            break 
        else:
            print("Invalid key") 
    cv2.destroyAllWindows()                    
