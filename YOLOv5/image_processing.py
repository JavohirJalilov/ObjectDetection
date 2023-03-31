import cv2
import numpy as np
import matplotlib.pyplot as plt

labels_color = {
    # 'svetafor':(192, 57, 43), #pomegranate
    # 'yuk mashina':(232, 67, 147), # prunis avium
    # 'stop sign':(26, 188, 156), # turquoise
    # 'mashina':(241, 196, 15), # sun flower
    # 'odam': (243, 156, 18), # orange
    # 'avtobus':(46, 204, 113) # emerald
    "traffic light": (192, 57, 43),  # pomegranate
    "bus": (232, 67, 147),  # prunis avium
    "stop sign": (26, 188, 156),  # turquoise
    "truck": (241, 196, 15),  # sun flower
    "person": (243, 156, 18),  # orange
    "car": (46, 204, 113),  # emerald
    }

def drawing_image(image,xmin,ymin,xmax,ymax,name):
    """
    Drawing image
    """
    start_point, end_point = (int(xmin),int(ymin)), (int(xmax),int(ymax))
    image = cv2.rectangle(
        image,
        start_point, 
        end_point,
        color=labels_color.get(name,(190, 46, 221)),
        thickness = 2
        )
    text_size, _ = cv2.getTextSize(
        name,
        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
        fontScale=0.5,  
        thickness=1
        )
    text_w, text_h = text_size
    image = cv2.rectangle(
        image,
        (int(xmin),int(ymin)-text_h), 
        (int(xmin) + text_w, int(ymin)), 
        color=labels_color.get(name,(190, 46, 221)), 
        thickness=-1
        )
    image = cv2.putText(
        image,
        name,
        org=(int(xmin),int(ymin)-1),
        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
        fontScale=0.5, 
        color=(255, 255, 255), 
        thickness=1,
        lineType=cv2.FILLED
        )
    return image

def image_processing(image, data):
    """
    image processing for object detection
    """
    area = []
    for xmin,ymin,xmax,ymax,confidence,label,name in data.values:
        area = abs(xmax-xmin)*abs(ymax-ymin)
        # if name == 'traffic light':
        #     name = 'svetafor'
        #     image = drawing_image(image, xmin,ymin,xmax,ymax,name)

        # if area > 1500 :
        #     if name == 'car':
        #         name = 'mashina'
        #     elif name == 'truck':
        #         name = 'yuk mashina'
        #     elif name == 'person':
        #         name = 'odam'
        #     elif name == 'bus':
        #         name = 'avtobus'
        #     else:
        #         continue
            
        image = drawing_image(image, xmin,ymin,xmax,ymax,name)
    return image

def resize_image(image, w,h):
    """
    Image resize with opencv
    """
    image = cv2.resize(image,(w, h))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image