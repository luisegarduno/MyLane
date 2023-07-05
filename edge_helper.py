import cv2


def threshold(channel, thresh=(120, 255)):
    """
    Defintion: Applies thresholding to a specific channel on an image
    Parameters:
        channel: (color)
        thresh: pixel value range (low, max)
    """
    return cv2.threshold(channel, thresh[0], thresh[1], cv2.THRESH_BINARY)
