from tkinter import Label, Button, Listbox, ACTIVE, Tk, Scale, HORIZONTAL, END
import pygame
import tkinter.filedialog as tkf
import os

pygame.init()
pygame.mixer.init()

win = Tk()
win.title('موزیک پلیر')
win.geometry('500x500')

listb = Listbox(win, fg='white', bg='black', font='tahoma')


z = 1

def lod():
    global z
    listb.delete(0, END)
    dirc = tkf.askdirectory()
    if dirc != '':
        os.chdir(dirc)
        dictlis = os.listdir(dirc)
        i = 0
        for file in dictlis:
            if file.endswith('.mp3'):
                listb.insert(i, file)
                i += 1
        if listb.size() != 0 and z == 1:
            volume.pack(fill='x')
            btnplay.pack(fill='x')
            btnpause.pack(fill='x')
            btnunpuse.pack(fill='x')
            btnstop.pack(fill='x')
            global label
            label = Label(win, text=listb.get(ACTIVE), font='tahoma')
            label.pack()
            z = 2


def play():
    pygame.mixer.music.load(listb.get(ACTIVE))
    pygame.mixer.music.play()
    label.config(text=listb.get(ACTIVE))
    pygame.mixer.music.set_volume(volume.get()/100)


def pause():
    pygame.mixer.music.pause()


def unpuse():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()


def chainge_velume(a):
    # a = volume.get()
    # a = a/100
    pygame.mixer.music.set_volume(volume.get()/100)


volume = Scale(win, orient=HORIZONTAL, fg='black', command=chainge_velume, cursor='hand2')
volume.set(50)
btnlod = Button(win, text='وارد کردن پوشه', command=lod, height=2, cursor='hand2')
btnlod.pack(fill='x')
listb.pack(fill='x')
btnstop = Button(win, text='stop', command=stop, height=2, cursor='hand2')
btnplay = Button(win, text='play', command=play, height=2, cursor='hand2')
btnunpuse = Button(win, text='unpause', command=unpuse, height=2, cursor='hand2')
btnpause = Button(win, text='pause', command=pause, height=2, cursor='hand2')

win.mainloop()
