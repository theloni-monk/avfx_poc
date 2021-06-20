import cv2
import numpy as np
from pysndfx import AudioEffectsChain
from mydia import Videos
fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
)

# Create a reader object
reader = Videos()

# Call the 'read()' function to get the video tensor
# which will be of shape (num_videos, num_frames, height, width, color_depth)
video = reader.read("res/demovid_unprocessed")[0] # get video tensor
"""
TODO: The Plan:
Holy shit this is hard to think about
What i want is to get an array representing a single color channel from from 0 to the last frame
Loop over pixels, height and width, get array of red pix value across frames 
apply fx() to that array
recombine to regular shape for a video
save or play it back via opencv
"""
red_tensor = video[] # this makes my head hurt, i dont know how to properly address the tensor