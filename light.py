# Turn the light on and off

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x600")
root.title('Light App')
img_off = ImageTk.PhotoImage(Image.open(r'turnOffLight.png'))
img_on = ImageTk.PhotoImage(Image.open(r'turnOnLight.png'))
global isOn
isOn = True


def turn_on_light():
    global isOn

    if isOn:
        turn_off_.configure(image=img_off)
        turn_light['text'] = 'شغلني'
        isOn = False
    else:
        turn_off_.configure(image=img_on)
        turn_light['text'] = 'اطفيني'
        isOn = True


turn_off_ = Label(root, image=img_off)
turn_light = Button(root, text='شغلني', width=100, font='normal 40 bold',
                    relief=SOLID, bd=5, command=lambda: turn_on_light())

turn_off_.pack(side='left')
turn_light.place(x=540, y=10, width=250, height=250)

mainloop()
