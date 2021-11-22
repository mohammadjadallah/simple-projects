# create button and linked it with function to copy text from the entry

import tkinter as t
import pyperclip

root = t.Tk()
root.config(bg='cyan')

entry = t.Entry(root, font="arial 20 bold",
                insertbackground="red",
                bg='pink',
                fg='purple')

entry.pack(padx = 100, pady = 15,
           ipadx = 40, ipady = 25)

btn = t.Button(root, text='Copy',
               font="arial 30 bold",
               command=lambda :copy(),
               bg='yellow',
               fg= 'brown')

btn.pack(ipadx=30, ipady=10)

def copy():
    en = entry.get()
    pyperclip.copy(en)

t.mainloop()
