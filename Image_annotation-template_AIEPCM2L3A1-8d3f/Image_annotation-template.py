import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image=cv2.imread('example.jpg') # User-provided image path

# Convert BGR to RGB for correct color display with matplotlib
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Get image dimensions
h,w,_=image_rgb.shape
# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rec1_w,rec1_h=150,150
top_left1=(20,20)  # Fixed 20 pixels padding from top-left
bottom_right1=(top_left1[0]+rec1_w, top_left1[1]+rec1_h)
cv2.rectangle(image_rgb, top_left1,bottom_right1,(0,255,255),3)# Yellow rectangle

# Rectangle 2: Bottom-right corner
rec2_w,rec2_h=200,150
top_left2=(w-rec2_w-20,h-rec2_h-20)# 20 pixels padding 
bottom_right2=(top_left2[0]+rec2_w,top_left2[1]+rec2_h) 
cv2.rectangle(image_rgb,top_left2,bottom_right2,(255,0,255),3)  # Magenta rectangle

# Step 3: Draw Circles at the Centers of Both Rectangles
c1x=top_left1[0]+rec1_w//2
c1y=top_left1[1]+rec1_h//2
c2x=top_left2[0]+rec1_w//2
c2y=top_left2[1]+rec1_h//2
cv2.circle(image_rgb,(c1x,c1y),15,(0,255,0),-1)   # Filled green circle
cv2.circle(image_rgb,(c2x,c2y),15,(0,255,0),-1)    # Filled red circle

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(image_rgb,(c1x,c1y),(c2x,c2y),(0,255,0),3)

# Step 5: Add Text Labels for Regions and Centers
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,'region',(top_left1[0],top_left1[1]-10),font,0.7,(0,255,255),2, cv2.LINE_AA)
# Step 6: Add Bi-Directional Arrow Representing Height
  # Start near the top-right
  # End near the bottom-right

# Draw arrows in both directions
arrow_start=(w-50,20)  # Downward arrow
arrow_end=(w-50,h-20) # Upward arrow

# Annotate the height value
cv2.arrowedLine(image_rgb,arrow_start,arrow_end,(255,255,0),3,tipLength=0.05)
cv2.arrowedLine(image_rgb,arrow_end,arrow_start,(255,255,0),3,tipLength=0.05)
# Step 7: Display the Annotated Image
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title('Annotated image')
plt.axis('off')
plt.show()