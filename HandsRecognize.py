import cv2
import numpy as np

cv2.ocl.setUseOpenCL(False)

# Load the YOLOv4 model in OpenCV
model=cv2.dnn.readNet('./darknet-master/cfg/yolov4.cfg','./darknet-master/yolov4.weights')

# Get the output layer names from the YOLOv4 model
layer_names = model.getLayerNames()
output_layers = [layer_names[i - 1] for i in model.getUnconnectedOutLayers()]

# Set the minimum confidence threshold for hand detection
conf_threshold = 0.5

# Capture frames from the video source
cap = cv2.VideoCapture('F://AI//UnMute//Dataset//Videos//Alphabets//double handed.mp4')

while True:
    # Capture a frame from the video source
    ret, frame = cap.read()
    
    # Convert the frame to a format that can be processed by the YOLOv4 model
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
    
    # Pass the converted frame through the YOLOv4 model for detection
    model.setInput(blob)
    outs = model.forward(output_layers)
    
    # Initialize the list of detected hands
    hands = []
    
    # Loop over the detected objects and filter out the hands
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if class_id == 0 and confidence > conf_threshold:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = center_x - w // 2
                y = center_y - h // 2
                hands.append((x, y, w, h))
    
    # Draw bounding boxes around the detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the output frame
    cv2.imshow("Hands", frame)
    
    # Exit the program if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
