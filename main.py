import os
import pygame
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from tkinter.filedialog import askopenfile

root = Tk()
pygame.init()
pygame.mixer.init()
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

queue = []


def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('music end event')
            PlayMusic()


    root.after(100, check_event)
def browse():
    file = filedialog.askopenfile(mode="r")
    if file:
        global filepath
        filepath = os.path.abspath(file.name)
        queue.append(filepath)
        print(queue)

def PlayMusic():
    pygame.mixer.music.load(queue.pop(0))
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
def updateUI():
    fileNames = [Path(path).name for path in queue]
    songlabel.config(text="\n".join(fileNames))
    root.after(100, updateUI)


clicked = 0


def PauseMusic():
    global clicked
    clicked += 1
    if clicked == 1:
        pauseBtn.config(text='resume')
        pygame.mixer.music.pause()
    if clicked == 2:
        clicked = 0
        pauseBtn.config(text='pause')
        pygame.mixer.music.unpause()
    print(clicked)
queueLabel=Label(
    master=root,
    text="Queue:"
)
queueLabel.pack(pady=0, padx =0)
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

pauseBtn = Button(
    master=root,
    command=PauseMusic,
    text='pause'
)

pauseBtn.pack(padx=0,pady=0)
playBtn.pack(padx=0,pady=0)
check_event()
updateUI()
root.mainloop()
pygame.quit()

