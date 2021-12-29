from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('  SIGN IN')
root.geometry('550x560')
root.iconbitmap('approve.ico')
pic = PhotoImage(file=r'C:\Users\mhmdj\PycharmProjects\sololearn\purplebg.png')
bg_image = Label(root, image=pic)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

image_check = Image.open(r'C:\Users\mhmdj\PycharmProjects\sololearn\purplebg.png')
pic_check = ImageTk.PhotoImage(image_check)

image_button = Image.open(r'C:\Users\mhmdj\PycharmProjects\sololearn\SIGNINRpng.png')
resize = image_button.resize((350, 85))
pic_button = ImageTk.PhotoImage(resize)


def indent(event):
    if email.get() == '':
        email.insert(0, '  ')
    elif email.get()[0:2] != '  ':
        email.insert(0, '  ')

    if password.get() == '':
        password.insert(0, '  ')
    elif password.get()[0:2] != '  ':
        password.insert(0, '  ')


def place_holder(event):
    if email.get() == '  example@gmail.com':
        email.delete(0, 'end')


def place_holder1(event):
    if password.get() == '  password':
        password.delete(0, 'end')


email = Entry(root, font='Arial 20 bold', relief=FLAT, fg='#ab23ff', insertbackground='purple')
email.place(x=80, y=100, height=90, width=400)

password = Entry(root, font='Arial 20 bold', relief=FLAT, fg='#ab23ff', insertbackground='purple')
password.place(x=80, y=220, height=90, width=400)

sign_in = Button(root, font='Arial 20 bold', relief=SOLID, fg='#ab23ff',
                 activebackground='#ab23ff', image=pic_button, )
sign_in.place(x=180, y=400, height=70, width=190)

# The best CheckButton
image = PhotoImage(file='check.png')
checkbutton = Checkbutton(root, fg='#ab23ff', relief=RIDGE, bg='#e997ff', activebackground='#bdcaff')
label_img1 = Label(root, image=image)
label_img2 = Label(root, image=image)
label_img3 = Label(root, image=image)
label_img4 = Label(root, image=image)
label_img5 = Label(root, image=pic_check, text='Remember password',
                   font=('courier', 15, 'bold'), compound='center', fg='#ab23ff')

checkbutton.place(x=80, y=315, width=120, height=30)
label_img3.place(x=130, y=316, width=16, height=5)
label_img4.place(x=130, y=337, width=16, height=5)
label_img1.place(x=145, y=316, width=54, height=27)
label_img2.place(x=81, y=316, width=48, height=27)
label_img5.place(x=200, y=316, width=260, height=29)

email.insert(0, '  example@gmail.com')
password.insert(0, '  password')

email.bind('<Key>', indent)
password.bind('<Key>', indent)

email.bind('<Button>', place_holder)
password.bind('<Button>', place_holder1)

mainloop()
