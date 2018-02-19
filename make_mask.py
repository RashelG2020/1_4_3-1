# -*- coding: utf-8 -*-
'''
Rashel_G_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory,'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50,100):
        img[row][column] = [255, 255, 0] # red + green = yellow
fig.show()


# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [500, 150, 200, 700] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [370, 80, 90, 400] # magenta, alpha=255
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()            