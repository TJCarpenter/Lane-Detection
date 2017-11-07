# Gets all images from a given file '''Change to a stream in the future'''
# Tyler Carpenter 1273574
# 11/1/2017

# Import Library
import matplotlib.image as matimg
import os
import errno

# Import Files
import process_frame

# Global
directory = '../Lane Images/Raw/Still Images/'
# Change to a stream eventually

def getImage():
    '''Get all images from a directory'''

    '''Check if directory exists'''
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    '''Loop through images in directory'''
    for raw_image in os.listdir(directory):
        image = matimg.imread(directory + raw_image)
        resultingImage = process_frame(image)
        # Saves the resulting images in a seperate file
        matimg.imsave('../Lane Images/Resulting Image/result_' + raw_image, resultingImage)
        
