# ========================================================================#
# Author Ali Khatai                                                       #
# This python document contain code written as part of optics research at #
# IWU during summer 2022 under Prof. Gabriel Spalding                     #
# ========================================================================#

# this file contains code for generating grey scales images for performing
# wavefront/abberation correction based on the Cizmar method using the
# Spatial light modulator(SLM)

from PIL import Image
from PIL import ImageTk
import numpy as np
# import the blaze_first function from blaze.py
from blaze import *

# define the resolution og the SLM
w = 1920
h = 1080

# define the dimensions of the orthogonal modes
pix = 120
piy = 120

# calculate the number of modes needed in the horizontal and vertical directions
hor = w//pix
ver = h//piy

# this list contains scalers that are added to each mode to apply a phase shift
# these can be changed to change the number of desired phase shifts
shift = [0, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6]

counter = 1

# use the blaze first function to create the reference mode
SLM = blaze_first(pix, pix, 4, 5)

# create a 2d matrix with zero values and place the reference mode in the desired position
hol = np.zeros((h, w), dtype=float)
hol[480:600, 960:1080] = SLM

# loops through all the modes whilst applying the phase shifts
for z in range(ver):

    #calculate vertical position of the modes
    xx_ = z*pix
    yy_ = (z*pix)+pix

    for i in range(hor):
            # calculate horizontal position of the modes
            xx = i * pix
            yy = (i * pix) + pix

            # make the blazing and get a copy of the image with reference mode
            SLM = blaze_first(pix, pix, 4, 5)
            holo = np.copy(hol)

            for j in shift:
                    # add the phase shift and place the blazing on the image in the required position
                    SLM = np.add(SLM, j)
                    holo[xx_:yy_, xx:yy] = SLM

                    # create image from array and save it on file
                    img = Image.fromarray(np.uint8(holo), 'L')
                    name = "D:/imagesSLM30x30/" + str(counter) + ".bmp"
                    img.save(name, 'BMP')
                    counter += 1

