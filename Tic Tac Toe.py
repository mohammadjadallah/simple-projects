# In this code we will learn about How do simple game like Tic-Tac-toe
# Library -> Tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('422x350')
root.resizable(FALSE, FALSE)
root.title('                                          Tic Tac toe')
root.configure(bg='gray')

# This function to make The buttons disabled

def disabled():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)

# If you want to start with O you should change click1 = False
# And count this variable to increase 1 with each press on button even reach to 9 presses
click1 = True
count = 0

#This function to make X and O present on button when you click any button
def press(buttonStr):
    global click1, count
    if click1 == True and buttonStr['text'] == " ":
        #textvariable = buttonStr1
        buttonStr['text'] = "X"
        click1 = False
        win()
        count += 1


    elif click1 == False and buttonStr['text'] == " ":
        buttonStr['text'] = "O"
        click1 = True
        win()
        count += 1

    else:
        messagebox.showerror("Tic Tac Toe", "Sorry but this box clicked two times")


#This function to Specify the winner

def win():
    global click1, count

    # Chick for X
    if btn1['text'] == btn2['text'] == btn3['text'] == 'X':
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn4["text"] == btn5["text"] == btn6["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn7["text"] == btn8["text"] == btn9["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn7["text"] == btn5["text"] == btn3["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn1["text"] == btn5["text"] == btn9["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn1["text"] == btn4["text"] == btn7["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn2["text"] == btn5["text"] == btn8["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    elif btn3["text"] == btn6["text"] == btn9["text"] == "X":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "X Won")
        disabled()

    # Chick for O
    if btn1["text"] == btn2["text"] == btn3["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn4["text"] == btn5["text"] == btn6["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn7["text"] == btn8["text"] == btn9["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn7["text"] == btn5["text"] == btn3["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn1["text"] == btn5["text"] == btn9["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn1["text"] == btn4["text"] == btn7["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn2["text"] == btn5["text"] == btn8["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif btn3["text"] == btn6["text"] == btn9["text"] == "O":
        click1 = True
        messagebox.showinfo("Tic Tac Toe", "O Won")
        disabled()

    elif (count == 8):
        disabled()
        messagebox.showinfo('Tic Tac Toe', 'It is a Tie')


buttonStr = StringVar()

# And Here All The Buttons

btn1 = Button(root, text=" ", font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn1))
btn2 = Button(root, text=" ", font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn2))
btn3 = Button(root, text=" ", font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn3))
btn4 = Button(root, text=" ", font=("normal", 20, "bold"),  relief=SUNKEN
              , command=lambda: press(btn4))
btn5 = Button(root, text=" ", font=("normal", 20, "bold"),  relief=SUNKEN
              , command=lambda: press(btn5))
btn6 = Button(root, text=" ", font=("normal", 20, "bold"),  relief=SUNKEN
              , command=lambda: press(btn6))
btn7 = Button(root, text=" ", font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn7))
btn8 = Button(root, text=" ", font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn8))
btn9 = Button(root, text=" ",  font=("normal", 20, "bold"), relief=SUNKEN
              , command=lambda: press(btn9))

btn1.place(width=140, height=115, x=0,   y=0)
btn2.place(width=140, height=115, x=140, y=0)
btn3.place(width=140, height=115, x=280, y=0)
btn4.place(width=140, height=115, x=0,   y=115)
btn5.place(width=140, height=115, x=140, y=115)
btn6.place(width=140, height=115, x=280, y=115)
btn7.place(width=140, height=115, x=0,   y=230)
btn8.place(width=140, height=115, x=140, y=230)
btn9.place(width=140, height=115, x=280, y=230)

root.mainloop()
