import os
import pygame
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from tkinter.filedialog import askopenfile

root = Tk()
pygame.mixer.init()
def browse():
    file = filedialog.askopenfile(mode="r")
    if file:
        global filepath
        filepath = os.path.abspath(file.name)
        print(filepath)
def PlayMusic():
    pygame.mixer.music.load(filepath)
    fileName = Path(filepath)
    songlabel.config(text=f"Playing:\n{fileName.name}")
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
songlabel = Label(
    master=root,
)
songlabel.pack(pady=0, padx =0)
browseBtn = Button(
    master=root,
    command=browse,
    text="Browse",
)
browseBtn.pack(padx = 0, pady=0)

playBtn = Button(
    master=root,
    command=PlayMusic,
    text="play",
)

playBtn.pack(padx=0,pady=0)
root.mainloop()

