import cv2
import time
import numpy as np
from pysndfx import AudioEffectsChain
from mydia import Videos
#processes effects on a numpy array in place
fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
)

# Create a reader object
reader = Videos()

# Call the 'read()' function to get the video tensor
# which will be of shape (num_videos, num_frames, height, width, color_depth)
video = reader.read("res/demovid_unprocessed.mp4")[0] # get video tensor
"""
TODO: The Plan:
Holy shit this is hard to think about
What i want is to get an array representing a single color channel from from 0 to the last frame
Loop over pixels, height and width, get array of red pix value across frames 
apply fx() to that array
recombine to regular shape for a video
save or play it back via opencv
"""
for i in range(video.shape[2]):
    for j in range(video.shape[1]):
        red_tensor = video[..., i, j, 0].astype(np.float32) 
        video[..., i, j, 0] = fx(red_tensor).astype(np.uint8)

        green_tensor = video[..., i, j, 1] 
        video[..., i, j, 1] = fx(green_tensor)

        blue_tensor = video[..., i, j, 2] 
        video[..., i, j, 2] = fx(blue_tensor)

#play the processed video
cv2.namedWindow("output")
for f in video:
    cv2.imshow(f)
    time.sleep(1/24)
cv2.waitKey(0)
    