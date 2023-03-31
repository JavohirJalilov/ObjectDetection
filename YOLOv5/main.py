import cv2
import numpy as np
import torch
import detect
import image_processing

#Read video
cap = cv2.VideoCapture("../ROAD.mp4")
out = cv2.VideoWriter('keypoints.mp4', cv2.VideoWriter_fourcc(*'mp4v'),fps=30.0, frameSize=(1536, 864))

#Check if video is loaded properly
if not cap.isOpened():
    print("Could not open video")
    exit()
#Loop until the end of the video
while True:
    #Read a new frame
    ok, frame = cap.read()
    if not ok:
        break
    # frame shape (1080,1920)
    # Prediction
    image = frame
    scale_percent = 80 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    image = image_processing.resize_image(image, width, height)

    data = detect.detection(image)
    # drawing bbox
    image = image_processing.image_processing(image, data)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    
    cv2.imshow("frame", image)
    out.write(image)

    #Wait for key
    k = cv2.waitKey(1)
    if k == 27:
        break

out.release()
#Print the end of the video
print("End of video")
# Close all windows
cv2.destroyAllWindows()