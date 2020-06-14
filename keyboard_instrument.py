#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/1/20 10:54 PM
# @Author  : Esmee Zhang
# @Site    : 
# @File    : keyborad_instrument.py
# @Software: PyCharm
import pygame.mixer
import sys
from tkinter import *
from tkinter.ttk import *
import pyaudio, struct
import time
import threading
import wave
import tkinter.filedialog
import tkinter.messagebox


CHUNK_SIZE = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE = 44100
RECORD_SECONDS = 20
fileName = None
allowRecording = False



def record():
    global fileName
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels = CHANNELS, rate = RATE, input = True,
                    frames_per_buffer=CHUNK_SIZE)
    wf = wave.open(fileName,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    while allowRecording:
        data = stream.read(CHUNK_SIZE)
        wf.writeframes(data)
    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    fileName = None


pygame.init()
pygame.mixer.set_num_channels(24)
def value_C():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("C.wav"))

    return

def value_C_sharp():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("C#.wav"))

    return

def value_D():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("D.wav"))

    return

def value_D_sharp():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("D#.wav"))


def value_E():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("E.wav"))


def value_F():
    pygame.mixer.Channel(5).play(pygame.mixer.Sound("F.wav"))


def value_F_sharp():
    pygame.mixer.Channel(6).play(pygame.mixer.Sound("F#.wav"))


def value_G():
    pygame.mixer.Channel(7).play(pygame.mixer.Sound("G.wav"))


def value_G_sharp():
    pygame.mixer.Channel(8).play(pygame.mixer.Sound("G#.wav"))


def value_A():
    pygame.mixer.Channel(9).play(pygame.mixer.Sound("A.wav"))


def value_A_sharp():
    pygame.mixer.Channel(10).play(pygame.mixer.Sound("A#.wav"))


def value_B():
    pygame.mixer.Channel(11).play(pygame.mixer.Sound("B.wav"))


def C():
    pygame.mixer.Channel(12).play(pygame.mixer.Sound("C1.wav"))

def C_sharp():
    pygame.mixer.Channel(13).play(pygame.mixer.Sound("C#1.wav"))

def D():
    pygame.mixer.Channel(14).play(pygame.mixer.Sound("D1.wav"))

    return
def D_sharp():
    pygame.mixer.Channel(15).play(pygame.mixer.Sound("D#1.wav"))

def E():
    pygame.mixer.Channel(16).play(pygame.mixer.Sound("E1.wav"))

def F():
    pygame.mixer.Channel(17).play(pygame.mixer.Sound("F1.wav"))

def F_sharp():
    pygame.mixer.Channel(18).play(pygame.mixer.Sound("F#1.wav"))

def G():
    pygame.mixer.Channel(19).play(pygame.mixer.Sound("G1.wav"))

def G_sharp():
    pygame.mixer.Channel(20).play(pygame.mixer.Sound("G#1.wav"))

def A():
    pygame.mixer.Channel(21).play(pygame.mixer.Sound("A1.wav"))

def A_sharp():
    pygame.mixer.Channel(22).play(pygame.mixer.Sound("A#1.wav"))

def B():
    pygame.mixer.Channel(23).play(pygame.mixer.Sound("B1.wav"))



def my_piano(event):
    if event.char == 'q':
        value_C()
        print("you are pressing C")
    if event.char == '2':
        value_C_sharp()
        print("you are pressing C sharp")
    if event.char == 'w':
        value_D()
        print("you are pressing D")
    if event.char == '3':
        value_D_sharp()
        print("you are pressing D sharp")
    if event.char == 'e':
        value_E()
        print("you are pressing E")
    if event.char == 'r':
        value_F()
        print("you are pressing F")
    if event.char == '5':
        value_F_sharp()
        print("you are pressing F sharp")
    if event.char == 't':
        value_G()
        print("you are pressing G")
    if event.char == '6':
        value_G_sharp()
        print("you are pressing G sharp")
    if event.char == 'y':
        value_A()
        print("you are pressing A")
    if event.char == '7':
        value_A_sharp()
        print("you are pressing A#")
    if event.char == 'u':
        value_B()
        print("you are pressing B")
    if event.char == '0':
        quit()

    if event.char == 'z':
        C()
        print("you are pressing C")
    if event.char == 's':
        C_sharp()
        print("you are pressing C sharp")
    if event.char == 'x':
        D()
        print("you are pressing D")
    if event.char == 'd':
        D_sharp()
        print("you are pressing D sharp")
    if event.char == 'c':
        E()
        print("you are pressing E")
    if event.char == 'v':
        F()
        print("you are pressing F")
    if event.char == 'g':
        F_sharp()
        print("you are pressing F sharp")
    if event.char == 'b':
        G()
        print("you are pressing G")
    if event.char == 'h':
        G_sharp()
        print("you are pressing G sharp")
    if event.char == 'n':
        A()
        print("you are pressing A")
    if event.char == 'j':
        A_sharp()
        print("you are pressing A sharp")
    if event.char == 'm':
        B()
        print("you are pressing B")
    if event.char == '0':
        quit()



root = Tk()

def start():
    global allowRecording, fileName
    fileName = tkinter.filedialog.asksaveasfilename(filetypes = [('wave_file','*.wav')])
    if not fileName.endswith('.wav'):
        fileName = fileName + '.wav'
    allowRecording = True
    threading.Thread(target=record).start()

def stop():
    global allowRecording
    allowRecording = False



s1 = StringVar()
s1.set("Play the instrument !")
s2 = StringVar()
s2.set("Type 'qwertyu23567' for piano")
s3 = StringVar()
s3.set("Type 'zxcvbnmsdsdghj' for guitar")
s4 = StringVar()
s4.set("Press 0 to quit")


L1 = Label(root, textvariable  = s1, font =('Arial', 20), background = "white").grid(row = 0, column = 0 )
L2 = Label(root, textvariable = s2, font = ('Arial', 15), background = "white").grid(row = 1, column = 0)
L3 = Label(root, textvariable = s3, font = ('Arial', 15), background = "white").grid(row = 1, column = 1)
L4 = Label(root, textvariable  = s4, font =('Arial', 20), background = "white").grid(row = 0, column = 1)

btnStart = Button(root, text="Start recording", command= start).grid(row = 3, column = 0)
btnStop = Button(root, text = "Stop recording", command = stop).grid(row = 3, column = 1)

piano = PhotoImage(file="unnamed.png")
guitar = PhotoImage(file ="guitar.png")

Label_piano = Label(root,image=piano).grid(row =2,column = 0)

Label_guitar = Label(root,image = guitar).grid(row = 2, column = 1)
#button_piano.pack(side = LEFT)
#button_guitar.pack(side = RIGHT)
#L.pack(side = TOP)
root.bind("<Key>", my_piano)
root.mainloop()


