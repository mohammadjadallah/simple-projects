# Let's make a simple passwords generators app
# We will use tkinter and random packages

# Here is the code you should use it to learn

from tkinter import *
from tkinter import ttk
from random import sample

root = Tk()
root.geometry('400x400')
root.resizable(False, False)
root.config(bg= '#91B8D9')
root.title('Password Generator')
largFont = ('Verdana', 12)
style = ttk.Style()

def Gen():
    aToz = ''.join(chr(i) for i in range(97, 123))
    AtoZ = aToz.upper()
    numbers = '0123456789'
    symbols = '(){}[];*-_/,.'
    all = aToz + AtoZ + numbers + symbols
    passwords = ''.join(sample(all, 16))
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    entry.insert(16, passwords)
    entry.configure(state=DISABLED)

def copyText():
    cop_Text = entry.get()
    root.clipboard_clear()
    root.clipboard_append(cop_Text)

style.configure('TLabel', background= '#91B8D9', foreground= '#4C5D70')
label = ttk.Label(root, text="Password", font= ("normal", 17, 'bold'))
label.place(x=25, y=150)
entry = ttk.Entry(root, textvariable= largFont, font= largFont)
entry.place(width=200, height= 30, x=150, y= 150)

style.configure('TButton', font= ("Arial", 15, "bold"), foreground="#4C5D70")
btn = ttk.Button(root, text= "Generate")
btn.place(width = 200, height= 40, x = 150, y = 200)

btn2 = ttk.Button(root, text= 'Copy')
btn2.place(width = 200 , height = 50, x = 150, y = 250)

btn.config(command=Gen)
btn2.config(command=copyText)
entry.configure(state=DISABLED)

mainloop()

