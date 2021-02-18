import speech_recognition as sr
import time
from playsound import playsound
from translate import Translator
import os
from gtts import gTTS
import os
from gtts import gTTS
from translate import Translator
import os
from gtts import gTTS
from translate import Translator
from PIL import Image , ImageTk   
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import * 
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image 

root = tk.Tk()
root.configure(background="#dbf6e9")
#root.geometry("1300x700")
import sqlite3

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Language Translation")

c=StringVar()
c1=StringVar()
data=StringVar()
data1=StringVar()

lbl = tk.Label(root, text="Speech-to-Text Translation", font=('times', 40,' bold '), height=1, width=30,bg="#dbf6e9",fg="indian red")
lbl.place(x=230, y=10)

frame_alpr1 = tk.LabelFrame(root, text=" --Process-- ", width=680, height=500, bd=5, font=('times', 15, ' bold '),bg="#f6f5f1")
frame_alpr1.grid(row=0, column=0, sticky='nw')
frame_alpr1.place(x=80, y=120)

frame_alpr2 = tk.LabelFrame(root, text=" --Translated text-- ", width=300, height=300, bd=5, font=('times', 15, ' bold '),bg="brown",fg="white")
frame_alpr2.grid(row=0, column=0, sticky='nw')
frame_alpr2.place(x=830, y=180)

def recognise():

    r = sr.Recognizer()
    print("Please talk...")
    l = Label(frame_alpr1, text = "Please talk...") 
    l.config(font =("Courier", 14)) 
    l.pack()
    
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        l1 = Label(frame_alpr1, text = "Recognizing...") 
        l1.config(font =("Courier", 14)) 
        l1.pack()
        data = r.recognize_google(audio_data)
        print("Recognised Speech:"+data)
        l2 = Label(frame_alpr1, text = data) 
        l2.config(font =("Courier", 14)) 
        l2.pack()
        return data
    
def translate_text():
    data1 = recognise()
    print(data1)
    Lang1=c.get()
    print(Lang1)
    Lang2=c1.get()
    print(Lang2)
    translator= Translator(from_lang=Lang1,to_lang=Lang2)
    translation = translator.translate(data1)
    print(translation)
    T = tk.Text(frame_alpr2)
    T.pack()
    T.insert(tk.END, translation)
    
label_1 = Label(frame_alpr1, text="Select Language",height=2,width=20,font=("bold", 10),bg='lightblue4',fg='white')
label_1.place(x=20,y=80)

list1 = ['English','Marathi','Hindi','Telugu','Malayalam','Kannada','Gujarati','Bengali'];
droplist=OptionMenu(frame_alpr1,c, *list1)
droplist.config(height=2,width=25)
c.set('Select From language') 
droplist.place(x=200,y=80)

list2 = ['English','Marathi','Hindi','Telugu','Malayalam','Kannada','Gujarati','Bengali'];

droplist=OptionMenu(frame_alpr1,c1, *list2)
droplist.config(height=2,width=25)
c1.set('Select To language') 
droplist.place(x=400,y=80)

Button(frame_alpr1, text='After Selecting Language... Press Button and Talk....',height=5,width=50,font=('times', 14, ' bold '),bg='brown',fg='white',command=translate_text).place(x=30,y=180)

root.mainloop()