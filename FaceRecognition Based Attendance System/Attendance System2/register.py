# from tkinter import *
# from tkinter.font import Font
# from tkinter import messagebox
#
# win = Tk()
# win.title("Ragistration_form ")
# win.geometry("500x500")
# win.configure(background='aqua')
#
# l1 = Label(win, text="RAGISTRATION FORM ", bg='aqua', fg='grey', font=("bold", 30))
# l1.pack(fill=X)
#
# Label(text="FIRST NAME : ", bg="aqua", fg='black', font=("bold", 15)).place(x=60, y=70)
# Label(text="LAST NAME : ", bg="aqua", fg='black', font=("bold", 15)).place(x=60, y=120)
# Label(text="E-MAIL : ", bg="aqua", fg='black', font=("bold", 15)).place(x=60, y=170)
# Label(text="MOBILE NO. :", bg="aqua", fg='black', font=("bold", 15)).place(x=60, y=220)
# Label(text="CITY :", bg="aqua", fg='black', font=("bold", 15)).place(x=60, y=270)
# # RADIO BUTTON >>>>>>>>>>>>>>>
# l5 = Label(win, text="GENDER", bg='aqua', fg='black', font=("bold", 15)).place(x=60, y=320)
# Radiobutton(win, text='Male', padx=5, variable='var', value=1, bg='aqua').place(x=250, y=320)
# Radiobutton(win, text='Female', padx=20, variable='var', value=2, bg='aqua').place(x=320, y=320)
#
# l2 = Entry(win, width="30").place(x=250, y=70)
# l3 = Entry(win, width='30').place(x=250, y=120)
# l4 = Entry(win, width='30').place(x=250, y=170)
# l6 = Entry(win, width='30').place(x=250, y=220)
# l7 = Entry(win, width='30').place(x=250, y=270)
#
#
# def register():
#     print(l2.get())
#
#
# Button(win, text="RAGISTER ", width="20", fg="white", bg='grey', command="register", font=("bold", 13)).place(x=165,
#                                                                                                               y=370)
# Button(win, text="CANCLE ", width="20", fg="white", bg='grey', command="Register", font=("bold", 13)).place(x=165,
#                                                                                                             y=420)
# win.mainloop()

from tkinter import *

win = Tk()
win.title('Registration Form')
win.geometry('500x500')
win.configure(background='aqua')

Label(win,text='Registration Form',bg='aqua',fg='grey',font=('bold,30')).pack(fill=X)

Label(win, text="Name", bg='aqua', fg='grey').place(x=60,y=70)
e1 = Entry(win,width="30").place(x=250,y=70)


Label(win, text="Name", bg='aqua', fg='grey').place(x=60,y=100)
e2 = Entry(win,width="30").place(x=250,y=100)

win.mainloop()