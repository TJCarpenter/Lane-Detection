# Creates an HSV (Hue Saturated Value) image from the received image
# Tyler Carpenter 1273574
# 11/1/2017

# Import Library
import cv2

# Import Files


# Global


def hsv(image):
    '''Converts an image to HSV'''
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # HSV = [HUE,  SATURATION, VALUE]
    return hsv_image
