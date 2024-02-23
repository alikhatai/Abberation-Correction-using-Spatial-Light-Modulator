# ========================================================================#
# Author Ali Khatai                                                       #
# This python document contain code written as part of optics research at #
# IWU during summer 2022 under Prof. Gabriel Spalding                     #
# ========================================================================#

# this file contains code for running a series of grey scale images in an animation
# for performing wavefront/abberation correction based on the Cizmar method using the
# Spatial light modulator(SLM). After updating the frame this program also takes an
# image from the connected CCD camera and saves it on file.



# tkinker is used to display the images and cv2 i for accessing the camera
from tkinter import *
from PIL import Image
from PIL import ImageTk
import numpy as np
import cv2


# create the main window with same dimensions as the resoluton of the SLM
win = Tk()
win.geometry("1920x1080")
win.attributes("-fullscreen",True)

# create a label which will be used to display the image
label1 = Label(win, bd=0, highlightthickness=0)
label1.pack()
label1.place(x=0, y=0)

# choose which camera to use. In the lab the CCD camera is usually a secondary camera so we will use 1.
# if the CCD camera is the only camera connected to the computer than use 0
cap= cv2.VideoCapture(0)

# this function is used to update the gray scale images on the SLM and capture the corresponding image using
# the CCD camera
def my_func(window, label):
    # z is used in the path name of loading images, as the images are saved in numerical order
    global z
    z = 1

    # x is used to keep track of how many images are in the list imgs
    global x
    x = 0

    #
    global c
    c = 1

    global imgs
    imgs = []

    # function to change to next image
    def move():

        global x
        global z
        global c
        global imgs

        # define the path where images are saved
        name = "D:/imagesSLM30x30/" + str(z) + ".bmp"

        # open the image and apply it to the label
        img = Image.open(name)
        #img.show()
        img = ImageTk.PhotoImage(img)
        imgs.append(img)
        label.config(image=imgs[x])

        # after the images is displayed on the SLM, tell the camera to take a picture and save
        # it on file
        '''cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        name1 = "D:/slm/" + str(z - 1) + ".bmp"
        img.save(name1, 'BMP')'''

        # for some reason tkinter dosen't update the images if they are not in a python list.
        # but loading all the images in a list takes up too much memory, so the images that have been
        # used are discarded
        if x!=0 and x % 700 == 0:
            del imgs[0:500]
            x = x - 500

        #increment x and z
        x = x + 1

        print(z)
        if (z % 10 == 0 and c % 4 != 0):
            c = c + 1
            z = z - 9
        elif (z % 10 != 0):
            z = z + 1
        elif (z % 10 ==0 and c % 4 ==0):
            c = c + 1
            z = z + 1


        #stop when all the images have been displayed
        if z < 1441:
           '''The .after() fucntion calls a desired function after a certain delay
           here we call the move() periodically to update the images and run an animation
           the second argument is the delay in miliseconds which can be changed to set the frame rate of the animaions'''
           window.after(500, move)
    move()


my_func(win, label1)
win.mainloop()

