# This is a simple project about creating a simple GUI that is content with the scary image as well as a button when pressing it 
# the scary sound will run.

# requierments:
                '''

                    pip install playsound
                    pip install tkhtmlview

                '''


scary pranks

from tkinter import *
from tkhtmlview import HTMLLabel
from playsound import playsound

root = Tk()
root.attributes('-fullscreen', True)


def play():
    playsound('scarysound.mp3')


image = HTMLLabel(root, html=f'<img src="https://cdn.wallpapersafari.com/90/68/w3upvq.jpg"; />')
image.place(x=-100, y=-120, width=1490, height=860)
b = Button(root, text="SCARY BUTTON", fg='white', bg='black', activebackground='black', command=play)
b.place(x=100, y=100, width=100, height=200)

mainloop()
