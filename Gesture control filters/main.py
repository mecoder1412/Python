import cv2
import mediapipe as mp
import numpy as np
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
filters=[None, "GRAYSCALE", "SEPIA", "NEGATIVE", "BLUR"]
current_filter=0#Starting filter
# Webcam setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()
# Timestamp for debouncing gestures
last_action_time=0
debounce_time=1#1 second debounce between actions
#Function to apply filters
def apply_filter(filter_name, frame):
  if filter_name == 'GrayScale Filter':
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  elif filter_name == 'Sepia Filter':
    kernel = np.array([[0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]])
    sepia = cv2.transform(frame, kernel)
    sepia = np.clip(sepia, 0, 255)
    return sepia
  elif filter_name == 'Negative Filter':
    return cv2.bitwise_not(frame) 
  elif filter_name == 'BLUR':
    return cv2.GaussianBlur(frame,(15,15),0)
  return frame

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)  # Flip the image for a mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[i].classification[0].label  # 'Left' or 'Right'
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract the tip of the thumb and index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_FINGER_TIP]
            h, w, _ = img.shape
            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))
            middle_pos = (int(middle_tip.x * w), int(middle_tip.y * h))
            ring_pos = (int(ring_tip.x * w), int(ring_tip.y * h))
            pinky_pos = (int(index_tip.x * w), int(pinky_tip.y * h))
            # Draw circles and line
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, middle_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, ring_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, pinky_pos, 10, (255, 0, 0), cv2.FILLED)
            #Gesture Logic
            current_time=time.time()
            #Click picture: Thumb touches Index finger
            if abs(thumb_pos.x-index_pos.x)< 30 and abs(thumb_pos.y-index_pos.y)<30:
               if current_time-last_action_time>debounce_time:
                  cv2.putText(img, "Picture Captured!",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                  last_action_time=current_time
                  cv2.imwrite(f"picture_{int(time.time())}.jpg",img)
                  print("Picture saved")
            elif abs(thumb_pos.x-middle_pos.x)< 30 and abs(thumb_pos.y-middle_pos.y)<30 or abs(thumb_pos.x-ring_pos.x)< 30 and abs(thumb_pos.y-ring_pos.y)<30 or abs(thumb_pos.x-pinky_pos.x)< 30 and abs(thumb_pos.y-pinky_pos.y)<30:
               if current_time-last_action_time>debounce_time:
                   current_filter=(current_filter+1)% len(filters)
                   last_action_time=current_time 
                   print(f"Switch to filter: {filters[current_filter]}")
#Apply the current filter
filtered_img=apply_filter(img, filters[current_filter])
# Display the image
if filter_name == 'GrayScale Filter' or filter_name == 'Edge Filter':
cv2.imshow("Gesture-Controlled Photo App", cv2.cvtColor(filtered_img, cv2.COLOR_GRAY2BGR))
else:
cv2.imshow("Gesture-Controlled Photo App", filtered_img)
if cv2.waitKey(1) & 0xFF == 27:
break
# Release resources
cap.release()
cv2.destroyAllWindows()                       