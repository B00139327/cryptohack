#!/usr/local/bin/python3
import numpy as np
from PIL import Image

# Open images
im1 = Image.open("im1.png")
im2 = Image.open("im2.png")

# Make into Numpy arrays
im1np = np.array(im1)*255
im2np = np.array(im2)*255

# XOR with Numpy
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')