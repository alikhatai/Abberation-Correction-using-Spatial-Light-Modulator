# ========================================================================#
# Author Ali Khatai                                                       #
# This python document contain code written as part of optics research at #
# IWU during summer 2022 under Prof. Gabriel Spalding                     #
# ========================================================================#

# this file contains function to create grey scale images which are the
# computer generated holograms used to control our Spatial light modulators

#import numpy for matrix calculation and Pillow for image processing
import numpy as np
from PIL import Image, ImageTk


def lens(W, H, R):
    """
    Generates digital hologram for a lens
    Arguments:
        W: width of the SLM display in pixels
        H: height of the SLM display in pixels
        R: Radius
    Returns:
        greyscale PIL image for the lens
    """
    x_lens = np.empty((0, W), float)

    R = R / 2
    for y in range(H):
        y_ll = [[]]
        for x in range(W):
            y_l = 255 - ((((x * 256) / 1920) - 256 * R) ** 2) % 256
            y_ll[0].append(y_l)
        xx_lens = np.append(x_lens, np.array(y_ll), axis=0)

    y_lens = np.empty((0, H), float)
    for y in range(W):
        y_ll = [[]]
        for x in range(H):
            y_l = 255 - ((((x * 256) / 1920) - 146 * R) ** 2) % 256
            y_ll[0].append(y_l)
        y_lens = np.append(y_lens, np.array(y_ll), axis=0)

    SLM2 = np.add(xx_lens, np.transpose(y_lens))

    img2 = Image.fromarray(np.uint8(SLM2), 'L')
    return img2

def blaze_first(W, H, xs, ys):
    """
    Generates digital hologram for a blazing patten
    Arguments:
        W: width of the SLM display in pixels
        H: height of the SLM display in pixels
        xs: number of vertical blazings
        ys: number of horizontal blazings
    Returns:
        greyscale PIL image for the blazing
    """
    hor_blazing = np.empty((0, W), float)
    hor_spacing = (xs * 256) / W
    for y in range(H):
        y_emp = [[]]
        for x in range(W):
            x2 = x * hor_spacing
            y = (x2) % 256
            y_emp[0].append(y)

    hor_blazing = np.append(hor_blazing, np.array(y_emp), axis=0)

    ver_blazing = np.empty((0, H), float)
    ver_spacing = (ys * 256) / H

    for y in range(W):
        y_emp = [[]]
        for x in range(H):
            x2 = x * ver_spacing
            y = (x2) % 256
            y_emp[0].append(y)

    ver_blazing = np.append(ver_blazing, np.array(y_emp), axis=0)

    SLM = np.transpose(ver_blazing)
    SLM = np.add(hor_blazing, SLM)

    img = Image.fromarray(np.uint8(SLM), 'L')
    return img

