from tkinter import *
from tkinter.ttk import Separator
import pygame
import pygame.mixer as mp 
import tkinter.filedialog as tkf
import os
from mutagen.mp3 import MP3
import time

# set icon button
repetion = 1
time_end_music = 0
def target():
    if mp.music.get_busy() == 1:
        global time_end_music
        time_n = mp.music.get_pos()/1000
        m, s= seconds_to_time(time_n)
        label_new.config(text= '{}:{}'.format(m, s))
        timezone.set(int((time_n/time_end_music)*100))
    else:
        global name_music
        if name_music == '':
            pass
        else:
            if repetion == 1:
                pass
            elif repetion == 2:
                next_button_comand()
            elif repetion == 3:
                mp.music.unload()
                mp.music.load(name_music)
                mp.music.play()
        # add repetion
    label_new.after(1000, target)

# add repetition to multiprocessing

def seconds_to_time(seconds: int) -> tuple:
    lang = int(seconds)
    mint = lang // 60
    secend = lang % 60
    return (mint, secend)


def get_lang_mp4(filename: str) -> tuple:  
    ''' get_lang_mp4(filename) -> tuple
    
    this function returns (minutes, seconds)-> `minutes : seconds`   of the MP4 file'''
    audio = MP3(filename)
    lang = int(audio.info.length)
    mint = lang // 60
    secend = lang % 60
    global time_end_music
    time_end_music = lang
    return (mint, secend)

    
pygame.init()
mp.init()

win = Tk()
win.title('موزیک پلیر')
win.geometry('500x500')

listb = Listbox(win, fg='white', bg='black', font='tahoma')

list_box_in = []
name_music = ''
z = 1

def lod():
    global z
    listb.delete(0, END)
    dirc = tkf.askdirectory()
    if dirc != '':
        os.chdir(dirc)
        dictlis = os.listdir(dirc)
        global list_box_in
        list_box_in = dictlis
        i = 0
        for file in dictlis:
            if file.endswith('.mp3'):
                listb.insert(i, file)
                i += 1
        if listb.size() != 0 and z == 1:
            # pack widget
            scale_timezone_form.pack(fill='x')
            Separator(win).pack(fill='x')
            form_bottom.grid(pady=5, padx= 5, column= 2, row= 0, sticky='ne')
            main_frame.pack(side='top', pady=10)

            volume_form.pack(fill='x')
            global label
            label = Label(win, text=listb.get(ACTIVE), font='tahoma')
            label.pack()

            z = 2

status_play = 1

def play():
    global status_play
    global name_music
    if status_play == 1:
        if name_music != listb.get(ACTIVE):
            load = listb.get(ACTIVE)
            mp.music.unload()
            mp.music.load(load)
            name_music = load
            m, s= get_lang_mp4(name_music)
            label_end.config(text='{}:{}'.format(m,s))
            mp.music.play()
            win.title(' موزیک پلیر ' + name_music)
            label.config(text=load)
            mp.music.set_volume(volume.get()/100)
            status_play = 2 
            play_pause.config(text='pause')  
        elif name_music == listb.get(ACTIVE):
            mp.music.pause()
            status_play = 2 
            play_pause.config(text='play')
    elif status_play == 2:
        mp.music.unpause()
        status_play = 1
        play_pause.config(text='pause')


def next_button_comand():
    global name_music
    global list_box_in
    load = list_box_in[list_box_in.index(name_music) + 1]
    mp.music.unload()
    mp.music.load(load)
    name_music = load
    m, s= get_lang_mp4(name_music)
    label_end.config(text='{}:{}'.format(m,s))
    mp.music.play()
    win.title(' موزیک پلیر ' + name_music)
    label.config(text=load)
    mp.music.set_volume(volume.get()/100)
    listb.selection_set(name_music, 'active')

       

def back_button_comand():
    global name_music
    global list_box_in
    load = list_box_in[list_box_in.index(name_music) - 1]
    mp.music.unload()
    mp.music.load(load)
    name_music = load
    m, s= get_lang_mp4(name_music)
    label_end.config(text='{}:{}'.format(m,s))
    mp.music.play()
    win.title(' موزیک پلیر ' + name_music)
    label.config(text=load)
    mp.music.set_volume(volume.get()/100)
    listb.selection_set(name_music, 'active')

    

def chainge_velume(a):
    pygame.mixer.music.set_volume(volume.get()/100)


def volume_comand():
    if mp.music.get_volume() == 0:
        pygame.mixer.music.set_volume(volume.get()/100)
    else:
        pygame.mixer.music.set_volume(0)
        
# def timezone_comand(in_):
#     in_ = int(in_)
#     global time_end_music
#     new_ = (in_ * time_end_music)/ 100
#     mp.music.set_pos(float(new_))
#     time_n = mp.music.get_pos()/1000
#     timezone.set(int((time_n/time_end_music)*100))

def rep():
    global repetion
    if repetion == 0:
        br.config(text='rep grop')
        repetion = 1
    elif repetion == 1:
        repetion = 2
        br.config(text='rep one')
    elif repetion == 2:
        repetion = 0
        br.config(text='no rep')

# head app
btnlod = Button(win, text='وارد کردن پوشه', command=lod, height=2, cursor='hand2')
btnlod.pack(fill='x')
listb.pack(fill='x')

# main frame 
main_frame = Frame(win)


# time zone 
scale_timezone_form = Frame(win)
# command= timezone_comand
timezone = Scale(scale_timezone_form, to=100, orient= HORIZONTAL)
timezone.pack(fill='x')

# time label end time  and   new time
label_end = Label(scale_timezone_form, text= 'mm:ss', font='tahoma')
label_new = Label(scale_timezone_form, text= 'mm:ss', font='tahoma')
label_new.pack(side='left')
label_end.pack(side='right')

# volume change
volume_form = Frame(win)
volume = Scale(volume_form, orient=HORIZONTAL, command=chainge_velume, cursor='hand2')
volume.set(50)
volume.pack(fill='x')
Label(volume_form,text= 'change volume', font='tahoma', fg= 'blue').pack(side='left')



# play and pause and next and back and ...
form_bottom = Frame(main_frame)
play_pause = Button(form_bottom, text= 'play', font='tahoma', width= 4, height=2, bd= 3, command= play)
play_pause.grid(column= 1, row= 0, padx=4)

back_button = Button(form_bottom, text= 'back', font='tahoma', width=5, height=1, bd= 3, command= back_button_comand)
back_button.grid(column= 0, row= 0, padx=4)

next_button = Button(form_bottom, text= 'next', font='tahoma', width= 5, height= 1, bd= 3, command=next_button_comand)
next_button.grid(column= 2, row = 0, padx=4)

# button for repete and volume 
br = Button(main_frame, bd= 4, width=4, height=2, text="no rep", command=rep)
br.grid(padx= 10, column= 0, row= 0)

bv = Button(main_frame, bd=4, width=4, height=2, text= "V", command= volume_comand)
bv.grid(padx=10 , column=4, row= 0)





target()


win.mainloop()
