from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator
import pyttsx3

speech = pyttsx3.init()

def speak():
    speech.setProperty('rate',200) #speech speed
    speech.setProperty('volume',1.0) #volumn
    speech.say(box1.get(1.0,END))
    speech.runAndWait()
    speech.stop()

# Tao Tk window
root = Tk()
listen = StringVar()
root.title('Google Galaxy')
root.geometry('500x630')
root.iconbitmap('logo.ico')

load=Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)


name=Label(root,text="translator",fg="#FFFFFF",bd=0,bg="#315a20")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)
box=Text(root,width=28,height=8,font=('Roboto',16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    t = Translator()
    a=t.translate(INPUT,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)


clear_button = Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=80,y=310)
trans_button = Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate)
trans_button.place(x=200,y=310)
listen_button = Button(button_frame,text="Speak",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=speak)
listen_button.place(x=300,y=310)

box1=Text(root,width=28,height=8,font=('Roboto',16))

box1.pack(pady=50)
root.mainloop()


