import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch

# model load
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detection(image):
    """
    Object detection
    """
    results = model(image)
    # get data(Pascal VOC, confidence, class)
    data = results.pandas().xyxy[0]
    return data