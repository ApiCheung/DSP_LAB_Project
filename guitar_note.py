#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/02/20 9:34 PM
# @Author  : Esmee Zhang
# @Site    : 
# @File    : guitar_note.py
# @Software: PyCharm

import sys, os
import time, random
import wave, argparse
import numpy as np
from collections import deque

pmNotes = {'C1': 262, 'C#1': 277, 'D1': 293, 'D#1': 311, 'E1': 329, 'F1': 349, 'F#1': 370, 'G1': 391, 'G#1': 415,
           'A1': 440, 'B1': 494, 'A#1': 466}


def writeWAVE(fname, data):
    file = wave.open(fname, 'wb')

    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100

    file.setparams((nChannels, sampleWidth, frameRate, nFrames,
                    'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()


def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100
    N = int(sampleRate / freq)
    buf = deque([random.random() - 0.5 for i in range(N)])

    samples = np.array([0] * nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.995 * 0.5 * (buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()

    samples = np.array(samples * 32767, 'int16')
    return samples.tostring()



def main():

    global gShowPlot

    parser = argparse.ArgumentParser(description="Generating sounds with Karplus String Algorithm.")

    args = parser.parse_args()

    print('creating notes...')
    for name, freq in list(pmNotes.items()):
        fileName = name + '.wav'
        if not os.path.exists(fileName):
            data = generateNote(freq)
            print('creating ' + fileName + '...')
            writeWAVE(fileName, data)
        else:
            print('fileName already created. skipping...')



if __name__ == '__main__':
    main()
