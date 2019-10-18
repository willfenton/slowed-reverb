#!/usr/bin/env python
#===============================================================================
# Author: Will Fenton
# Date: October 17 2019
#===============================================================================

from pysndfx import AudioEffectsChain
import moviepy.editor as mp

import os
import sys
import math
import getopt

#===============================================================================

def print_usage():
    sys.stderr.write(
"""Usage: python3 slowed-reverb.py [options]
Options:
    (-a | --audio)        <audio file>   the audio file to use
    (-g | --gif)          <gif file>     the gif to loop
    (-o | --output-path)  <path>         where to save the output
    (-h | --help)                        display this message
Example: python3 slowed-reverb.py -a song.mp3 -g video.gif -o slowed-reverb.mp4
""")

def main():
    # quit if no arguments provided
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)

    # read options
    try:
        options = "a:g:o:h"
        longOptions = ["audio=", "gif=", "output-path=", "help"]
        opts, args = getopt.getopt(sys.argv[1:], options, longOptions)
    except getopt.GetoptError:
        print_usage()
        sys.exit(1)

    audio_path = ""
    gif_path = ""
    output_path = "output/slowed-reverb.mp4"

    # parse options
    for o, v in opts:
        if o in ("-a", "--audio"):
            audio_path = v
        if o in ("-g", "--gif"):
            gif_path = v
        if o in ("-o", "--output-path"):
            output_path = v
        if o in ("-h", "--help"):
            print_usage()
            sys.exit()

    # make sure audio and gif are provided
    if audio_path == "":
        raise Exception("Need to specify an audio file.")
    if gif_path == "":
        raise Exception("Need to specify a gif")

    # make output directory
    try:
        os.mkdir("output")
    except FileExistsError:
        pass

    # chain of effects to apply to the audio
    fx = (
        AudioEffectsChain()
        .speed(0.9)
        .reverb()
    )

    # path to temporarily store the audio
    temp_audio_path = "output/temp.mp3"

    # apply the effects, save file
    fx(audio_path, temp_audio_path)

    # load audio file
    audio_clip = mp.AudioFileClip(temp_audio_path)

    # load video
    video_clip = mp.VideoFileClip(gif_path)

    # loop the gif for the duration of the audio
    num_loops = math.ceil(audio_clip.duration / video_clip.duration)
    video_clip2 = video_clip.loop(n=num_loops)

    # add the audio to the video
    video_clip3 = video_clip2.set_audio(audio_clip)

    # save result
    video_clip3.write_videofile(output_path, verbose=False, logger=None)

    # delete temp audio file
    os.remove(temp_audio_path)

#===============================================================================

if __name__ == "__main__":
    main()

#===============================================================================
