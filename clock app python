#                                                             make your own clock

# libraries 👇
  # tkinter 
  # datetime

#------------------------------------------------
#The code::::::::::::::::
#------------------------------------------------

from tkinter import *
from datetime import datetime, date

# This function to bring time+date and insert it in (Label)

def liveTime():
    currentTime = datetime.now().time().strftime('%H:%M:%S')
    dateDay = date.today().strftime('%d/%m/%Y')
    clockLive.config(text=currentTime)
    clockLive.after(1, liveTime) #  This makes time in unfix (changing)
    Date.config(text=dateDay) 


#  Prepare GUI 

if __name__ == '__main__':
    root = Tk()
    root.geometry('550x220')
    root.resizable(1, 1)
    root.config(bg='#1e313f')
    root.title('                                   '
               '                                     clock')
    clockLive = Label(root, font='Normal 60 bold',
                      fg='white', bg='#1e313f')

    Date = Label(root, font='Normal 30 bold',
                      fg='white', bg='#1e313f')

    clockLive.place(x=120, y=70)
    Date.place(x=180, y=20)
    liveTime()
    mainloop()
