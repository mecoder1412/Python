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
    elif filter_type=="sobel":
        gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely=cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel=cv2.bitwise_or(sobelx.astype('uint8'),sobely.astype('uint8'))
        filtered_image=cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type=="canny edge":
            # Canny Edge Detection
            gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            edges=cv2.Canny(gray_image,100 ,200) 
            filtered_image=cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)    
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
    print("s-Sobel")
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
        elif key==ord('s'):
            filter_type="sobel"
        elif key==ord('c'):
            filter_type="canny edge"     
        elif key==ord('q'):
            print("Exiting...")   
            break 
        else:
            print("Invalid key") 
    cv2.destroyAllWindows()                    
