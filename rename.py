import os

# specify the folder where the images are saved
folder = "D:\imagesSLM30x30"

# number of images needs to be set depending on the number of modes that were used
# for the abeeration correction. for example if we are using modes of 120x120 pixels then we'll have a total
# of 140 modes each with 10 phase shifts. this gives us a total of 1440 images.
num_images = 1440

x = 1
y = 1
z = 1
phase = 0

for filename in range(1, num_images+1):
    dst = f"{str(y)}-{str(x)}-{phase}.bmp"
    
    if filename%160 == 0:
        y = y+1
        x = 1
    elif filename % 10 == 0:
        x = x + 1
    if (phase+1) % 10 == 0:
        phase = 0
    else:
        phase = phase + 1
    z = z + 1
    src = f"{folder}\{str(filename)}.bmp"  # foldername/filename, if .py file is outside folder
    dst = f"{folder}\{dst}"

    # rename() function will
    #rename all the files
    os.rename(src, dst)



