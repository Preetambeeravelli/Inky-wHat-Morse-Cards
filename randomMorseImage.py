#!/usr/bin/env python3

import os
from PIL import Image
from inky import InkyWHAT
import random

# Generate a random number between 1 and 26 (inclusive)
random_number = random.randint(1, 26)

# Set up the inky wHAT display and border colour
inky_display=InkyWHAT("red")
inky_display.set_border(inky_display.BLACK)

# Creating image path with the use of random numbers
directory = "Cards"
random_file = str(random_number) + ".png"
img_path = os.path.join(directory, random_file)

# Open our image file from path created

img = Image.open(img_path)

# Get the width and height of the image

w, h = img.size

# Calculate the new height and width of the image

h_new = 300
w_new = int((float(w) / h) * h_new)
w_cropped = 400

# Resize the image with high-quality resampling

img = img.resize((w_new, h_new), resample=Image.LANCZOS)

# Calculate coordinates to crop image to 400 pixels wide

x0 = (w_new - w_cropped) / 2
x1 = x0 + w_cropped
y0 = 0
y1 = h_new

# Crop image

img = img.crop((x0, y0, x1, y1))

# Convert the image to use a white / black / red colour palette

pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

img = img.convert("RGB").quantize(palette=pal_img)

# Display the final image on Inky wHAT

inky_display.set_image(img)
inky_display.show()
