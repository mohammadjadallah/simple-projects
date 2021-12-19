# This app will help user to open URL
# just put the URL and open it when you press on button
# you must put the full path url like https://github.com/Mohammad2002-web/simple-projects
# or from www. like www.youtube.com

from tkinter import *
from webbrowser import get

root = Tk()
root.title('open site')
root.iconbitmap('websitesopen.ico')
root.geometry('600x500')
root.resizable(0, 0)


def pre_space(event):
    if link.get() == '':
        link.insert(0, ' ')
    elif link.get()[0] != ' ':
        link.insert(0, ' ')


def place_holder(event):
    if link.get() == '                    Enter URL':
        link.delete(0, END)


def open_site():
    get('windows-default').open(str(link.get()).strip())

# windows-default
# www.youtube.com

try:
    link = Entry(root, font='normal 20 bold', insertbackground='purple',
                 bg='lightgray')

    link.grid(row=2, column=0, rowspan=1, padx=80, pady=0, ipadx=70, ipady=15)
    link.insert(0, '                    Enter URL')
    label = Label(root, text='Enter the URL to open the site', font='arial 20 bold',
                  fg='green')
    label.grid(row=1, column=0, pady=30)

    go = Button(root, text='Go to the site', font='arial 20 bold', bg='purple', fg='white',
                relief=SOLID, activebackground='lightgray', bd=4, cursor='hand2')
    go.grid(row=3, column=0, columnspan=1, padx=0, pady=50, ipadx=40, ipady=20)

    link.bind('<Key>', pre_space)
    link.bind('<Button>', place_holder)

    go.config(command=lambda: root.after(1, open_site()))
except TclError.args:  # this to avoid the error (TclError) 
    pass

mainloop()
