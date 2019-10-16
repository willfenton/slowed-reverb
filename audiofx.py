#====================================
# Author: Will Fenton
# Date: October 15 2019
#====================================

from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .speed(0.9)
    .reverb()
)

infile = "input/GINGER/SUGAR.mp3"
outfile = "output/Sugar.mp3"

fx(infile, outfile)
