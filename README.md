# MyLane
MyLane is a python program that applies lane detection to a given video file.

## Prerequisites
* Have the following python3 modules installed: OpenCV, Numpy, & Tkinter

```bash
pip3 install opencv-python numpy tkinter scikit-image
```

## Instructions
1. Run the program
```bash
./lane.py
```
2. Select video (.mp4) via the GUI pop-up 
3. Press 'q' at anytime to stop the program and close the video player. Otherwise the program will automatically stop once the video has played through once.

## Features

* Sobel Edge Detection, Binary Threshold, Set to 0 Threshold, HLS (see lines 30:35) 
* Change way of selecting video: GUI, manual, or live webcam (see lines 40:48) 
