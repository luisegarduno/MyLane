#!/usr/bin/env python3
import cv2
import numpy as np
from skimage.filters import sobel_h, sobel_v
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Default: set width & height: 960x540
W = 1920//2
H = 1080//2

def process_frame(img):
    # Resize video
    img = cv2.resize(img, (W, H))

    # cv2.cvtColor is applied over image w/ given
    # parameters to convert image to Grayscale/HLS
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # applying different thresholding techniques on the input image
    # all pixels value above 120 will be set to 255
    ret, thresh1 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img1, 120, 255, cv2.THRESH_TOZERO)

    # Apply sobel edge detection gradient 2D
    gradient_mag = np.sqrt(sobel_v(img1)**2 + sobel_h(img1)**2) 

    # Show window
    cv2.imshow('Original', img)
    #cv2.imshow('Grayscale', img1)
    #cv2.imshow('HLS', img2)
    cv2.imshow('Sobel Edge Detector', gradient_mag)
    #cv2.imshow('Binary Threshold', thresh1)
    #cv2.imshow('Set to 0', thresh2)

if __name__ == "__main__":
    # Load video (.mp4)
    
    # Option 1: Use GUI to select file your files
    Tk().withdraw()
    cap = cv2.VideoCapture(askopenfilename(filetypes=[("Video files", "*.mp4")]))

    # Option 2: Manually input location of video file
    #cap = cv2.VideoCapture("./Videos/driving.mp4")

    # Option 3: Use webcam
    #cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
