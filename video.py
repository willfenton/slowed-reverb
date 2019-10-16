#====================================
# Author: Will Fenton
# Date: October 15 2019
#====================================

import moviepy.editor as mp
import math

audio_clip = mp.AudioFileClip("output/Sugar.mp3")
video_clip = mp.VideoFileClip("input/test.gif")
num_loops = math.ceil(audio_clip.duration / video_clip.duration)
video_clip2 = video_clip.loop(n=num_loops)
video_clip3 = video_clip2.set_audio(audio_clip)
video_clip3.write_videofile("output/test2.mp4")