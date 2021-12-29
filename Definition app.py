#                                                           Definition App
# let's make a simple app to find the words definition   
# pip install textblob
# GUI is tkinter

from textblob import *
from tkinter import *

# get the meaning
def definition():
    getTextEntry = entry.get()[1:]
    word = Word(getTextEntry)
    STR.set('\n.'.join(word.definitions[0:4]))


# Create a place-holder
def place_holder(event):
    if entry.get() == '          Enter the word':
        entry.delete(0, END)


# spaces before write in entry
def spaces(event):
    if entry.get() == '':
        entry.insert(0, ' ')

    elif entry.get()[0] != ' ':
        entry.insert(0, ' ')


# Setup GUI
root = Tk()
root.geometry('440x560')
root.resizable(0, 0)
root.title('Definition App')
STR = StringVar()

entry = Entry(root, font=('Normal bold', 17),
              insertbackground='#C55FFC')
btn = Button(root, font=('Normal bold', 10),
             text='search',
             bg='#C55FFC',
             fg='white',
             relief=SUNKEN,
             bd=0,
             activebackground='#C55FFC',
             )

message = Message(root, textvariable=STR,
                  font=('Normal bold', 14))

message.place(x=30, y=200)
btn.config(command=lambda: definition())
btn.after(1, definition())
btn.place(x=285, y=100, width=110, height=60)
entry.place(x=20, y=100, width=260, height=60)
entry.insert(0, '          Enter the word')
entry.bind('<Button>', place_holder)
entry.bind('<Key>', spaces)

root.mainloop()
