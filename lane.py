#!/usr/bin/env python3
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Set Width & Height: 960x540
W = 1920//2
H = 1080//2

def process_frame(img):
    # Resize video
    img = cv2.resize(img, (W, H))

    # Show window
    cv2.imshow('MyLane', img)

if __name__ == "__main__":
    # Load video (.mp4)
    Tk().withdraw()
    cap = cv2.VideoCapture(askopenfilename(filetypes=[("Video files", "*.mp4")]))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
