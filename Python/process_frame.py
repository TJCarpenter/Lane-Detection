# Receives the images from the directory and processes
# the image to create the resulting image
# Tyler Carpenter 1273574
# 11/1/2017

# Import Library
import numpy as np

# Import Files
from grayscale import *
from hsv import *

# Global
debug = False
image = cv2.imread('TestImage.jpg')

def process_frame(image):
    '''Takes in an image and finds the white or yellow mask and then
       determines where the lanes are and makes a resulting mask'''

    hsv_image = hsv(image)

    if debug == True:
        '''Show HSV image'''
        cv2.imshow('HSV', cv2.resize(hsv_image, (1000, 500)))

    #Yellow Mask
    '''Find the yellow mask in the HSV range of [0, 100, 0] to MAX'''

    lower_yellow = np.array([0, 100, 0], dtype = np.uint8) 
    upper_yellow = np.array([255, 255, 255], dtype = np.uint8)
    

    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    if debug == True:
        '''Show Yellow mask'''
        cv2.imshow('Yellow_Mask', cv2.resize(yellow_mask, (1000, 500)))
    
    # White Mask
    '''Find the white mask in the HSV range of [0, 0, 75] to MAX'''

    lower_white = np.array([0, 0, 75], dtype = np.uint8) 
    upper_white = np.array([255, 255, 255], dtype = np.uint8)

    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    if debug == True:
        '''Show White mask'''
        cv2.imshow('White_Mask', cv2.resize(white_mask, (1000, 500)))

    # Combine Mask

    yw_mask = cv2.bitwise_or(white_mask, yellow_mask)

    if debug == True:
        '''Show Yellow and White mask'''
        cv2.imshow('Yellow_and_black', cv2.resize(yw_mask, (1000, 500)))

    return yw_mask

if __name__ == '__main__':
    process_frame(image)
    
    if debug == True:
        '''Resulting Image'''
        cv2.imshow('Main', cv2.resize(process_frame(image), (1000, 500)))
    
    
